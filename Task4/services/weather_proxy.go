package services

import (
	"fmt"
	"os"
	"time"
	"weatherapp/database"
	"weatherapp/models"

	"github.com/go-resty/resty/v2"
)

type WeatherAPIResponse struct {
	Weather []struct {
		Description string `json:"description"`
	} `json:"weather"`
	Main struct {
		Temp float64 `json:"temp"`
	} `json:"main"`
}

func FetchWeather(city string) (*models.Weather, error) {
	apiKey := os.Getenv("WEATHER_API_KEY")
	if apiKey == "" {
		return nil, fmt.Errorf("brak klucza API – sprawdź plik .env lub zmienną środowiskową")
	}

	url := fmt.Sprintf("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric", city, apiKey)

	client := resty.New().
		SetTimeout(10 * time.Second)

	var res WeatherAPIResponse
	resp, err := client.R().
		SetResult(&res).
		Get(url)

	if err != nil {
		return nil, fmt.Errorf("błąd pobierania danych z API: %v", err)
	}

	fmt.Println("STATUS:", resp.Status())
	fmt.Println("BODY:", resp)

	if len(res.Weather) == 0 {
		return nil, fmt.Errorf("brak danych pogodowych dla %s", city)
	}

	weather := &models.Weather{
		City:        city,
		Temperature: res.Main.Temp,
		Condition:   res.Weather[0].Description,
	}

	database.DB.Create(weather)
	return weather, nil
}

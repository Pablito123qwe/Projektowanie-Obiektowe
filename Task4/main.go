package main

import (
	"github.com/joho/godotenv"
    "log"
    "weatherapp/database"
    "weatherapp/controllers"
    "github.com/labstack/echo/v4"
)

func main() {
	err := godotenv.Load()
    if err != nil {
        log.Fatal("Error loading .env file")
    }
    database.InitDB()
    e := echo.New()

    e.GET("/weather", controllers.GetWeather)
    e.POST("/weather", controllers.GetWeather)

	e.GET("/", func(c echo.Context) error {
    return c.JSON(200, echo.Map{
        "message": "API działa! Użyj /weather?city=Miasto",
    })
	})

    e.Logger.Fatal(e.Start(":8080"))
}

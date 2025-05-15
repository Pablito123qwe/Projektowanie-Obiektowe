package controllers

import (
	"net/http"
	"weatherapp/services"

	"github.com/labstack/echo/v4"
)

type RequestBody struct {
	City string `json:"city"`
}

func GetWeather(c echo.Context) error {
	var req RequestBody

	city := c.QueryParam("city")
	if city == "" {
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, echo.Map{"error": "Missing city parameter"})
		}
		city = req.City
	}

	weather, err := services.FetchWeather(city)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, echo.Map{"error": err.Error()})
	}

	return c.JSON(http.StatusOK, weather)
}

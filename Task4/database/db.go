package database

import (
	"weatherapp/models"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func InitDB() {
	var err error
	DB, err = gorm.Open(sqlite.Open("weather.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	DB.AutoMigrate(&models.Weather{})

	DB.Create(&models.Weather{City: "Warsaw", Temperature: 20, Condition: "Sunny"})
}

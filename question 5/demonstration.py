import random
from datetime import date, timedelta
import weather_module

# Generate dates for the period 1st August 2023 to 10th July 2024
startDate = date(2023, 8, 1)
endDate = date(2024, 7, 10)

delta = (endDate - startDate).days
# Generate a list of dictionaries to store weather data
weatherData = []
for i in range(delta):
    day = startDate + timedelta(i)
    max_temp = round(random.uniform(25, 35), 1)  # Random max temp between 25 and 35°C
    min_temp = round(random.uniform(5, 25), 1)  # Random min temp between 15 and 25°C
    humidity = random.randint(50, 100)  # Random humidity between 50% and 100%

    weatherData.append({
        "date": day.strftime('%Y-%m-%d'),
        "max_temp": max_temp,
        "min_temp": min_temp,
        "humidity": humidity
    })

    result = weather_module.highLowWeek(weatherData, "2023-08-01")
print(" highest and lowest temperature for a week from 2023-08-01 is:\n", "highest temp : ", result[0], "\n lowest temp : ", result[1])


import weather_module
print("number of days with temperature above 30 : ", weather_module.tempAbove30(weatherData))

print("average humidity for 6 days from 2024-07-05 is : ", weather_module.avgHumidity(weatherData, "2024-07-05", 6))
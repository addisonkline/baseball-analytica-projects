import requests
import csv
from datetime import datetime, timedelta
from time import sleep

# New York: USW00094728
# Denver: USW00003017
# Kansas City: USW00003947
# Atlanta: USW00013874
# Minnesota: USW00014922
# Los Angeles: USW00093134

def fetch_weather_data(start_date, end_date):
    base_url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00003947&startDate={}&endDate={}&format=json"
    data = []

    current_date = start_date
    while current_date <= end_date:
        sleep(3)
        url = base_url.format(current_date.strftime("%Y-%m-%d"), current_date.strftime("%Y-%m-%d"))
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            if len(weather_data) > 0:
                max_temp = int(weather_data[0].get('TMAX', None)) / 10  # temperature in Celsius
                min_temp = int(weather_data[0].get('TMIN', None)) / 10  # temperature in Celsius
                humidity = int(weather_data[0].get('ADPT', None)) / 10  # average dew point in Celsius
                precipitation = float(weather_data[0].get('PRCP', None)) / 10  # precipitation in millimeters
                data.append([current_date.strftime("%Y-%m-%d"), max_temp, min_temp, humidity, precipitation])
                print(f'{str(current_date)} successfully accessed')
        current_date += timedelta(days=1)

    return data

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Max Temperature (°C)', 'Min Temperature (°C)', 'Humidity', 'Precipitation (mm)'])
        writer.writerows(data)

if __name__ == "__main__":
    start_date = datetime(2023, 3, 25)
    end_date = datetime(2023, 10, 5)

    weather_data = fetch_weather_data(start_date, end_date)
    write_to_csv(weather_data, 'data/climate_data_KCR.csv')
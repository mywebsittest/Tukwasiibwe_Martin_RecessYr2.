import requests
import csv
import json
from bs4 import BeautifulSoup

# Replace api_key with your actual API key
api_key = '336e6e8bd4820f250616b1c3d5529e08'
city = 'Kampala'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
weather_data = response.json()

# response = requests.get(url)
# weather_data = response.json()

# Print the complete response data


# Step 4: Extract relevant data
data = {
    'city': weather_data.get('name'),
    'weather': weather_data['weather'][0]['description'],
    'temperature': weather_data['main']['temp'],
    'humidity': weather_data['main']['humidity'],
    'pressure': weather_data['main']['pressure'],
}

# Step 5: Save the data to a CSV file
csv_file = 'weather_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)

# Step 6: Save the data to a JSON file
json_file = 'weather_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    
#step 7: save successfully to csv and json format

print('Data saved successfully to{csv_file} and {json_file} format')
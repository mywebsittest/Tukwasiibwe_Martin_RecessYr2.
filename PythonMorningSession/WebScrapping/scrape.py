

#Libraries for web scraping
#Request, BeautifulSoup, lxml, scrapy, Selenium
#API Keys
#Exercise, openweathermap.org 

#Step 1:
import requests
from bs4 import BeautifulSoup
import csv
import json

#Step 2: Fetch the web pages 

url= 'http://ryeko.org'
response = requests.get(url)
html_content = response.text

#step 3: Parse the html using BeatifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

#step 4: find the specific data

data = []

for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title':title, 'link':link})

#step 5: save the data to csv file 

csv_file = 'scraped_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title','link'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
        
#step 6 : save the data to a JSON file
json_file = 'scraped_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    
#step 7: save successfully to csv and json format

print('Data saved successfully to{csv_file} and {json_file} format')

#Execrise 1: Scrape data from the http://openweathermap.org
#current weatherdata


    
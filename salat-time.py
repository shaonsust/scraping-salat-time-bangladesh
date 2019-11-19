import requests
from bs4 import BeautifulSoup
import json

def getContent(url):
    # Connect to the url and get html string response
    response = requests.get(url)

    # Parse HTML content and make beautiful soap object
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup
    
def getCity():
    # Parse HTML and make beautiful soup object
    soup = getContent('https://www.islamicfinder.org/world/bangladesh/')

    # target city table div
    div = soup.find('div', attrs = {'id' : 'top-city-table'})

    # Get all <a> attribute tag for taking city name
    aa = div.findAll('a')

    cities = []
    for a in aa:
        cities.append(a.text.strip().lower())

    return cities

def getPrayerTime():
    # Get city name
    cities = getCity()

    for city in cities:
        # Parse HTML and get content
        soup = getContent('https://www.salahtimes.com/bangladesh/' + city)

getCity()
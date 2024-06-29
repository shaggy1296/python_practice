
#simple_weather
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


def get_city_url(city_name):
    search_url = f'https://www.accuweather.com/en/search-locations?query={city_name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for result in soup.find_all('a', href=True):
            if city_name.lower() in result['href'].lower():
                city_url = 'https://www.accuweather.com' + result['href']
                return city_url
        else:
            print(f"No results found for {city_name}")
            return None
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        return None


def get_weather_data(city_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(city_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        current_temp = soup.find('div', class_='temp')

        if current_temp :
            current_temp = current_temp.get_text(strip=True)
            return current_temp
        else:
            print("Could not find weather data on the page.")
            return None, None
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        return None, None


def main():
    city_name = input("Enter city name: ")
    city_url = get_city_url(city_name)
    if city_url:
        current_temp = get_weather_data(city_url)
        if current_temp :
            print(f"Current Temperature in {city_name}: {current_temp}")


if __name__ == "__main__":
    main()

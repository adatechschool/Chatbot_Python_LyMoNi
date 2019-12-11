import configparser
import requests
import sys
import os

cnf_file = os.path.join(os.path.dirname(__file__), 'config.ini')

def get_api_key():
    config = configparser.ConfigParser()
    config.read(cnf_file)
    ret = config['openweathermap']['api']
    return ret

def get_weather(location, api):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api)
    r = requests.get(url)
    return r.json()

def weather(*args):
    api = get_api_key()
    city = args[0]

    data = get_weather(city, api)
    return data

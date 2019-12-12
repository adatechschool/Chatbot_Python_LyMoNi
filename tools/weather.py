import configparser, requests, sys, os

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

def constuct_report(data):
    # weather_data = list(data)

    weather_data = ['weather', 'main', 'wind', 'sys']
    weather_exact = ['main', 'temp', 'feels_like', 'temp_max', 'temp_min', 'humidity', 'speed', 'country', 'name']

    print(data['weather']['main'])


    for i in weather_data:
        if i in data:
            for y in weather_exact:
                if y in data[i]:
                    print(data[i][y])


def weather(*args):
    if None in args:
        return 'You have to chose a city.'
    api = get_api_key()
    city = args[0]
    data = get_weather(city, api)

    constuct_report(data)

    # print(list(data[main[1]]))
    #
    # weather_report = '\nToday there are/is {}.'.format(data[1][1])

    return 1

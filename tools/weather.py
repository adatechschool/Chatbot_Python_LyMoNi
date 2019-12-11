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
    main = list(data)

    main_index = [1, 3, 5, 8]
    weather_index = [1]
    main_index = [0, 1, 2, 3, 5]
    wind_index = [0]
    sys_index = [2, 7]

    main_l = []

    for i in main_index:
        main_l.append(main[i])

    for i in weather_index:
        weather_l = list(data[main_l[0]])

    for i in main_l:
        print(i)
        # for x in weather_l:
        #     print()
            #print(data[i][x])
    # print(data[main_l[0]][weather_l[i]])

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

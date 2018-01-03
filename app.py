import pyowm


API_key = 'Set your api key'
owm = pyowm.OWM(API_key)

search = True

while search:
    city = input('Enter the city: ')

    try:
        search = False
        observation = owm.weather_at_place(city)

        w = observation.get_weather()

        # Weather details
        wind = w.get_wind()
        humidity = w.get_humidity()
        temperature = w.get_temperature('celsius')

        print(
            'Weather in the ' + city + ' is a ' + str(w.get_detailed_status()) + ' \n' +
            'wind: ' + str(wind['speed']) + ' m/s \n' +
            'humidity: ' + str(humidity) + ' mm \n' +
            'temperature: ' + str(int(temperature['temp'])) + u"\u2103"
        )
    except Exception as e:
        print("Error: " + str(e))
        search = True

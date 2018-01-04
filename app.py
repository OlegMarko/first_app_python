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
            'Weather in the {} is a {} \n'.format(city, w.get_detailed_status()) +
            'wind: {} m/s \n'.format(wind['speed']) +
            'humidity: {} mm \n'.format(humidity) +
            'temperature: {} \u2103'.format(int(temperature['temp']))
        )
    except Exception as e:
        print("Error: " + str(e))
        search = True

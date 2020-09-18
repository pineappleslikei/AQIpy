import requests
import credentials as cred
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
startup_message = "Welcome to Chris' Air Quality Index lookup service"
print(startup_message)


def get_aqi(zipcode):
    response = requests.get(
        f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={str(zipcode)}&date={today}&distance=5&API_KEY={cred.token}').json()
    if len(response) == 0:
        print('Sorry, no data for this zip code.')
    if len(response) > 0:
        for sensor in response:
            if sensor['ParameterName'] == 'PM2.5':
                aqi = sensor['AQI']
                category = sensor['Category']['Name']
                break
        print(f'Today the AQI for {zipcode} is {aqi}\n{category}')


def main():
    quit = False
    responses = ['y', 'n']
    while quit == False:
        while True:
            try:
                zipcode = input("Please enter a zip code:")
            except:
                print('You need to enter a valid 5-digit zip code.')
            if len(zipcode) != 5:
                print('You need to enter a valid 5-digit zip code.')
                continue
            else:
                break
        get_aqi(zipcode)
        while True:
            cont = input("Would you like to look up another one?(y/n):")
            if cont not in responses:
                print("Invalid resposne. Please enter 'y' or 'n' ")
                continue
            if cont == 'n':
                exit()
            if cont == 'y':
                break
        main()


main()

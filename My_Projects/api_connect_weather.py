#Attempts to connect to Open Weather api via python

import requests
import json

api_key = '10e0eab204568320634ff5d1096bc32f'

# res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%r,us&appid=%s' % (zip_code, api_key))

# if res:
#     print("Boom shaka laka!")
# else:
#     print("Epic fail :(")

# print(res.headers)

# header = res.headers

# r = res.json()

# res_json = json.dumps(r, indent=2, sort_keys=True)

# print(res_json)

# location = r['name']
# local_weather = r['weather'][0]['description']

# print("We are in %s and the weather is %s!" % (location, local_weather))

# def locals_only():
#     res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%r,us&appid=%s' % (zip_code, api_key))
#     r = res.json()
#     location = r['name']
#     local_weather = r['weather'][0]['description']
#     if local_weather == "clear sky":
#         print('You should go to %s the weather there is AWESOME!' % location)
#     else:
#         print("It\'s gross in %s! Stay the fuck home!" % location)
#
# print("Want to know the weather?")
# answer = input("> ")
#
# if "yes" in answer:
#     print("Cool! What's your zip code?")
#     zip_code = int(input("> "))
#     locals_only()
# else:
#     print("Peace Out!")


class Weather(object):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=90291r,us&appid=%s' % api_key)
    r = res.json()

import json
import requests
import datetime
from sys import exit
import os
import pyfiglet
from colored import fg, bg, attr

os.system('clear')

#API call
res = requests.get('https://api.adviceslip.com/advice')
#Convert response to json
r = res.json()

result = pyfiglet.figlet_format("Random Advice", font = 'slant')
print('%s%s%s' % (fg(10), result, attr(0)))

# res = requests.get('https://api.adviceslip.com/advice')
#
# r = res.json()
#
# pretty = json.dumps(r, indent=2, sort_keys=True)
#
# print(pretty)

# random_advice = r['slip']['advice']

#Determine the date
date = datetime.datetime.now()
day_week = date.strftime(("%A"))
month = date.strftime(("%b"))
day_month = date.strftime(("%d"))
year = date.strftime(("%Y"))

def advice_generator():
    random_advice = r['slip']['advice']
    print("\nHere\'s your peice of advice for %s %s %s,%s:" % (day_week, month, day_month, year))
    print("%s%s%s\n" % (fg(10), random_advice, attr(0)))

start = input("If you\'d like to get some random advice today press enter, or type q to quit: > ")

if "q" in start:
    print("You\'re missing out :(")
    exit(0)
else:
    advice_generator()

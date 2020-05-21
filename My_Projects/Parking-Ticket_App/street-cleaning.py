import requests
import json
from pprint import pprint
from collections import namedtuple

#Import street cleaning data via LA open source API

request = requests.get('https://data.lacity.org/resource/krk7-ayq2.json?$limit=5')
data = request.json()
pretty_json = json.dumps(data, indent=2, sort_keys=True)

# print(pretty_json)


# Cleaning up Weekday abberviations
days = []
weekdays = []
time_start = []
time_end = []
streets = []
for i in data[2:]:
    if len(i['route_no'].split(' ')) == 2:
        route = (i['route_no'].split(' '))
        days.append(route[1])
    time_start.append(i['time_start'])
    time_end.append(i['time_end'])
    streets.append(i['boundaries'])
for i in days:
    full_days = i.replace('M', 'Monday').replace('Tu', 'Tuesday').replace('W',
    'Wednesday').replace('Th', 'Thursday').replace('F','Friday')
    weekdays.append(full_days)


schedules = []
for d, ts, te, l  in zip(weekdays, time_start, time_end, streets):
    ind_schedule = {'day': d, 'time_start': ts, 'time_end': te, 'location': l}
    schedules.append(ind_schedule)

pprint(schedules[0]['day'])

#Dictionaries

states = {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print some cities
print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

#Print some states
print('-' * 10)
print('Michigan\'s abberviation is: ', states['Michigan'])
print('Florida\'s abberviation is: ', states['Florida'])

#Do it by using the state then cities Dict
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

#Print every state abberviation
print('-' * 10)
for state, abbrev in states.items():
    print('%s is abbreviated %s' % (state, abbrev))

#Now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print('%s state is abbreviated %s and has city %s' % (state, abbrev, cities[abbrev]))

#Safely get an abberviation by state that might not be there
print('-' * 10)
state = states.get('Texas', None)

if not state:
    print('Sorry, no Texas')

#Get a city with a default value
print('-' * 10)
city = cities.get('TX', 'Does not exist')
print("The city for the state of 'TX' is: %s" % city)

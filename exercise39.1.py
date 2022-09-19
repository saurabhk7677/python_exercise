#Create a mapping of state to abbreviation

states = { 
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them 

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities

cities['NY'] = 'New York',
cities['OR'] = 'Portland'

# print out some cities

print('_' * 10)
print("NY state has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states

print('_' * 10)
print("Michigan's abbreviation is: ", states['michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict

print('_', * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('_' * 10)
for abbrev, city in lis(cities.items()):
    print(f"{abbrev} has the city{city}")

# now do both at the same time

print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_', * 10)
# Safely get a abbrevation by state that might not be there 

state = state.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value

city = cities.get('TX', 'Does Not Exits')
print(f"The city for the state 'TX' is: {city}")
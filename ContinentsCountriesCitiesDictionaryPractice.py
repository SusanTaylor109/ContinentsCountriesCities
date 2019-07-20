"""
Sue Taylor
April, 2019
Dictionary practice

"""
#Dictionary of continents, countries and cities

# Code

locations = {'North America': {'USA': ['Mountain View', "Atlanta"]},
             'Asia' : {'India':['Bangalore'], 'China': ['Shanghai']},
             'Africa' : {'Egypt': ['Cairo']}
            
            
            }
# TODO: Print a list of all cities in the USA in alphabetic order.

locations["North America"]['USA'].sort()
print(locations["North America"]['USA'])



# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
str_result = ""
result = []
for country in locations['Asia']:
    str_result = locations['Asia'][country][0] + "   " + country
    result.append(str_result)
result.sort()
for city in result:
    print(city)



#their solution
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai','Bajing']
locations['Africa'] = {'Egypt': ['Cairo']}

usa_sorted = sorted(locations['North America']['USA'])
print (1)
for city in usa_sorted:
    print (city)

asia_cities = []
print (2)
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)

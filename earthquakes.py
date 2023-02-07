'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude,
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''


import json

# PROBLEM 1
infile = open('eq_data.json', 'r')

earthquakes = json.load(infile)

print("----------------------------")
print("This is the solution for problem 1")
print("\n")
print("Number of Earthquakes:", len(earthquakes["features"]))

# I am thinking that the "type" is an indicator of how many earthquakes there are, so we would need to count that

print("Number of Earthquakes:", earthquakes["metadata"]["count"])
print("\n")
print("This is the end of problem 1")
print("----------------------------")
mag = ("The magnitude of the earthquake, this will be a function that drills down the dictionaries to finally find the magnitude")


# PROBLEM 2

eq_dict = {}

print("This is the solution for problem 2")
print("\n")
for i in earthquakes["features"]:
    if i["properties"]["mag"] > 6:
        # location = earthquake["metadata"]["features"]["properties"]
        location = i["properties"]["place"]
        magnitude = i["properties"]["mag"]
        longitude = i["geometry"]["coordinates"][0]
        latitude = i["geometry"]["coordinates"][1]
        print("Location:", location)
        print("Magnitude:", magnitude)
        print("Longitude:", longitude)
        print("Latitude:", latitude)
        print("\n\n")

eq_dict = {}
for i in earthquakes:
    case = {'key1': value, 'key2': value, 'key3': value}
    case_list.update(case)
'''
for i in eq_dict:
    print("Location:", location)
    print("Magnitude:", magnitude)
    print("Longitude:", longitude)
    print("Latitude:", latitude)
    print("\n\n")
'''

print(eq_dict)
print("This is the end of problem 2")
print("----------------------------")

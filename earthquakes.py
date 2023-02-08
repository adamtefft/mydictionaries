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


print("\n")
print("This is the end of problem 1")
print("----------------------------")


# PROBLEM 2


print("This is the solution for problem 2")
print("\n")

eq_dict = {}

for i in earthquakes["features"]:
    if i["properties"]["mag"] > 6:
        eq_list = []
        # eq_list.append([i["properties"]["place"]])
        eq_list.append([i["properties"]["mag"]])
        eq_list.append([i["geometry"]["coordinates"][0]])
        eq_list.append([i["geometry"]["coordinates"][1]])
        eq_dict[i["properties"]["place"]] = eq_list

print(eq_dict)

print("\n")
print("This is the end of problem 2")
print("----------------------------")
print("This is the soliution for problem 3")
print("\n")

# PROBLEM 3
# The * removes the brackets when it prints it out as a list
for i in eq_dict:
    print("Location:", *[i])
    print("Magnitude:", *eq_dict[i][0])
    print("Longitude:", *eq_dict[i][1])
    print("Latitude:", *eq_dict[i][2])
    print("\n")

print("This is the end of problem 3")
print("----------------------------")

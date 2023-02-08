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

# print("Number of Earthquakes:", earthquakes["metadata"]["count"])

print("\n")
print("This is the end of problem 1")
print("----------------------------")
mag = ("The magnitude of the earthquake, this will be a function that drills down the dictionaries to finally find the magnitude")


# PROBLEM 2


print("This is the solution for problem 2")
print("\n")

eq_list = []
eq_dict = {}

for i in earthquakes["features"]:
    if i["properties"]["mag"] > 6:
        # location = earthquake["metadata"]["features"]["properties"]
        # Why is this only printing out the last item in the loop?
        # It looks like it is deleting each item in the loop that has been added previously
        placelist = []
        placelist.append([i["properties"]["place"]])
        placelist.append([i["properties"]["mag"]])
        placelist.append([i["geometry"]["coordinates"][0]])
        placelist.append([i["geometry"]["coordinates"][1]])
        eq_dict[i["properties"]["place"]] = placelist

print(eq_dict)

print("\n")
print("This is the end of problem 2")
print("----------------------------")
print("This is the soliution for problem 3")
print("\n")

for i in eq_dict:
    print(*eq_dict[i][0])
    print(*eq_dict[i][1])
    print(*eq_dict[i][2])
    print(*eq_dict[i][3])


print("\n")
print("This is the end of problem 3")
print("----------------------------")


'''

This was my old code for step #2

for i in earthquakes["features"]:
    if i["properties"]["mag"] > 6:
        eq_dict = {}
        # location = earthquake["metadata"]["features"]["properties"]
        # Why is this only printing out the last item in the loop?
        # It looks like it is deleting each item in the loop that has been added previously
        eq_dict["Location"] = i["properties"]["place"]
        eq_dict["Magnitude"] = i["properties"]["mag"]
        eq_dict["Longitude"] = i["geometry"]["coordinates"][0]
        eq_dict["Latitude"] = i["geometry"]["coordinates"][1]
        print("Location:", eq_dict["Location"])
        print("Magnitude:", eq_dict['Magnitude'])
        print("Longitude", eq_dict["Longitude"])
        print("Latitude", eq_dict["Latitude"])
        print("\n")
'''

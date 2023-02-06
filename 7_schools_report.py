"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 80%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

schools = json.load(infile)
conference_schools = [372, 108, 107, 130]
# these numbers are based off of the list in the instructions, it identifies what conference the school is in

print(type(schools))

# How many schools are in this file?
print(len(schools))


'''
this is my work

for i in schools:
    graduation_rate = schools[i]["Graduation rate  women (DRVGR2020)"]
    if graduation_rate <= 80:
        print(f'{graduation_rate}')

for i in schools:
    total_price = schools[i][
        "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
    if total_price >= 50000:
        print(f'{total_price}')


'''
# this is what the answer was in class


for school in schools:
    if school['NCAA']["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Graduation rate  women (DRVGR2020)"] > 80:
            if school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
                # Why is this if statement not working?
                print("School:", school["instnm"])
                print("Graduation Rate for Women:",
                      school["Graduation rate  women (DRVGR2020)"])
                print("In State Tuition:",
                      school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
                print("\n")


'''
for school in schools:
    if school['NCAA']["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Graduation rate  women (DRVGR2020)"] > 80:
            print("School:", school["instnm"])
            print("Graduation Rate for Women:",
                  school["Graduation rate  women (DRVGR2020)"])
            print("\n")

for school in schools:
    if school['NCAA']["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            print("In State Tuition:",
                  school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
'''

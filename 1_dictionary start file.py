import random

phonebook = {}
phonebook = {'Chris': '555−1111',
             'Katie': '555−2222',
             'Joanne': '555−3333'}

mydictionary = dict(m=8, n=9)


print()
print('*****  start section 1 - print dictionary ********')
print()

print(mydictionary)

print(len(phonebook))

print()
print('*****  end section 1 ********')
print()


print()
print('*****  start section 2 - search dictionary ********')
print()


print(phonebook['Chris'])

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} does not exist in the phonebook")


print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print()


phonebook['Chris'] = "555-4444"

phonebook["Joe"] = "555-0123"

print(phonebook)

# this updated the value of the phone number for Chris
# joe did not exist, so Joe and his phone number were appended to the dictionary

print()
print('*****  end section 3 ********')
print()


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook["Chris"]
print(phonebook)

# this will delete Chris from the dictionary

print()
print('*****  end section 4 ********')
print()


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for i in phonebook:
    print(i)

for value in phonebook.values():
    print(value)

for k, v in phonebook.items():
    print(k)
    print(v)
    # print(f'The key is: {i} and the value is {phonebook[i]}")

for ph_tuple in phonebook.items():
    print(ph_tuple)


# this will print the keys
# printf"the key is: {key} and the value is {phonebook[key]}")
print()
print('*****  end section 5 ********')
print()


print()
print('*****  start section 6 - using get and clear ********')
print()


name = "Chris"

phone = phonebook.get(name, "key not found")

print(phone)

phonebook.clear()

print(phonebook)

print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop("Chris", "not found")

print(remove)
print(phonebook)


print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()


# supposed to pop it out of the dictionary and it is supposed to pick a key value pair
# it will pop out Joanne because she is the last item in the dictionary


a = phonebook.popitem()

print(a)

print(phonebook)


print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

# this means that the keys will be the output of this list
list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)
print(random_key)
# get the corresponding phone number
print(phonebook[random_key])

# this is how you would do all the code in one line
print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()

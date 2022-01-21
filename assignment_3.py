"""
   1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

    2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

    3) Use a list comprehension to check whether all persons are older than 20.

    4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

    5) Unpack the persons of the original list into different variables and output these variables.
"""

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
people = [
    {
        "name": "Manuel",
        "age": 35,
        "hobbies": ["Hockey", "Soccer"]
    },
    {
        "name": "Max",
        "age": 29,
        "hobbies": ["Tenis", "Soccer", "Guitar"]
    }
]

print("people:" + str(people))

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [person['name'] for person in people]
print("names:" + str(names))

# 3) Use a list comprehension to check whether all persons are older than 20.
print("all people older than 20: " + str(all([person['age'] > 20 for person in people])))

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

# copied_people = people[:] shallow copy doesnt work for complex object
copied_people = [person.copy() for person in people]

copied_people[0]['name'] = 'John'
print("copied people changed:" + str(copied_people))
print("original people unchanged:" + str(people))

# 5) Unpack the persons of the original list into different variables and output these variables.
p1, p2 = people

print("p1: " + str(p1))
print("p2: " + str(p2))

"""
    1) Create two variables – one with your name and one with your age

    2) Create a function which prints your data as one string

    3) Create a function which prints ANY data (two arguments) as one string

    4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
"""

name = input("Please type your full name:")
age = int(input("Please type your age:"))

def print_data():
    print("name: " + name + "\nage: " + str(age))


def print_concatenated_data(el1, el2):
    print("name: " + el1 + "\nage: " + str(el2))

def age_to_decades(age):
    return age // 10

print_data()
print_concatenated_data(name, age)

print("decades:" + str(age_to_decades(int(age))))

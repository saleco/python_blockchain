"""
    1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

    2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

    3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

    4) Adjust the logic to load the file content to work with pickled/ json data.
"""

#     1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
#     2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

import json
import pickle

# running = True
#
# while running:
#     print("Please choose:")
#     print("1: Add input")
#     print("2: OUtput data")
#     print("q:Quit")
#     choice = input("Select a choice:")
#     if choice == '1':
#         u_input = input("Your text: ")
#         with open('user_input.txt', mode='a') as f:
#             # user_inputs.append(u_input)
#             # f.write(json.dumps(user_inputs))
#             f.write(u_input)
#             f.write("\n")
#     if choice == '2':
#         with open('user_input.txt', mode='r') as f:
#             file_content = f.readlines()
#             for line in file_content:
#                 print(line)
#     elif choice == 'q':
#         running = False

#

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both
# with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.
running = True
user_inputs = []
while running:
    print("Please choose:")
    print("1: Add input")
    print("2: OUtput data")
    print("q:Quit")
    choice = input("Select a choice:")
    if choice == '1':
        u_input = input("Your text: ")
        user_inputs.append(u_input)
        with open('user_input.p', mode='wb') as f:
            # f.write(json.dumps(user_inputs))
            f.write(pickle.dumps(user_inputs))
    if choice == '2':
        with open('user_input.p', mode='rb') as f:
            # file_content = json.loads(f.read())
            file_content = pickle.loads(f.read())
            for line in file_content:
                print(line)
    elif choice == 'q':
        running = False
print("Exiting...")



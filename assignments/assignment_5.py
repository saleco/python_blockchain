"""
   1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

    2) Use the datetime library together with the random number to generate a random, unique value.
"""

# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random
import datetime

random_number_between_0_1 = random.random()
random_number_between_1_10 = random.randint(1, 10)

print(random_number_between_0_1)
print(random_number_between_1_10)

# 2) Use the datetime library together with the random number to generate a random, unique value.


random_with_datetime = random.randint(0, int(datetime.datetime.now().timestamp()))
print(random_with_datetime)
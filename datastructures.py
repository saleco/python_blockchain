simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
del (simple_list[0])
print(simple_list)

dictionary = {'name': 'Max'}
print(dictionary.items())
for k, v in dictionary.items():
    print(k, v)
del (dictionary['name'])
print(dictionary)

tuple = (1, 2, 3)
print(tuple.index(1))
# del(tuple[0]) tuples are imutable


set = {'Max', 'Ana', 'Max'}
print(set)
# del(set['Max']) use discard


#  all & any
new_list = [True, True, False]
print(any(new_list))  # should be True because at least one element is True
print(all(new_list))  # should be False because not all the elements are True

#  implement with list comprehension
number_list = [1, 2, 3, -5]
print(any([el > 0 for el in number_list]))  # should be False because at least one element is positive
print(all([el > 0 for el in number_list]))  # should be False because not all elements are positive

# collection map function
simple_list = [1, 2, 3, 4]
def multiply(el):
    return el * 2

print(list(map(multiply, simple_list)))

# map with lambda
print(list(map(lambda el: el * 2, simple_list)))

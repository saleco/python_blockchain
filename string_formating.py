# stupid way
name = 'Max'
age = 29
print('I am ' + name + ' and I am ' + str(age) + ' years old')

# same using format and {}
print('I am {} and I am {} years old.'.format(name, age))

# same using index args
print('I am {1} and I am {0} years old.'.format(age, name))

# same using index args multiple times
print('I am {1} and I am {0} years old. I really am named {1}'.format(age, name))

# same using args by name
print('I am {name} and I am {years} years old.'.format(name=name, years=age))

# formatting outputs
funds = 150.9723
print('Funds: {}'.format(funds))

# formatting outputs with ":" for float
funds = 150.9723
print('Funds: {:f}'.format(funds))

# formatting outputs with ":" for float with 1 decimal
funds = 150.9723
print('Funds: {:.1f}'.format(funds))

# formatting outputs with ":" for float with 1 decimal and 10 spaces between the value
funds = 150.9723
print('Funds: {:10.1f}'.format(funds))

# escaping characters
print('I\'m Max')

# formatting Strings with "f" in front of the string
print(f'I am {name} and I am {age} years old.')

# formatting Strings with "f" in front of the string + ":" for float with 2 decimals
print(f'I am {name} and I am {age:.2f} years old.')


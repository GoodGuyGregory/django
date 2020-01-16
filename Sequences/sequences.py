
# Basic For Loops:
groceries = ['roast beef', 'cucumbers', 'lettuce',
             'peanut butter', 'bread', 'dog food']

for item in groceries:
    print(item)


# Enumerate function used for identifying the index number for the items:

# Numbered version: this method isnt very pythonic, you could use the enumerate function instead
# index = 1
# for item in groceries:
#     print(f'{index}. {item}')
#     index += 1

# second argument in enumerate makes the list start at 1
for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')

course = ['Ashley', 'Introducing Dictionaries', 'Beginner']

print('List Version of the courses:')

print(course[0])

courseDictionary = {'teacher': 'Ashley',
                    'title': 'Introducing Disctionaries', 'level': 'Beginner'}

print('Dictionary Version of the course:')

print(courseDictionary['teacher'])

print(courseDictionary.keys())

print(courseDictionary.values())

# Sorts the list lexigraphically
print(sorted(courseDictionary.keys()))
print('=================================')
courseDictionary['teacher'] = 'Treasure'

print('Changes the value of Teacher in the Dictionary')
print(courseDictionary.values())

# Adds Stages to the Dictionary
courseDictionary['stages'] = 6
print(courseDictionary.keys())

# Deletes the Stages Key
del(courseDictionary['stages'])

print(courseDictionary.keys())

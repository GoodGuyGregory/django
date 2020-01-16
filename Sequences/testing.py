docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

# not in could also be used
if 'tuple' in docs:
    # do something:
    print('tuple is here!')
else:
    # do something else:
    print('tuple is not here')

print(docs.count('tuple'))

teachers = ['Sexton', 'Heterachi', 'Walsh', 'Doyle']

print(teachers.index('Doyle'))

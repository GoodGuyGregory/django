# Slices.py:
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# prints orange
print(rainbow[1])
# Guess what this prints
print(rainbow[3:7])

print(rainbow[0:])

# primary colors: skips every other element
print(rainbow[::2])
# reverse the rainbow
print(rainbow[::-1])


# Length Methods:
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(len(nums))
print(max(nums))
min(nums)
# Max and Min on strings look for the numbers closer to the end of the alphabet
animal = "ziggy the zebra"

print(max(animal))

# Concatenation of sequences
object1 = [1, 2, 3, 4]
object2 = [5, 6, 7, 8]
object1 = object1 + object2

print(object1)

# Multiplication: basically repetative concatenation

str = 'python'

print(str*5)

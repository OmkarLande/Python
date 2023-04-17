#...........Sets.........

sets={1,2,3,4,5}
print("This is a set \n",sets)

print("Adding 7 in given set")
sets.add(7)
print(sets)

print("Removing 7 in given set")
sets.remove(7)
print(sets)

print("Updaring given set")
updated_set={-1,0}
sets.update(updated_set)
print(sets)

print("length of given set")
print(len(sets))

print("min in given set")
print(min(sets))

print("max in given set")
print(max(sets))

print("sum of given set")
print(sum(sets))

#........Strings............

str1='Patu'
str2='String'

print("First string is \n",str1)
print("Second string is \n",str1)

print("Comparing 2 strings")
print(str1==str2)

print("Length of string 1")
print(len(str1))

print("Converting string 1 to Upperclass")
print(str1.upper())

print("Converting string 1 to Lowerclass")
print(str1.lower())

print("Index of a t in a string 1")
print(str1.index('t'))

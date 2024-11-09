# List or Array

names = ["a", "b", "c", "d", "e"]


# Accessing Elements    
print(names[0])  # Output: a
print(names[2])  # Output: c


# Changing Elements
names[1] = "new_element"
print(names)  # Output: ['a', 'new_element', 'c', 'd', 'e']


# Adding Elements
names.append("f")
print(names)  # Output: ['a', 'new_element', 'c', 'd', 'e', 'f']

names.insert(1, "inserted_element")
print(names)  # Output: ['a', 'inserted_element', 'new_element', 'c', 'd', 'e', 'f']


# Removing Elements
names.remove("new_element")
print(names)  # Output: ['a', 'inserted_element', 'c', 'd', 'e', 'f']

names.pop(1)
print(names)  # Output: ['a', 'c', 'd', 'e', 'f']


# Slicing
print(names[1:3])  # Output: ['c', 'd']
print(names[:3])  # Output: ['a', 'c', 'd']
print(names[3:])  # Output: ['e', 'f']


# Concatenation
names_two = ["g", "h", "i"]
combined_names = names + names_two
print(combined_names)  # Output: ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


# Sorting
combined_names.sort()
print("sorting",combined_names)  # Output: ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

combined_names.reverse()
print(combined_names)  # Output: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'a']


# Length
print(len(combined_names))  # Output: 8 


# Membership
print("a" in combined_names)  # Output: True
print("j" in combined_names)  # Output: False


# copy() function
copied_names = combined_names.copy()
print(copied_names)  # Output: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'a']

copied_names[0] = "new_element"
print(combined_names)  # Output: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'new_element']
print(copied_names)  # Output: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'new_element']

a =0.1
b=0.2
c=0.3
print(a+b == c)
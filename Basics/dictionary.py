#  dictionary
person = {
   "name": "John Doe",
   "age": 30,
   "city": "New York"
}   

# access

print(person["name"])
print(person["age"])
print(person.get("name"))

# update
person["age"] = 31
print(person["age"])

# single variable assignment
for i in person:
    print(i,person[i])

# find
if "city" in person:
    print("City is in the dictionary")
else:
    print("City is not in the dictionary")


# add
person["gender"] = "Male"
print(person)

# delete
del person["city"]
print(person)

# pop
person.pop("gender")
print(person)

# popitem # remove last item
person.popitem()
print(person)

# copy  #copy the person 
new_person = person.copy()
print(new_person)

# nested dictionary
nested_person = {
   "name": "John Doe",
   "age": 30,
   "address": {
      "street": "123 Main St",
      "city": "New York",
      "state": "NY"
   }
}

print(nested_person["address"]["city"])
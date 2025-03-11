#  List
# list is a collection of items that are ordered and mutable
# list is defined using square brackets
# list is a sequence of items
# list is a mutable sequence of items
# list is a heterogeneous sequence of items
# list is a dynamic sequence of items
# list is a flexible sequence of items
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.index("apple")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.copy()
print(fruits)

fruits.count("apple")
print(fruits)


fruits.insert(0, "apple")
print(fruits)

fruits.extend(["pineapple", "mango"])
print(fruits)

# Tuple
# tuple is a collection of items that are ordered and immutable
# tuple is defined using parentheses
# tuple is a sequence of items
# tuple is a heterogeneous sequence of items
# tuple is a dynamic sequence of items
# tuple is a flexible sequence of items

flowers = ("rose", "lily", "tulip", "daisy")
vegetables = ("carrot", "potato", "onion", "garlic")
colors = ("red","red", "green", "blue", "yellow")
tuples = flowers + vegetables
print(colors)
print(vegetables[1])
print("id od flowers is", id(flowers))
print("id of vegetables is", id(vegetables))
print("id of colors is", id(colors))
print(flowers == vegetables)
print(colors[2])
print(colors[1:3])
print(len(colors))
print(colors.count("red"))
print(colors.index("red"))

# Dictionary
# dictionary is a collection of items that are unordered and mutable
# dictionary is defined using curly braces
# dictionary is a sequence of items
# dictionary is a heterogeneous sequence of items
# dictionary is a dynamic sequence of items
# dictionary is a flexible sequence of items

data = {
    "name": "Rimsha",
    "age": 21,
    "city": "Karachi",
}
print(data)
print(data["name"])
print(data["age"])
print(data["city"])

data["age"] = 22
print(data)

data["city"] = "Lahore"
print(data)

del data ["city"]
print(data)

print(data.keys())
print(data.values())
print(data.items()) 
 

data.update({"city": "Islamabad"})
print(data)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key , ":", value)

# nested dictionary

person = {
    "name": "Rimsha",
    "age": 21,
    "city": "Karachi",
    "address": {
        "street": "123 Main St",
        "city": "Karachi",
    }
}

print(person)
print(person["address"]["street"])

person1 = person.copy()
print(person1)

person1["age"] = 22
print(person1)

person1["street"] = "456 Main St"
print(person1)


































thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Accessing Dictionary
x = thisdict["model"]
print(x)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

#Changing Items
thisdict["year"] = 2018
print(thisdict["year"])
thisdict.update({"year": 2020})
print(thisdict["year"])

#Adding an item
thisdict["color"] = "red"
print(thisdict)

#Looping
for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)

#Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])

#Removing an element
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
# del thisdict["year"]
# print(thisdict)
thisdict.clear()
print(thisdict)
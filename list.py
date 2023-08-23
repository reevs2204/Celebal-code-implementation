thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Accessing the list
print(thislist[-1])
print(thislist[2:5])
print(thislist[:3])
print(thislist[2:])
print(thislist[-4:-1])

#Change list items
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)

#Add list items
thislist.append("orange")
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Loop List
for i in range(len(thislist)):
  print(thislist[i])

#List comprehension
newlist = [x for x in thislist if x != "apple"]
print(newlist)
newlist = [x.upper() for x in thislist]
print(newlist)

#Sort List
thislis = [100, 50, 65, 82, 23]
thislis.sort()
print(thislis)
thislis.sort(reverse = True)
print(thislis)
thislist.sort(key = str.lower)
print(thislist)
thislis.reverse()
print(thislis)

#Copy
mylist = thislist.copy()
print(mylist)

#Remove list items
thislist.remove("watermelon")
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)




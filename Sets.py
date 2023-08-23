thisset = {"apple", "banana", "cherry"}
print(thisset)

#Accessing Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Add set items
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Loop in set
for x in thisset:
  print(x)

#Join Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
a= x.symmetric_difference(y)
print(a)

#Removing the items from set
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)
del thisset
print(thisset)
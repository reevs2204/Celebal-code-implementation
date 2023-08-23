thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Accessing Tuple
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:2])
print(thistuple[:1])
print(thistuple[2:])
print(thistuple[-2:-1])

#Updating Tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
z = list(thistuple)
z.append("orange")
thistuple = tuple(z)
a = ("orange",)
thistuple += a
print(thistuple)

#Unpack Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Loop Tuple
for x in thistuple:
  print(x)
i=0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
mytuple = fruits * 2
print(mytuple)

#Removing Items
y = list(thistuple)
y.remove("apple")
print(y)
thistuple = tuple(y)
del thistuple
print(thistuple)
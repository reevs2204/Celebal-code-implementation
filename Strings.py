a='Hello'
print("Hello")
print('Hello')
print(a)
a = "Hello, World!"
print(a[1])

#String Slicing
b = "Hello, World!"
print(b[2:5])
#Slice from start
b = "Hello, World!"
print(b[:5])
#Slice to the end
b = "Hello, World!"
print(b[2:])

#String modification
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(","))

#Concatenate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format Strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape character
txt = 'It\'s alright.'
print(txt) 
txt1 = "This will insert one \\ (backslash)."
print(txt1)
txt3 = "Hello\nWorld!"
print(txt3)  
txt4 = "Hello\rWorld!"
print(txt4)
txt5 = "Hello\tWorld!"
print(txt5) 
txt6 = "Hello \bWorld!"
print(txt6) 
txt7 = "\110\145\154\154\157"
print(txt7) 
txt8 = "\x48\x65\x6c\x6c\x6f"
print(txt8) 





#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

 
lis = [1, 2, 3, 4]
print(tuple(lis))
print(list(lis))
print(set(lis))

list_1 = [("Nakul", 93), ("Shivansh", 45), ("Samved", 65),
          ("Yash", 88), ("Vidit", 70), ("Pradeep", 52)]
dict_1 = dict()
 
for student, score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)



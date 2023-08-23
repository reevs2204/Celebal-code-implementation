#Lambda function
str1 = 'HowAreYou?' 
upper = lambda string: string.upper()
print(upper(str1))

def cube(y):
    return y*y*y 
lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

ages = [13, 90, 17, 59, 21, 60, 5] 
adults = list(filter(lambda age: age > 18, ages)) 
print(adults)

#Function
def my_function():
  print("Hello from a function")
my_function()

def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
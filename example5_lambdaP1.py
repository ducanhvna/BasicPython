# Syntax 
# lambda arguments : expresstion
# example 1: A lambda funciton that adds 10 to the number pass in as an argument, and print the result
x = lambda a : a + 10
print (x (5))

# Output : 15

# Example 2 : A lambda funciton that multiples argument a with argument b and print the result
x = lambda a, b: a * b
print (x(5, 25))

# Expected output: 125

# Example 3: A lambda funciton that sums argument a, b and c and print result
x = lambda a, b, c: a + b + c
print (x(1, 2, 3))
# expected output: 6

# Why use lambda functoins?
# The power of labmda is better shown when use them as an anomyouts function inside another function
# Say you have an function definition that thake one argument and that argument will be multiplied with an unknow number
# def myfunc(n):
#     return lambda a: a * n

# Example 5: Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a: a * n

x = myfunc(10)
print(x (25))

# Output:  250

# example 5: Use the same function definition to make a function that always triples the number you send in
def myfunc(n):
    return lambda a: a * n
x = myfunc(3)
print(x(23))

# Output 69

# example 6: Use the same function definitiono to make both functions, in the same program:
def myfunc(n):
    return lambda a: a* n

my_double = myfunc(2)
my_triple = myfunc(3)

print (my_double (2))
print (my_triple(2))

print (my_double(3) + my_triple (3))

# Output:
# 4
# 6
# 15
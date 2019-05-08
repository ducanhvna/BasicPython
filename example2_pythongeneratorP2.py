# Example1 is of less use and we studied it just to get an idea of what was happening in the back ground.
# NOrmally, generator funcitons are implemented with a loop having a suitable terminating condition
# Let's take an example of a generator that reverses a string
def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]

# For loop to reverse the string 
# Output:
# o
# l
# e
# h
for char in rev_str("hello"):
    print (char)
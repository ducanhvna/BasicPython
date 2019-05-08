# Its is fairly simple to create a generator in python. Its is as easy as defining a normal functin with yield satment instead of a return statement
# if a function contains at least one yeield satement (it may contain other yielkd or return statements), ist becoms a generator function. Bothe yeield and return will return some value from a funtion
# the difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls
## Generator function contains one or more yield satement
## when called 
# Asimple genrator function
def my_gen():
    n=1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is print the third ')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# One interesting thing to note in the above example is that, the value of varialbe n is remembered between each call
# Unlike normal funtions, the local varialbes are not destroyed when the function yeilds. Furthermore, the genreator object can be iterated only once
# To restart the process we need to created another gerator object using somting like a = my_gen()

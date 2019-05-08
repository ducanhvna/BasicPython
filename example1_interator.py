# define a list
my_list = [0, 4, 7, 3, 6]

# get an interator using iter()
my_iter = iter(my_list)

## interate throuhg it using next()
# print 0 
print(next(my_iter))

# print 4
print(next(my_iter))

## next(obj) is same as obj.__next__()
# print 7
print(my_iter.__next__())

print(my_iter.__next__())

print(my_iter.__next__())

## This will raise error, notiems left
print(my_iter.__next__())


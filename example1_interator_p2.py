my_list = [0, 1, 2, 3, 9]

# create a interator object from interable
my_object = iter(my_list)
while True:
    try:
        print(next(my_object))
    except StopIteration:
        print('Stop interation')
        break
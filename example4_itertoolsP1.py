# Dùng itertools
# Làm phẳng list
import itertools
a = [[1,2], [3, 4], [5, 6]]

result = list(itertools.chain.from_iterable(a))

# Output: 
# [1, 2, 3, 4, 5, 6]

# dùng sum

result2 = sum(a,[])

# dùng list comprehension
[x for l in a for x in l]

# nâng cao: list các phần tử bất kì
a = [1,2, [3,4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]


# Sử dụng comprehension
# Biểu thức generator
g = (x ** 2 for x in range(10))
next(g)
for i in g :
    print(i)
sum ( x ** 3 for x in range (10))

sum (x ** 3 for x in range(10) if x % 3 ==1)


# Dic comprehension
m = {x: x ** 2 for x in range(5)}

# Dict comprehension
m = {x: 'A' + str(x) for x in range(10)}

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Chuyển đổi dic dùng comprehension
{v: k for k, v in m.items()}

# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# Tập hợp và các phép toán liên quan
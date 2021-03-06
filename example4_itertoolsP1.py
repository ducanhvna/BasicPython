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
# Tập hợp và các phép toán liên 

# Nhóm các phần tử liền nhau
group_adjacent = lambda a, k: list(zip(*([iter(a)]*k)))
# >>> group_adjacent(a, 3)
# [(1, 2, 3), (4, 5, 6)]
# >>> group_adjacent(a, 2)
# [(1, 2), (3, 4), (5, 6)]
# >>> group_adjacent(a, 1)
# [(1,), (2,), (3,), (4,), (5,), (6,)]
# >>> a = [1,2, 3, 4, 5, 6, 9]
# >>> group_adjacent(a, 1)
# [(1,), (2,), (3,), (4,), (5,), (6,), (9,)]
# >>> group_adjacent(a, 2)
# [(1, 2), (3, 4), (5, 6)]
# >>> group_adjacent(a, 3)
# [(1, 2, 3), (4, 5, 6)]
# >>>
from itertools import islice
group_adjacent = lambda a,k: list(zip(*(islice(a, i, None, k ) for i in range(k))))
# >>> group_adjacent = lambda a,k: list(zip(*(islice(a, i, None, k ) for i in range(k))))
# >>> group_adjacent(a, 3)
# [(1, 2, 3), (4, 5, 6)]
# >>> group_adjacent(a,2)
# [(1, 2), (3, 4), (5, 6)]
# >>> group_adjacent(a,1)
# [(1,), (2,), (3,), (4,), (5,), (6,), (9,)]
# Sinh uniqe id cho từng giá trị
import collections
import itertools
value_to_numeric_map = collections.defaultdict(itertools.count().__next__)

# Những phần tử lớn nhất và nhỏ nhất trong 1 list
import heapq
import random
a = [random.randint(0, 100) for __ in range(100)]
heapq.nsmallest(5,a)
heapq.nlargest(5,a)

# Ứng dụng của itertools
# Tích Descartes
import itertools
for p in itertools.product('223', '54'):
    print(''.join(p))

for p in itertools.product('12', repeat = 4):
    print(''.join(p))

# Ghép các iterable
import itertools
a = [1, 2, 4, 3]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a,3)):
    print(p)

for subset in itertools.chain.from_iterable(itertools.combinations(a,n) for n in range(len(a) + 1)):
    print(subset)

# Nhóm các phần tử theo một tiêu chí

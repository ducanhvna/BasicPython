# Nhóm các phần tử theo một tiêu chí
import itertools
for k,g in itertools.groupby('12223333444555555'):
    print(k, ''.join(g))

# Trong trinh thông dịch, _ sẽ lưu giá trị phép tính cuối cùng

# Đảo ngược list
list(reversed([1, 2, 3, 4]))
[1, 2, 3, 4][::-1]
tuple(reversed((1,2,3,4)))
# >>> list(reversed([1, 2, 3, 4]))
# [4, 3, 2, 1]
# >>> [1, 2, 3, 4][::-1]
# [4, 3, 2, 1]
# >>> tuple(reversed((1,2,3,4)))
# (4, 3, 2, 1)

# Chuyển iterable thành String
x = ['Hello', 'world', '!']
' '.join(x)
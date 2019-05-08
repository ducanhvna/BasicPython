# Easy to emplement
# Generators can be implemented in a clear and concise way as compared to ther iterator class counterpart. Follwoing is an example to implememnt a sequence of power of 2's using iterator class
class PowTwo:
    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.n  = 0 
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2** self.n
        self.n += 1
        return result

def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

def all_even():
    n = 0
    while True:
        yield n
        n += 2
        
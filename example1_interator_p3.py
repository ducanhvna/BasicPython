# Buiding your own terator in python

# Buiding an interator from scratch by create two method __inter__ and __next__()
# The __inter() method returns the interator object itself. If required, some initialization can be performed
class PowTwo:
    """ class to implement an iterator
    of powers of two """

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo (4)




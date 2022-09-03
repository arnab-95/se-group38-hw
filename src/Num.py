import math


class Num:

    # Initialize new Sym class object
    def __init__(self, n=0, at=0, name="", has=None, lo=float('inf'), hi=-float('inf'), issorted=True):
        if has is None:
            has = {}
        self.n = n
        self.at = at
        self.name = name
        self.has = has
        self.lo = lo,
        self.hi = hi,
        self.isSorted = issorted,

    # Add num of column to class object
    def add(self, v):
        pass

    # Returns mode of column
    def mid(self):
        pass

    # Returns entropy of column
    def div(self, ):
        pass

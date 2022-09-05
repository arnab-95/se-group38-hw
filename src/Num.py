from random import random, randint
from src import utils

class Num:

    # Initialize new Num class object
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self.has = []
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isSorted = True
        self.w = -1 if "-$" in self.name else 1

    # Return kept numbers, sorted.
    def nums(self):
        if not self.isSorted:            
            self.has.sort()
            self.isSorted = True
        
        return self.has
    
    # Reservoir sampler. Keep at most ‘the.nums‘ numbers
    # (and if we run out of room, delete something old, at random)., 
    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)            

            pos = None

            if len(self.has) < utils.the["nums"]:
                pos = 1 + len(self.has)
            elif random() < utils.the["nums"] / self.n:
                pos = randint(1, len(self.has))
            
            if pos:
                self.isSorted = False
                if len(self.has) == pos + 1:
                    self.has.append(v)
                else:
                    self.has[pos - 1] = v

    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self):
        a = self.nums()
        return (utils.per(a, 0.9) - utils.per(a, 0.1)) / 2.58

    # Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return utils.per(self.nums(), 0.5)

from random import random

class Num:

    # Initialize new Num class object
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self.has = {}
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isSorted = True
        self.w = -1 if "-$" in name else 1


    # Return kept numbers, sorted.
    def nums(self):
        if not self.isSorted:
            table.sort(self.has) # TODO
            self.isSorted = True
        
        return self.has
    
    # Reservoir sampler. Keep at most ‘the.nums‘ numbers
    # (and if we run out of room, delete something old, at random)., 
    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)

            if self.has < the.nums:
                pos = 1 + self.has
            elif random() < the.nums / self.n:
                pos = random(self.has)
            
            if pos:
                self.isSorted = False
                self.has[pos] = tonumber(v) # TODO

    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58 # TODO

    # Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(), 0.5) # TODO
    

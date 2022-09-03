import math


class Sym:

    # Initialize new Sym class object
    def __init__(self, n=0, at=0, name="", has=None):
        if has is None:
            has = {}
        self.n = n
        self.at = at
        self.name = name
        self.has = has

    # Add symbol of column to class object
    def add(self, v):
        if v != '?':
            self.n += 1
            if v in self.has:
                self.has[v] += 1
            else:
                self.has[v] = 1

    # Returns mode of column
    def mid(self):
        mode = 0
        most = -1
        for key in self.has:
            if self.has[key] > most:
                mode = key
                most = self.has[key]
        return mode

    # Returns entropy of column
    def div(self, ):
        e = 0
        for key in self.has:
            if self.has[key] > 0:
                e = e - self.fun(self.has[key] / self.n)
        return e

    # Function to help in entropy calculation
    def fun(self, p):
        return p * math.log(p, 2)

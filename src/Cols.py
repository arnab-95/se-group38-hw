import math


class Cols:

    # Initialize new Sym class object
    def __init__(self, n=0, at=0, name="", has=None):
        if has is None:
            has = {}
        self.n = n
        self.at = at
        self.name = name
        self.has = has

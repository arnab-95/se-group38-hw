class Row:
    def __init__(self,t):
        self.t =t
        self.cooked = copy(t)
        self.cells = t
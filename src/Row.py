from . import utils

class Row:
## `Row` holds one record

    def __init__(self, t):
    # Initialize new Row class object
        self.cells = t
        self.cooked = utils.copy(t)
        self.isEvaled = False
        return self

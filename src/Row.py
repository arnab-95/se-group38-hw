from . import utils
from utils import copy

class Row:
## `Row` holds one record

    def __init__(self, t):
    # Initialize new Row class object
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False
        return self

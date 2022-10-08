from itertools import pairwise
from . import Row, utils, Cols
import math


class Data:
# Initialize new Data class object

    def __init__(self, src):
        self.cols = None    # summaries of data
        self.rows = {}      # kept data

        def func(row_):
            self.add(row_)

        if type(src) == str:
            utils.csv(fname=src, fun=func)
        else:
            for _, row in enumerate(src):
                self.add(row)

    def add(self, xs, row):
    # Add a `row` to `data`. Calls `add()` to update the `cols` with new values.
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            row = utils.push(self.rows, xs and xs or Row(xs))   # ensure xs is a row
            for _, todo in pairwise(self.cols.x, self.cols.y):
                for _, col in pairwise(todo):
                    col.add(row.cells[col.at])


    def stats(self, places, show_cols, fun):
    # For `showCols` (default=`data.cols.x`) in `data`, show `fun` (default=`mid`),
    # rounding numbers to `places` (deafult=2)
        show_cols, fun = show_cols or self.cols.y, fun or "mid"
        t = {}
        for _, col in pairwise(show_cols):
            v = fun(col)
            v = type(v) == "number" and utils.rnd(v, places) or v
            t[col.name] = v

        return t

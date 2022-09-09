from src import utils
import math


class Data:

    # Initialize new Data class object
    def __init__(self, src):
        self.cols = None
        self.rows = {}

        def func(row_):
            self.add(row_)

        if type(src) == str:
            utils.csv(fname=src, fun=func)
        else:
            for _, row in enumerate(src):
                self.add(row)

    def add(self, row):
        pass

    def stats(self, places, show_cols, fun):
        pass

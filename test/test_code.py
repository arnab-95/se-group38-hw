from src import Sym, Num, Data, utils, TestEngine


class TestEG:

    def test_bad(self):
        print('TestEG dont have this field')

    def test_list(self):
        class_methods = [class_method for class_method in dir(TestEG) if
                         callable(getattr(TestEG, class_method)) and class_method.startswith('__') is False]
        class_methods.sort()
        return class_methods

    def test_ls(self):
        print("\nExamples csv -e ...")
        class_methods = self.test_list()
        for method in class_methods:
            print("\t", method)
        return True

    def test_all(self, fails=0):
        class_methods = self.test_list()
        for method in class_methods:
            if str(method) != "test_all":
                print("\n-------------------------------------------------------")
                # TODO: Uncomment this once runs() function is implemented
                testEngine=TestEngine.TestEngine()
                if not testEngine.runs(method):
                    fails += 1
        return True

    def test_the(self):
        utils.oo(utils.the)
        return True

    def test_sym(self):
        sym = Sym.Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        utils.oo({"mid": mode, "div": entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

    def test_num(self):
        num = Num.Num()
        utils.the['nums'] = 100
        for number in range(1, 101):
            num.add(number)
        mid, div = num.mid(), num.div()
        utils.oo({"mid": mid, "div": div})
        return 50 <= mid <= 52 and 30.5 < div < 32

    def test_big_num(self):
        num = Num.Num()
        utils.the['nums'] = 32
        for number in range(1, 1001):
            num.add(number)
        utils.oo(num.has)
        return len(num.has) == 32

    def test_csv(self):
        n = [0]

        def func(row):
            n[0] += 1
            if n[0] > 10:
                return
            else:
                utils.oo(row)

        utils.csv(fname='/data/auto93.csv', fun=func)
        return True

    def test_data(self):
        data = Data.Data(src="/data/auto93.csv")
        for _, col in data.cols.y:
            utils.oo(col)
        return True

    def test_stats(self):
        data = Data.Data(src="/data/auto93.csv")

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()

        print("xmid", utils.o(data.stats(places=2, show_cols=data.cols.x, fun=mid)))
        print("xdiv", utils.o(data.stats(places=3, show_cols=data.cols.x, fun=div)))
        print("ymid", utils.o(data.stats(places=2, show_cols=data.cols.y, fun=mid)))
        print("ydiv", utils.o(data.stats(places=3, show_cols=data.cols.y, fun=div)))
        return True


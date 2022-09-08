from src import Sym, Num, Data, utils


def test_the():
    utils.oo(utils.the)
    return True


def test_sym():
    sym = Sym.Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    utils.oo({"mid": mode, "div": entropy})
    # return mode == "a" and 1.37 <= entropy <= 1.38
    assert mode == "a" and 1.37 <= entropy <= 1.38


def test_num():
    num = Num.Num()
    utils.the['nums'] = 100
    for number in range(1, 101):
        num.add(number)
    mid, div = num.mid(), num.div()
    utils.oo({"mid": mid, "div": div})
    # return 50 <= mid <= 52 and 30.5 < div < 32
    assert 50 <= mid <= 52 and 30.5 < div < 32


def test_big_num():
    num = Num.Num()
    utils.the['nums'] = 32
    for number in range(1, 1001):
        num.add(number)
    utils.oo({"nums": num.has})
    # return len(num.has) == 32
    assert len(num.has) == 32


def test_csv():
    n = [0]

    def func(row):
        n[0] += 1
        if n[0] > 10:
            return
        else:
            utils.oo(row)

    utils.csv(fname='../data/auto93.csv', fun=func)
    return True


def test_data():
    data = Data.Data(src="../data/auto93.csv")
    for _, col in data.cols.y:
        utils.oo(col)
    return True


def test_stats():
    data = Data.Data(src="../data/auto93.csv")

    def div(col):
        return col.div()

    def mid(col):
        return col.mid()

    print("xmid", utils.o(data.stats(places=2, show_cols=data.cols.x, fun=mid)))
    print("xdiv", utils.o(data.stats(places=3, show_cols=data.cols.x, fun=div)))
    print("ymid", utils.o(data.stats(places=2, show_cols=data.cols.y, fun=mid)))
    print("ydiv", utils.o(data.stats(places=3, show_cols=data.cols.y, fun=div)))
    return True

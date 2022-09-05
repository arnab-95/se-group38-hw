from src import Sym, Num, utils
import logging

log = logging.getLogger()


def test_the():
    log.info("the: %s", utils.the)


def test_sym():
    sym = Sym.Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    log.info("{mid=%s, div=%s}", mode, entropy)
    assert mode == "a" and 1.37 <= entropy <= 1.38


# def test_num():
#     num = Num.Num()
#     for number in range(1, 101):
#         num.add(number)
#     mid, div = num.mid(), num.div()
#     log.info("{mid=%s, div=%s}", mid, div)
#     assert 50 <= mid <= 52 and 30.5 < div < 32
#
#
# def test_big_num():
#     num = Num.Num()
#     utils.the.nums = 32
#     for number in range(1, 1001):
#         num.add(number)
#     log.info("nums:%s", num.has.keys())
#     assert len(num.has) == 32

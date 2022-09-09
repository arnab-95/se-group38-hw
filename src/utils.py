import math
import sys

# TODO: Shift to a better place. Also, some properties need to be set at the start of the code.
the = {}
_ENV = {}
b4 = {}


def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1

    # TODO: Improve this
    try:
        return int(s)
    except:
        pass

    # TODO: Improve this
    try:
        return float(s)
    except:
        pass

    # TODO: Match function is missing
    return fun(s)


def cli(t):
    new_t = {}
    for slot, v in t.items():
        v = str(v)
        for n,x in enumerate(sys.argv):
            if x == "-" + slot[0] or x == "--" + slot:
                v = (v == "false" and "true") or (v == "true" and "false") or sys.argv[n+1]
        new_t[slot] = coerce(v)

    if "help" in new_t.keys():
        # TODO: os.exit() pending
        print("\nhelp\n")

    return new_t


def copy(t):
    if type(t) == list:
        new_t = []
        for v in t:
            new_t.append(copy(v))

    if type(t) == dict:
        new_t = {}
        for k in t.keys():
            new_t[k] = copy(t[k])
        return new_t

    # TODO: Check metadata in lua
    return t


def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]


def push(t, x):
    if type(t) == list:
        t.append(x)
    elif type(t) == dict:
        t[1 + len(t)] = x
    return x


def csv(fname, fun):
    with open(fname) as f:
        lines = f.read().split("\n")
        for i in range(len(lines)):
            if i == 0 or lines[i] == "":
                continue
            line = lines[i].split(the.separator)

            t = {}
            for v in line:
                t[1 + len(t)] = coerce(v)

            fun(t)


def o(t):
    if type(t) != dict and type(t) != list:
        return str(t)

    def show(k, v):
        if str(k[0]) != "_":
            v = o(v)
            if len(t) == 0:
                return str(k) + str(v)
            else:
                return str(v)

    itr = None
    if type(t)==list:
        itr = enumerate(t)
    else:
        itr = t.items()

    u = {}
    for k, v in itr:
        print(len(u))
        u[len(u)] = show(k, v)
    
    # TODO: Ask professor why this is needed
    # if len(t) == 0:
    #     u = sorted(u)

    print(u)
    
    # this is for line 88
    temp = ""  # created string to add values of dict and print them
    for key, value in u.items():
        temp = temp + " a" + u[key]
    return "{" + temp + "}"


def oo(t):
    print(o(t))
    return t


def rogues():
    for k, v in _ENV.items():
        if k not in b4.keys():
            print("?", k, type(v))


def rnd(x, places=2):
    mult = 10 ** places
    return math.floor(x * mult + 0.5) / mult

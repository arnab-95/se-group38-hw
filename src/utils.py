import math

the = {}

def o(t):
    if type(t) != dict:
        return str(t)
    def show(k,v):
        if str(k[0]) != "_":
            v = o(v)
            if len(t) == 0:
                return (str(k)+str(v))
            else:
                return str(v)
    u = {}
    for k,v in t.items():
        print(len(u))
        u[len(u)] = show(k,v)
    if len(t) == 0:
        u = sorted(u)
    print(u)
    # this is for line 88
    temp = "" 		#created string to add values of dict and print them
    for key,value in u.items():
        temp = temp +" a"+ u[key]
    return ("{"+temp+"}")


def oo(t):
    print(o(t))
    return t


def rnd(x,places):
    mult = 1
    if places == "False":
        mult = 10**2
    else:
        mult = 10**places
    return (math.floor(x * mult +0.5)/mult)

# TODO: Fix the code
def coerce(s):
    pass
    # if s == 'true':
    #     return True
    # if s == 'false':
    #     return False
    # if type(s) == str:
    #     if s.isdigit() == True:
    #         s = int(s)
    # return s or int(s) or s

def per(t,p):
    p = math.floor((( p or .5)*len(t))+.5)
    return t[max(1,min(len(t),p))]


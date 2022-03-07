
def index1(k, arinst):
    p = 0
    while (p < len(arinst)):
        if arinst[p]==k:
            return p;
        p = p + 1
    return -1


def add(r2, r3):
    return (r2 + r3)


def sub(r2, r3):
    return (r2 - r3)


def bne(r1, r2, label,inst1,p):
    if r1 != r2:
        return index1(label,inst1)
    return p

def beq(r1, r2, label,inst1,p):
    if r1 == r2:
        return index1(label,inst1)
    else:
        return p

def blt(r1,r2,label,inst,p):
    if(r2>r1):
        return index1(label,inst)
    else:
        return p


def add(r2, r3):
    return r2 + r3


def sub(r2, r3):
    return r2 - r3


def bne(r1, r2, label):
    if r1 != r2:
        label


def jal(label):
    label


def lw(n, r2):
    return n + r2


def mov(r2):
    return r2


def li(r1, n):
    return n


zero = 0
ra = 0
sp = 0
gp = 0
tp = 0
t0 = 0
t1 = 0
t2 = 0
s0 = 0
s1 = 0
a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0

instr = ["add", "li"]
data = ["t1", "t2", "t3", "t4", 6]
num = [5, 2]

dat = []
sz = len(instr)
siz = len(data)
for i in range(siz):
    dat.append(0)
j = 0
k = 0
for i in range(sz):

    if instr[i] == "add":
        dat[j+1] = num[k]
        dat[j+2] = num[k+1]
        dat[j] = add(dat[j+1], dat[j+2])
        j = j+3
        k = k+2
    elif instr[i] == "sub":
        dat[j+1] = num[k]
        dat[j+2] = num[k+1]
        dat[j] = sub(dat[j+1], dat[j+2])
        j = j+3
        k = k+2
    elif instr[i] == "mov":
        dat[j+1] = num[k]
        dat[j] = mov(dat[j+1])
        j = j+2
        k = k+1
    elif instr[i] == "lw":
        dat[j+1] = num[k]
        dat[j+2] = num[k+1]
        dat[j] = lw(dat[j+1], dat[j+2])
        j = j+3
        k = k+2
    elif instr[i] == "li":
        dat[j+1] = data[j+1]
        dat[j] = li(dat[j], dat[j+1])
        j = j+2


for i in range(siz):
    if data[i] == "ra":
        ra = dat[i]
    elif data[i] == "sp":
        sp = dat[i]
    elif data[i] == "gp":
        gp = dat[i]
    elif data[i] == "tp":
        tp = dat[i]
    elif data[i] == "t0":
        t0 = dat[i]
    elif data[i] == "t1":
        t1 = dat[i]
    elif data[i] == "t2":
        t2 = dat[i]
    elif data[i] == "s0":
        s0 = dat[i]
    elif data[i] == "s1":
        s1 = dat[i]
    elif data[i] == "a0":
        a0 = dat[i]
    elif data[i] == "a1":
        a1 = dat[i]
    elif data[i] == "a2":
        a2 = dat[i]
    elif data[i] == "a3":
        a3 = dat[i]
    elif data[i] == "a4":
        a4 = dat[i]
    elif data[i] == "a5":
        a5 = dat[i]
    elif data[i] == "a6":
        a6 = dat[i]
    elif data[i] == "a7":
        a7 = dat[i]
    elif data[i] == "s2":
        s2 = dat[i]
    elif data[i] == "s3":
        s3 = dat[i]
    elif data[i] == "s4":
        s4 = dat[i]
    elif data[i] == "s5":
        s5 = dat[i]
    elif data[i] == "s6":
        s6 = dat[i]
    elif data[i] == "s7":
        s7 = dat[i]
    elif data[i] == "s8":
        s8 = dat[i]
    elif data[i] == "s9":
        s9 = dat[i]
    elif data[i] == "s10":
        s10 = dat[i]
    elif data[i] == "s11":
        s11 = dat[i]
    elif data[i] == "t3":
        t3 = dat[i]
    elif data[i] == "t4":
        t4 = dat[i]
    elif data[i] == "t5":
        t5 = dat[i]
    elif data[i] == "t6":
        t6 = dat[i]

print("zero = ", zero)
print("ra = ", ra)
print("sp = ", sp)
print("gp = ", gp)
print("tp = ", tp)
print("t0 = ", t0)
print("t1 = ", t1)
print("t2 = ", t2)
print("s0 = ", s0)
print("s1 = ", s1)
print("a0 = ", a0)
print("a1 = ", a1)
print("a2 = ", a2)
print("a3 = ", a3)
print("a4 = ", a4)
print("a5 = ", a5)
print("a6 = ", a6)
print("a7 = ", a7)
print("s2 = ", s2)
print("s3 = ", s3)
print("s4 = ", s4)
print("s5 = ", s5)
print("s6 = ", s6)
print("s7 = ", s7)
print("s8 = ", s8)
print("s9 = ", s9)
print("s10 = ", s10)
print("s11 = ", s11)
print("t3 = ", t3)
print("t4 = ", t4)
print("t5 = ", t5)
print("t6 = ", t6)

#file
File_object = open(r"new.S","r")
#variable
arrinst = '.word'
arrinst1 = ','
inst1 = '__start:'
inst2 = 'li'
inst3 = 'add'
inst4 = 'sub'
inst5 = 'j'
inst6 = 'lw'
inst7 = 'sw'
inst8 = 'addi'
inst9 = 'move'
inst10 = 'blt'
inst11 = 'beq'
che = '$'
che1 = '('
flag = [0,0,0,0,0,0,0,0,0,0,0,0]
arrflag = [0]
index = 0
inst = []
rawdata = []
data = []
arr = []
#taking input ( file )
for line in File_object:
    index += 1
    if flag[0]==1:
        for word in line.split():
            if flag[1]==1:
                rawdata.append(word)
                flag[1]=0
            elif flag[2]==1:
                rawdata.append(word)
                flag[2]=0
            elif flag[3]==1:
                rawdata.append(word)
                flag[3]=0
            elif flag[4] == 1:
                rawdata.append(word)
                flag[4] = 0
            elif flag[5] == 1:
                rawdata.append(word)
                flag[5] = 0
            elif flag[6] == 1:
                rawdata.append(word)
                flag[6] = 0
            elif flag[7] == 1:
                rawdata.append(word)
                flag[7] = 0
            elif flag[8] == 1:
                rawdata.append(word)
                flag[8] = 0
            elif flag[9] == 1:
                rawdata.append(word)
                flag[9] = 0
            elif flag[10] == 1:
                rawdata.append(word)
                flag[10] = 0
            elif flag[11] == 1:
                rawdata.append(word)
                flag[11] = 0
            elif word==inst2:
                inst.append(inst2)
                flag[1] = 1
            elif word==inst3:
                inst.append(inst3)
                flag[2] = 1
            elif word==inst4:
                inst.append(inst4)
                flag[3] = 1
            elif word==inst5:
                inst.append(inst5)
                flag[4] = 1
            elif word == inst6:
                inst.append(inst6)
                flag[5] = 1
            elif word == inst7:
                inst.append(inst7)
                flag[6] = 1
            elif word == inst8:
                inst.append(inst8)
                flag[7] = 1
            elif word == inst9:
                inst.append(inst9)
                flag[8] = 1
            elif word == inst10:
                inst.append(inst10)
                flag[9] = 1
            elif word == inst11:
                inst.append(inst11)
                flag[10] = 1
            else:
                inst.append(word)
                size = len(inst[len(inst)-1])
                inst[len(inst)-1] = inst[len(inst)-1][:size-1]
    if inst1 in line:
        n = index
        if index!=1:
            flag[0]=1
    if arrinst in line:
        for word in line.split():
            if arrinst==word:
                w1 = word
            elif arrinst1==word:
                w2 = word
            else:
                arr.append(word)
for_i = 0
while (for_i<len(rawdata)):
    gap = [-1]
    j = 0
    while(j<len(rawdata[for_i])):
        if arrinst1==rawdata[for_i][j]:
            gap.append(j)
        j = j + 1
    gap.append(len(rawdata[for_i]))
    k = 0
    while(k<len(gap)-1):
        p = rawdata[for_i][(gap[k])+1:gap[k+1]]
        if p[0]==che:
            p = p[1:len(p)]
        if len(p)>2:
            if p[1]==che1:
                p = p[3:len(p)-1]
        data.append(p)
        k = k+1
    for_i = for_i + 1







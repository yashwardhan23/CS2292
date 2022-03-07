import func


File_object = open(r"new.S","r")
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
checkpointj = {}
data = []
arr = []
check_index = 0;
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
                check_index = check_index +2
                flag[1] = 1
            elif word==inst3:
                inst.append(inst3)
                check_index = check_index + 3
                flag[2] = 1
            elif word==inst4:
                inst.append(inst4)
                check_index = check_index + 3
                flag[3] = 1
            elif word==inst5:
                inst.append(inst5)
                check_index = check_index + 1
                flag[4] = 1
            elif word == inst6:
                inst.append(inst6)
                check_index = check_index + 2
                flag[5] = 1
            elif word == inst7:
                inst.append(inst7)
                check_index = check_index + 2
                flag[6] = 1
            elif word == inst8:
                inst.append(inst8)
                check_index = check_index + 3
                flag[7] = 1
            elif word == inst9:
                inst.append(inst9)
                check_index = check_index + 2
                flag[8] = 1
            elif word == inst10:
                inst.append(inst10)
                check_index = check_index + 3
                flag[9] = 1
            elif word == inst11:
                inst.append(inst11)
                check_index = check_index + 3
                flag[10] = 1
            else:
                inst.append(word)
                size = len(inst[len(inst)-1])
                inst[len(inst)-1] = inst[len(inst)-1][:size-1]
                checkpointj[len(inst)-1] = check_index
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
                arr1 = word;
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

new_arr = []
arr_gap = [-1]
a_j = 0
while(a_j)<len(arr1):
    if arrinst1 == arr1[a_j]:
        arr_gap.append(a_j)
    a_j = a_j + 1
arr_gap.append(len(arr1))
k1 = 0
while(k1<len(arr_gap)-1):
    new_arr.append(arr1[(arr_gap[k1]+1):arr_gap[k1+1]])
    k1 = k1 + 1


i10 = 0
while(i10<len(new_arr)):
    arr.append(int(new_arr[i10]))
    i10 = i10 + 1




reg = {'zero': 0, 'ra': 0, 'sp': 0, 'gp': 0, 'tp': 0, 't0': 0, 't1': 0, 't2': 0, 's0': 0, 'a0': 0, 'a1': 0, 'a2': 0,
       'a3': 0, 'a4': 0, 'a5': 0, 'a6': 0, 'a7': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0, 's6': 0, 's7': 0, 's8': 0,
       's9': 0, 's10': 0, 's11': 0, 't3': 0, 't4': 0, 't5': 0, 't6': 0}

i = 0
j = 0
k = 0




while(i<len(inst)):
    if inst[i] == "add":
        reg[data[j]] = func.add(reg[data[j + 2]], reg[data[j + 1]])
        j = j + 3

    elif inst[i] == "li":
        reg[data[j]] = int(data[j + 1])
        j = j + 2

    elif inst[i] == "sub":
        reg[data[j]] = func.sub(reg[data[j + 1]], reg[data[j + 2]])
        j = j + 3
    elif inst[i] == "lw":
        reg[data[j]] = int(arr[int((int(reg[data[j + 1]]))/4)])
        j = j + 2
    elif inst[i] == "sw":
        arr[int((int(reg[data[j + 1]]))/4)] = int(reg[data[j]])
        j = j + 2
    elif inst[i] == 'addi':
        reg[data[j]] = reg[data[j + 1]] + int(data[j + 2])
        j = j + 3
    elif inst[i] == 'j':
        i = func.index1(data[j], inst)
        j = checkpointj[i]
    elif inst[i] == 'bne':
        i1= func.bne(reg[data[j]], reg[data[j + 1]], data[j + 2], inst, i)
        if i1==i:
            j = j + 3
            i = i1
        else:
            i = i1
            j = checkpointj[i]
    elif inst[i] == 'beq':
        i1 = func.beq(reg[data[j]], reg[data[j + 1]], data[j + 2], inst, i)
        if i1 == i:
            j = j + 3
            i = i1
        else:
            i = i1
            j = checkpointj[i]
    elif inst[i] == 'blt':
        i1 = func.blt(reg[data[j]], reg[data[j + 1]], data[j + 2], inst, i)
        if i1 == i:
            j = j + 3
            i = i1
        else:
            i = i1
            j = checkpointj[i]
    i = i +1
    if (j > len(data)):
        print("error")
        break


print("--------------------------------------------------------------------------")
print(reg)
print("--------------------------------------------------------------------------")
print("Memory consumed : " )
cal_1 = 31*(4) + len(arr)*(4)
print(str(cal_1) + " Bytes" )
print("---------------------------------------------------------------------------")
print(arr)

arr = []
import numpy as np
for line in open("inp3.txt").readlines():
    arr.append(line.replace("\n",""))

o2 = []
co2 = []
arr2 = arr.copy()
arr3 = arr.copy()
arr4 = arr.copy()
for idx in range(len(arr[0])):
    zc = 0
    oc = 0
    for v in arr:
        if v[idx] == "0":
            zc+=1
        else:
            oc+=1
    if zc > oc:
        max_e = "0"
    elif zc < oc:
        max_e = "1"
    else:
        max_e = "1"
    for binary in arr2:
        if len(arr) == 1:
            break
        o2 = list(set(o2))
        if binary[idx] == max_e:
            if binary in arr:
                o2.append(binary)
        else:
            if binary in o2:
                o2.remove(binary)
            if binary in arr:
                arr.remove(binary)
for idx in range(len(arr[0])):
    zc = 0
    oc = 0
    for v in arr3:
        if v[idx] == "0":
            zc += 1
        else:
            oc += 1
    if zc > oc:
        min_e = "1"
    elif zc < oc:
        min_e = "0"
    else:
        min_e = "0"
    for binary in arr4:
        if len(arr3) == 1:
            break
        co2 = list(set(co2))
        if binary[idx] == min_e:
            if binary in arr3:
                co2.append(binary)
        else:
            if binary in co2:
                co2.remove(binary)
            if binary in arr3:
                arr3.remove(binary)

v1 = list(set(o2))[0]
v2 = list(set(co2))[0]
print(int(v1, 2)*int(v2, 2))

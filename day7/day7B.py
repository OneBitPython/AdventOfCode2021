with open("inp7.txt")as f:
    arr = list(map(int, f.read().split(",")))

tmp = []
for i in range(max(arr)):
    curr = i
    a=0
    for j in range(len(arr)):
        dist = abs(curr-arr[j])
        a+=(dist*(dist+1))//2 # AP
    tmp.append(a)
print("answer : ",min(tmp))
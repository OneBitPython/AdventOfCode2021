arr = []
for line in open("inp6.txt").readlines():
    arr = list(map(int,line.split(",")))

for j in range(80):
    print(arr)
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i] = 7
            arr.append(8)
        arr[i]-=1

        
print(len(arr))
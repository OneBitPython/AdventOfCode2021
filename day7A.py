with open("inp7.txt")as f:
    arr = list(map(int, f.read().split(",")))
arr.sort()

middle = arr[len(arr)//2]
ans = 0
for i in arr:
    ans+=abs(i-middle)
print("answer : ",ans)
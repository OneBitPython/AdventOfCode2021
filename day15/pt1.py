arr = []
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day15\\inp15.txt").readlines():
    arr.append([int(x) for x in line.strip()])

cache = {}
def func(r,c):
    if (r,c)in cache:
        return cache[(r,c)]
    if r<0 or r>= len(arr) or c<0 or c>= len(arr[r]):
        return 1e19
    if r==len(arr)-1 and c==len(arr[r])-1:
        return arr[r][c]
    ans = arr[r][c]+min(func(r+1, c),func(r,c+1))
    cache[(r,c)] = ans
    return ans
print(func(0,0)-arr[0][0])
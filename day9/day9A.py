ans = 0
arr = []
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day9\\inp9.txt").readlines():
    tmp = []
    for value in line:
        if value!='\n':
            tmp.append(int(value))
        else:
            arr.append(tmp)
arr.append(tmp)
low_points = []
for i,row in enumerate(arr):
    for j, val in enumerate(row):
        neighbours = []
        if i>0:
            neighbours.append(arr[i-1][j])
        if i<len(arr)-1:
            neighbours.append(arr[i+1][j])
        if j > 0:
            neighbours.append(arr[i][j-1])
        if j<len(row)-1:
            neighbours.append(arr[i][j+1])

        for value in neighbours:
            if val >= value:
                break
        else:
            low_points.append(arr[i][j]+1)
print(sum(low_points))
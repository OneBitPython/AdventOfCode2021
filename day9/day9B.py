arr = []
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day9\\inp9.txt").readlines():
    tmp = []
    for value in line:
        if value != '\n':
            tmp.append(int(value))
        else:
            arr.append(tmp)
arr.append(tmp)
basin_size = []
visited = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
for x, row in enumerate(arr):
    for y, val in enumerate(row):
        i,j = x,y
        queue = [[i,j]]
        size = 0
        while (len(queue) > 0):
            i,j = queue.pop()
            if not visited[i][j]:
                visited[i][j] = 1
                if arr[i][j]!=9:
                    size+=1
                    neighbours = []
                    if i > 0:
                        neighbours.append([i-1, j])
                    if i < len(arr)-1:
                        neighbours.append([i+1, j])
                    if j > 0:
                        neighbours.append([i, j-1])
                    if j < len(row)-1:
                        neighbours.append([i, j+1])
                    for q in neighbours:
                        queue.append(q)
        basin_size.append(size)

basin_size.sort(reverse=True)
ans=basin_size[0]
for v in basin_size[1:3]:
    ans*=v
print(ans)
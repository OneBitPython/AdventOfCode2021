def is_valid(i, j):
    return (i >= 0 and i < row_len and j >= 0 and j < col_len)


def dfs(i, j):
    if(matrix[i][j] == -1):
        return 0
    elif(matrix[i][j] >= 9):
        count_flashes = 1
        matrix[i][j] = -1
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                new_r = i+r
                new_c = j+c
                if is_valid(new_r, new_c):
                    count_flashes += dfs(new_r, new_c)
        return count_flashes

    else:
        matrix[i][j] += 1
        return 0


f = open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day11\\inp11.txt", "r")
data = f.read()
matrix = [[int(j) for j in i] for i in data.split('\n')]

row_len = len(matrix)
col_len = len(matrix[0])
count_flashes = 0

steps = 0
while True:
    steps += 1
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == -1:
                continue
            if matrix[i][j] < 9:
                matrix[i][j] += 1
            else:
                count_flashes += dfs(i, j)

    total_sum = 0
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
            total_sum += matrix[i][j]
    if total_sum == 0:
        print(steps)
        break

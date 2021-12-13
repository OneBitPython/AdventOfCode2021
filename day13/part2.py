points = []
maxx = 0
maxy = 0
instructions = []
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day13\\inp13.txt"):
    if "fold along" not in line and line!='\n':
        points.append(list(map(int,line.strip().split(","))))
        maxx = max(maxx, points[-1][0])
        maxy = max(maxy, points[-1][1])
    if "fold along" in line:
        line = line.split("=")
        instructions.append([line[0][-1],int(line[1].strip())])


board = [["." for i in range(maxx+1)] for j in range(maxy+1)]
for point in points:
    board[point[1]][point[0]] = "#"

for b in instructions:
    inst = b[0]
    val = b[1]
    if inst == "y":
        for i in range(maxy, maxy-val, -1):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[maxy-i][j] = board[i][j]
        board = board[:val]
        maxy = len(board)-1
        maxx = len(board[0])
    else:
        for i in range(len(board)):
            for j in range(val+1):
                if board[i][len(board[0])-j-1] == "#":
                    board[i][j] = board[i][len(board[0])-j-1]
        new_board = []
        for row in board:
            new_board.append(row[:val])
        board = new_board
        maxx = len(board[0])
        maxy=len(board)-1
a = 0
for row in board:
    for val in row:
        print(val,end=" ")
    print()

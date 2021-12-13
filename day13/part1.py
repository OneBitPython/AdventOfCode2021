points = []
maxx=0
maxy=9
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day13\\inp13.txt"):
    if line!='\n':
        points.append(list(map(int,line.strip().split(","))))
        maxx = max(maxx, points[-1][0])
        maxy = max(maxy, points[-1][1])
    else:
        break
board = [["1" for i in range(maxx+1)] for j in range(maxy+1)]
for point in points:
    board[point[1]][point[0]]="#"
inst = "x"
val = 655

for i in range(len(board)):
    for j in range(val+1):
        if board[i][len(board[0])-j-1] == "#":
            board[i][j] = board[i][len(board[0])-j-1]
new_board = []
for row in board:
    new_board.append(row[:val])
board = new_board
a = 0
for i in range(len(board)):
    a+=board[i].count("#")
print(a)

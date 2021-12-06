arr = []
xmax = 0
ymax = 0
for line in open("inp5.txt").readlines():
    if line != '\n':
        line = line.split("->")
        one = line[0]
        two = line[1].replace("\n", "")
        
        x1, y1 = map(int, one.split(","))
        x2, y2 = map(int, two.split(","))

        if max(x1, x2) > xmax:
            xmax = max(x1, x2)
        if max(y1, y2) > ymax:
            ymax = max(y1, y2)
        arr.append([x1, y1, x2, y2])

draw = [[0 for i in range(xmax+1)] for j in range(ymax+1)]


def get_diagonal_points(x1,x2,y1,y2):
    if x1 > y1:
        increment = -1
    else:
        increment=1
    if x2 > y2:
        increment2 = -1
    else:
        increment2=1
    points = []
    for i,j in zip(range(x1, y1+increment, increment), range(x2, y2+increment2, increment2)):
        points.append([i,j])
    return points

for value in arr:
    x1, y1, x2, y2 = value
    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            draw[y1][i] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            draw[i][x1] += 1
    else:
        points = get_diagonal_points(x1,y1,x2,y2)
        for i in points:
            draw[i[1]][i[0]]+=1
a = 0

for i in draw:
    for j in i:
        if j >= 2:
            a += 1
print(a)

arr = []
xmax = 0
ymax = 0
for line in open("inp5.txt").readlines():
    if line !='\n':
        line = line.split("->")
        one = line[0]
        two = line[1].replace("\n","")
        x1,y1 = map(int,one.split(","))
        x2, y2 = map(int, two.split(","))

        if max(x1,x2)>xmax:
            xmax = max(x1,x2)
        if max(y1,y2)>ymax:
            ymax=max(y1,y2)
        if x1 == x2 or y1 == y2:
            arr.append([x1,y1,x2,y2])

draw = [[0 for i in range(xmax+1)] for j in range(ymax+1)]

for value in arr:
    x1,y1,x2,y2 = value
    if y1 == y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            draw[y1][i]+=1
    if x1==x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            draw[i][x1]+=1

a=0

for i in draw:
    for j in i:
        if j>=2:
            a+=1
print(a)
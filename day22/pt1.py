lookup = {}
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day22\\input22.txt").readlines():
    line = line.strip()
    instr = line[0]
    line = line[2:].split(",")
    values = []
    for value in line:
        value = value[2:]
        values.append(list(map(int,value.split(" "))))
    x1 = values[0][0]
    x2 = values[0][1]
    y1 = values[1][0]
    y2 = values[1][1]
    z1 = values[2][0]
    z2 = values[2][1]
    
    minx = min(x1, x2)
    maxx = max(x1, x2)+1
    miny = min(y1, y2)
    maxy = max(y1, y2)+1
    minz = min(z1, z2)
    maxz = max(z1, z2)+1

    if -50 <= minx <= maxx <=50 and -50 <=miny <= maxy <= 50 and -50 <=minz <= maxz <=50:
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                for z in range(minz, maxz):
                    lookup[(x,y,z)] = int(instr)
print(sum(lookup.values()))
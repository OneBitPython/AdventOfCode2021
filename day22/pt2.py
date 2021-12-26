InstructMaster = []
with open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day22\\input22.txt", "r") as data:
    Count = 0
    for t in data:
        OnOff, Coords = t.strip().split(" ")
        x, y, z = Coords.split(",")
        InstructMaster.append([OnOff, x, y, z])
        Count+=1
        #if Count == 20:
        #    break

InstructSecond = []
for r in InstructMaster:
    InstructLine = []
    OnOff = r[0]
    X = r[1][2:]
    X1, X2 = X.split("..")
    X1 = int(X1)
    X2 = int(X2)
    if X1 > X2:
        X2, X1 = X1, X2
    Y = r[2][2:]
    Y1, Y2 = Y.split("..")
    Y1 = int(Y1)
    Y2 = int(Y2)
    if Y1 > Y2:
        Y2, Y1 = Y1, Y2
    Z = r[3][2:]
    Z1, Z2 = Z.split("..")
    Z1 = int(Z1)
    Z2 = int(Z2)
    if Z1 > Z2:
        Z2, Z1 = Z1, Z2
    InstructSecond.append([OnOff, X1, X2, Y1, Y2, Z1, Z2])

InstructThird = []
for r in range(len(InstructSecond)):
    InstructThird.append(InstructSecond.pop())

CubeHitboxList = []
CubeOnCount = 0

def AttemptAddCube(OnOff, X1, X2, Y1, Y2, Z1, Z2, FirstIndex, Level):
    global CubeOnCount
    for f in range(FirstIndex, len(CubeHitboxList)):
        if X1 > CubeHitboxList[f][0] and X2 < CubeHitboxList[f][1] and Y1 > CubeHitboxList[f][2] and Y2 < CubeHitboxList[f][3] and Z1 > CubeHitboxList[f][4] and Z2 < CubeHitboxList[f][5]:
            return
    
    if OnOff == "on":
        Uncracked = True
        for f in range(FirstIndex, len(CubeHitboxList)):
            XOver = False
            YOver = False
            ZOver = False
            A1 = CubeHitboxList[f][0]
            A2 = CubeHitboxList[f][1]
            B1 = CubeHitboxList[f][2]
            B2 = CubeHitboxList[f][3]
            C1 = CubeHitboxList[f][4]
            C2 = CubeHitboxList[f][5]
            if (X1 > A2 or X2 < A1):
                XOver = False
            else:
                XOver = True
            if (Y1 > B2 or Y2 < B1): 
                YOver = False
            else: 
                YOver = True
            if (Z1 > C2 or Z2 < C1):
                ZOver = False
            else:
                ZOver = True
            if XOver and YOver and ZOver:
                if X1 < A1:
                    NX1 = A1
                    AttemptAddCube("on", X1, A1-1, Y1, Y2, Z1, Z2, (f+1), Level+1)
                else:
                    NX1 = X1
                if X2 > A2:
                    NX2 = A2
                    AttemptAddCube("on", A2+1, X2, Y1, Y2, Z1, Z2, (f+1), Level+1)
                else:
                    NX2 = X2
                if Y1 < B1:
                    NY1 = B1
                    AttemptAddCube("on", NX1, NX2, Y1, B1-1, Z1, Z2, (f+1), Level+1)
                else:
                    NY1 = Y1
                if Y2 > B2:
                    NY2 = B2
                    AttemptAddCube("on", NX1, NX2, B2+1, Y2, Z1, Z2, (f+1), Level+1)
                else:
                    NY2 = Y2
                if Z1 < C1:
                    NZ1 = C1
                    AttemptAddCube("on", NX1, NX2, NY1, NY2, Z1, C1-1, (f+1), Level+1)
                if Z2 > C2:
                    NZ2 = C2
                    AttemptAddCube("on", NX1, NX2, NY1, NY2, C2+1, Z2, (f+1), Level+1)
                Uncracked = False
                break
                #This break was the bane of my existance for 4 hours
                
        if Uncracked:
            NewCount = (X2 - X1 + 1)*(Y2 - Y1 + 1)*(Z2 - Z1 + 1)
            CubeOnCount += NewCount
            #if Level == 0:
            #    print("Top level cube passed uncracked")
            #print(f"Scored Cube bounded by {X1}, {X2}, {Y1}, {Y2}, {Z1}, {Z2}, Level {Level}")
            #print(NewCount)

    if Level == 0:        
        CubeHitboxList.append([X1, X2, Y1, Y2, Z1, Z2])
        #print(f"{len(CubeHitboxList) = }")
        #print(CubeOnCount)

CycleCount = 0
for t in InstructThird:
    AttemptAddCube(str(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4]), int(t[5]), int(t[6]), 0, 0)
    CycleCount += 1
    print(f"Cube Number {421 - CycleCount} added.")
    #if CycleCount == 10:
    #    break

print(f"{CubeOnCount = }")

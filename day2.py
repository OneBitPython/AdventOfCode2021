arr = []
x = 0
y = 0
aim = 0
for line in open("inp2.txt"):
    one, two = line.split()
    if one == "forward":
        x+=int(two)
        y+=aim*int(two)
    elif one == "down":
        aim+=int(two)
    elif one == "up":
        aim-=int(two)
        
print("ans :",abs(x*y))

ans=0
for line in open("inp8.txt").readlines():
    line = line.split(" | ")
    for value in line[1].split():
        if len(value)==2 or len(value)==3 or len(value)==4 or len(value)==7:
            ans+=1
print(ans)
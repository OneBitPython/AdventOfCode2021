template = {}
starting = ""
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day14\\inp14.txt").readlines():
    if line != '\n':
        if "->" in line:
            line = line.strip().split(" -> ")
            template[line[0]] = line[1]
        else:
            starting = line.strip()
starting = [i for i in starting]
new_starting = ""
v = []
for j in range(10):
    for i in range(len(starting)-1):
        new_starting += starting[i]
        if starting[i]+starting[i+1] in template:
            new_starting += template[starting[i]+starting[i+1]]
    new_starting+=starting[-1]
    starting = new_starting
    ans = starting
    new_starting = ""

comp = []
for i in ans:
    if i not in comp:
        comp.append(i)
counts = []
for value in comp:
    counts.append(ans.count(value))
print(max(counts)-min(counts))
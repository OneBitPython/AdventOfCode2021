templates = {}
starting = ""
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day14\\inp14.txt").readlines():
    if line != '\n':
        if "->" in line:
            line = line.strip().split(" -> ")
            templates[line[0]] = line[1]
        else:
            starting = line.strip()
from collections import Counter,defaultdict
c = Counter()
for i in range(len(starting)-1):
    c[starting[i]+starting[i+1]]+=1

for q in range(40):
    new = Counter()

    for template in c:
        new[template[0]+templates[template]]+=c[template]
        new[templates[template]+template[1]] += c[template]
    c = new
dict_ = defaultdict(int)
for template in c:
    dict_[template[0]] += c[template]
dict_[starting[-1]] += 1
print(max(dict_.values())-min(dict_.values()))
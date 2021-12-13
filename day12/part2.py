from collections import defaultdict

neighbours = defaultdict(lambda : [])
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day12\\inp12.txt"):
    line = line.strip().split("-")
    neighbours[line[0]].append(line[1])
    neighbours[line[1]].append(line[0])

queue = [("start",set(["start"]),False)]
ans = 0
while queue:
<<<<<<< HEAD
    pos,small_caves,mode = queue.pop()
=======
    pos,small_caves,mode = queue.pop(0)
>>>>>>> e490694897044bf3e6cfbaee9b01315a7cfb0f27
    if pos == 'end':
        ans+=1
    else:
        for neighbour in neighbours[pos]:
            if neighbour not in small_caves:
                new_small_caves = set(small_caves)
                if neighbour.islower():
                    new_small_caves.add(neighbour)
                queue.append((neighbour,new_small_caves, mode))
            else:
                if mode == False and neighbour not in ["start", "end"]:
                    queue.append((neighbour, small_caves, True))
print(ans)

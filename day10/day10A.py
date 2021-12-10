arr = []
inverse = {">": "<", "]": "[", ")": "(", "}": "{"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}

ans = 0
for line in open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day10\\inp10.txt").readlines():
    stack = []

    line = line.strip()
    incorrect = ""
    for value in line:
        if value in inverse.values():
            stack.append(value)
        elif value in inverse.keys():
            if len(stack)>0 and inverse[value]==stack[-1]:
                stack.pop()
            else:
                incorrect = value
                break

    ans+=score[incorrect]
print(ans)
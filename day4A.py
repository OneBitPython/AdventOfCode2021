tmp = []

with open("inp4.txt")as f:
    content = f.read().splitlines()
nums = content[0]
nums = list(map(int, nums.split(",")))
tmp = []
arr = []
for i in content[2:]:
    if i!= '':
        tmp.append(list(map(int, i.split())))
    else:
        arr.append(tmp)
        tmp = []
arr.append(tmp)
deleted = [[] for i in range(len(arr))]

b = False
final = []
comp = 0
for num in nums:
    i=-1
    if b:
        break
    for board in arr:
        i+=1
        if b:
            break
        for j, row in enumerate(board):
            if num in row:
                idx = row.index(num)
                row[row.index(num)] = -1
                if board[0][idx] == -1 and board[1][idx] == -1 and board[2][idx] == -1 and board[3][idx] == -1 and board[4][idx] == -1:
                    final = board
                    comp = num
                    b=True
                    break
            for value in row:
                if value != -1:
                    break
            else:
                final = board
                comp = num
                b = True
                break            

a = 0
for row in final:
    for num in row:
        if num!=-1:
            a+=num
print(a*comp)
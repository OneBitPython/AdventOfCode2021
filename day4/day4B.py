tmp = []

with open("inp4.txt")as f:
    content = f.read().splitlines()
nums = content[0]
nums = list(map(int, nums.split(",")))
tmp = []
arr = []
for i in content[2:]:
    if i != '':
        tmp.append(list(map(int, i.split())))
    else:
        arr.append(tmp)
        tmp = []
arr.append(tmp)

b = False
arr2 = arr.copy()
for num in nums:
    if b:
        break
    for board in arr:
        if b:
            break
        for row in board:
            if num in row:
                idx = row.index(num)
                row[row.index(num)] = -1
                if board[0][idx] == -1 and board[1][idx] == -1 and board[2][idx] == -1 and board[3][idx] == -1 and board[4][idx] == -1:
                    if board in arr2:
                        if len(arr2) == 1:
                            final = arr2[0]
                            b = True
                            comp = num
                            break

                        arr2.remove(board)
            for value in row:
                if value != -1:
                    break
            else:
                if board in arr2:
                    if len(arr2) == 1:
                        final = arr2[0]
                        b = True
                        comp = num
                        break

                    arr2.remove(board)
a = 0
for row in final:
    for v in row:
        if v!=-1:
            a+=v
print(comp*a)

ans=0
for line in open("inp8.txt").readlines():
    line = line.split(" | ")    
    board = ['0' for i in range(7)]
    # if len(3) value is 7, if len(2) value is 1, if len(4) value is 4, if len(7) value is 8
    idxs = {3: (0, 2, 5), 2: (2, 5), 4: (1, 2, 3, 5), 7: (0, 1, 2, 3, 4, 5, 6)}
    pos_len_five = {5 : (0, 1, 3, 5, 6), 2:(0,2,3,4,6),3:(0,2,3,5,6)} #all values in which num sigs on are repeating
    pos_len_six = {6: (0, 1, 3, 4, 5, 6), 9: (0, 1, 2, 3, 5, 6), 0:(0,1,2,4,5,6)}
    
    for value in line[0].split():
        null_points = []
        pos_of_val = ""
        len_v = len(value)
        if len_v==5 or len_v==6:
            pass
        else:
            for i, pos in enumerate(idxs[len_v]):
                if board[pos] == '0' or board[pos]==value[i]:
                    if value[i] in board:
                        board[board.index(value[i])] = "0"
                    board[pos] = value[i]
                else:
                    #swap
                    if board[pos] != value[i]:
                        for j, b in enumerate(board):
                            if b == '0':
                                null_points.append(j)
                            if b == value[i]:
                                pos_of_val = j
                                break
                    
                    if pos_of_val!="":
                        board[pos_of_val], board[pos] = board[pos], board[pos_of_val]
                    else:
                        board[null_points[0]], board[pos] = board[pos], board[null_points[0]]
                        
                print(board, value, pos)

    digits = []
    for v in line[1].split():
        q = 3
        if len(v)==5 or len(v)==6:
            contains = []
            for rval in v:
                contains.append(board.index(rval))
            contains.sort()
            if len(v)==5:
                dict_ = pos_len_five
            else:
                dict_ = pos_len_six
            for key, value in dict_.items():
                if value == tuple(contains):
                    q=key
                    break
            digits.append(q)
        else:
            if len(v)==3:
                digits.append(7)
            elif len(v)==4:
                digits.append(4) 
            elif len(v)==7:
                digits.append(8)
            elif len(v)==2:
                digits.append(1)
    sub_ans = int("".join(list(map(str,digits))))
    ans+=sub_ans
print(ans)
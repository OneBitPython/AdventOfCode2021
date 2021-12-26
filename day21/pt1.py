pos = [7,4] 
score = [0, 0]

die = 0
turn = 0
rolls = 0
while score[0] < 1000 and score[1] < 1000:
    for r in range(3):
        die = die % 100 + 1
        pos[turn] += die
        rolls += 1
    pos[turn] = (pos[turn] - 1) % 10 + 1
    score[turn] += pos[turn]
    turn = (turn + 1) % 2
print(min(score)*rolls)


import sys
import itertools
from collections import defaultdict, Counter


digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}


def find_perm_slow(before):
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord('a')+i)] = chr(ord('a')+perm[i])
        for w in before:
            w_perm = ''
            for c in w:
                w_perm += D[c]
            w_perm = ''.join(sorted(w_perm))

            if w_perm not in digits.values():
                ok = False
        if ok:
            return D

ans = 0
p1 = 0
for line in open("inp8.txt").readlines():
    before, after = line.split(" | ")
    D = find_perm_slow(before.split())
    ret = ''
    for w in after.split():
        w_perm = ''
        for c in w:
            w_perm += D[c]
        w_perm = ''.join(sorted(w_perm))
        d = [k for k, v in digits.items() if v == w_perm]
        if d[0] in [1, 4, 7, 8]:
            p1 += 1
        ret += str(d[0])
    ans += int(ret)
print(ans)
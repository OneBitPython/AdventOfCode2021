import collections

with open("inp6.txt")as f:
    arr =list(map(int, f.read().split(',')))
fish = collections.defaultdict(lambda:0)
for j in arr:
    fish[j]+=1


def func(fish,n):
    if n==0:
        return fish
    counts = collections.defaultdict(lambda :0)
    for el, count in fish.items():
        if el==0:
            counts[6] += count
            counts[8] += count
        else:
            counts[el-1] += count
            
    return func(counts, n-1)

fish = func(fish,256)
print(sum(fish.values()))
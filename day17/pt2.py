minx = 269
maxx = 292
miny = -68
maxy = -44

ans = 0
for VX in range(500):
    for VY in range(-100,1000):

        x, y = 0, 0
        ok = False
        vx, vy = VX, VY
        for t in range(1000):
            x += vx
            y += vy
            if vx < 0:
                vx += 1
            if vx > 0:
                vx -= 1
            vy -= 1

            if x <= maxx and x >= minx and y >= miny and y <= maxy:
                ok = True
                break
        if ok:
            ans+=1
            print(ans)
print(ans)

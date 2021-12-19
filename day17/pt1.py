minx = 269
maxx = 292
miny = -68
maxy = -44

ans = 0
for VX in range(150):
    for VY in range(500):

        x,y = 0,0
        ok  = False
        vx, vy = VX, VY
        m = 0
        for t in range(1000):
            x+=vx
            y+=vy
            m = max(m, y)
            if vx < 0:
                vx+=1
            if vx >0:
                vx-=1
            vy-=1

            if x <= maxx and x >= minx and y >= miny and y<=maxy:
                ok = True
        if ok:
            ans = max(m, ans)
            print(ans)
print(ans)

def odometer(oksana):
    N = len(oksana)
    v = []
    h = 0
    t = []
    s = 0
    for i in range(N):
        if i%2 == 0:
            v.append(oksana[i])
        else:
            t.append(oksana[i] - h)
            h = oksana[i]
    for k in range(N//2):
        s += v[k]*t[k]  
    return s
    


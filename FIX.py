# cook your dish here
for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    
    y = []
    z = {}
    maxi = max(x)
    for i in range(n):
        if z.setdefault(x[i],0)==0:
            y.append(x[i])
            z[x[i]]=1
            
        else:
            y.append(maxi)
            z[maxi]=1 
    print(*y)
            
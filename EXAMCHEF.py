# cook your dish here
for t in range(int(input())):
    x,y,z = map(int,input().split())
    total = x * y   
    if( z > (total//2)):
        print("YES")
    else:
        print("NO")
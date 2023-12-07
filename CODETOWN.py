# cook your dish here
for t in range(int(input())):
    town = input()
    req = ['1','0','1','0','1','0','1','1']
    vow = ['A','E','I','O','U']
    
    if(town == "CODETOWN"):
        print("YES")
    else:
        town=list(town)
        for i in range(len(town)):
            if(town[i] in vow):
                town[i]='0'
            else:
                town[i]='1' 
        
        if(town==req):
            print("YES")
        else:
            print("NO")
        
            
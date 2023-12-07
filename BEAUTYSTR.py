# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    total = 1
    for i in range(26):
        total *= s.count(a[i])+1
    print((total-1)%((10**9)+7))
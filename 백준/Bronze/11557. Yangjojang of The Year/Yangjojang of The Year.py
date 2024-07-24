t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for _ in range(n):
        u,a=input().split()
        a=int(a)
        arr.append((a,u))
        
    print(max(arr)[1])
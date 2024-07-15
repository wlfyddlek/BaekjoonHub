n=int(input())
chc=list(map(int,input().split()))
number=chc[0]//2+chc[1]
if number>n:
    print(n)
else:
    print(number)
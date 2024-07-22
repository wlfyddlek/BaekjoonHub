arr=[]
scr=0
for _ in range(10):
    a=int(input())
    arr.append(a)
for i in arr:
    scr+=i
    if scr==100:
        break
    if scr >=100:
        if scr-100>100-(scr-i):
            scr-=i
            break
print(scr)
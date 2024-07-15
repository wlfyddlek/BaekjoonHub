n,l=map(int,input().split())
frt=list(map(int,input().split()))
frt.sort()
for i in range(n):
    if l >= frt[i]:
        l+=1
    else:
        break
print(l)

n=int(input())
test=list(map(int,input().split()))
m=max(test)
fake=[]
for s in test:
    fake.append(s/m*100)
avg=sum(fake)/n
print(avg)

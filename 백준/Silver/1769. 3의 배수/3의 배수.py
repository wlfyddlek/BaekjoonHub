n=input()
count=0
while len(n) > 1:
    count +=1
    sum=0
    for i in n:
        sum+=int(i)
    n=str(sum)

print(count)

if int(n)%3==0:
    print("YES")
else:
    print("NO")
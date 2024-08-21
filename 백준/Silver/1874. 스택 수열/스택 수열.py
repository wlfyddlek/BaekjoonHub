import sys
n=int(sys.stdin.readline().strip())

result=[]
stack=[]

num=1
for _ in range(n):
    seq=int(sys.stdin.readline().strip())
    while num<=seq:
        stack.append(num)
        result.append('+')
        num+=1
    if stack[-1]==seq:
        stack.pop()
        result.append("-")
    else:
        result.clear()
        result.append("NO")
        break
for answer in result:
    print(answer)
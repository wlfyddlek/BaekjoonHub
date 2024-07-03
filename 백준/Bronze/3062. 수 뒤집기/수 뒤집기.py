n = int(input())

for _ in range(n):
    num=int(input())
    reverse_num=int(str(num)[::-1])
    plus=str(num+reverse_num)
    
    if plus== plus[::-1]:
        print("YES")
    else:
        print("NO")
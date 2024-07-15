while True:
    n=int(input())
    reverse_n=int(str(n)[::-1])
    if reverse_n==n==0:
        break
    elif reverse_n==n:
        print('yes')
    else:
        print('no')

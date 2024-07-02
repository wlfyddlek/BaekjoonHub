N = int(input())
players = [list(map(int, input().split())) for i in range(N)]

def calculate(dice):
    dicecount=[0]*7
    
    for d in dice:
        dicecount[d] +=1

        max_count=max(dicecount)
    
    if max_count ==4:
        prize= 50000+dicecount.index(4)*5000
    elif max_count==3:
        prize= 10000+dicecount.index(3)*1000
    elif max_count==2:
        if dicecount.count(2)==2:
            pair1=dicecount.index(2)
            pair2=dicecount.index(2, pair1+1)
            prize=2000+pair1*500 + pair2*500
        else:
            prize=1000+dicecount.index(2)*100
    else:
        prize=max(dice)*100

        
    return prize
maxprize= max(calculate(player) for player in players)
print(maxprize)
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plain_text=input()
text=''

for c in plain_text:
    if alphabet.find(c) != -1:
        i = alphabet.index(c) -3
        if i > len(alphabet) -1:
            p= alphabet[i-26]
        else:
            p=alphabet[i]
    
    else:
        p=c
    text=text+p
print(text)
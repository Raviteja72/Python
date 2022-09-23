s=input()

l=[list(map(str,i)) for i in s.split()]

#print(l)

for i in range(len(l)):
    for j in range(len(l[i])-1):
        if(ord(l[i][j].lower()) < ord(l[i][j+1].lower())):
            l[i][j+1] = l[i][j+1].upper()
        if(ord(l[i][j].lower()) > ord(l[i][j+1].lower())):
            l[i][j+1] = l[i][j+1].lower()
            
      
#print(l)

p=""
for i in l:
    for j in i:
        p=p+j
    p=p+' '
    
print(p)


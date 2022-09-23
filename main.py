string=input()
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "zyxwvutsrqponmlkjihgfedcba"
dig = "1234567890"
sp ="_#@%"
s=0
c=1
output = ''
check = list(string.split(" "))
#print(check)
for i in check:
    for j in range(len(i)):
        if(i[j] in dig):
            output+=sp[s]
            #print(output)
            s=s+1 
            if(s == 4):
                s=0 
        elif(i[j] in str1):
            index = str1.find(i[j])
            revs = str2[index]
            if(c==5):
                output+=revs.upper()
                c=1 
            else:
                output+=revs.casefold()
                c+=1 
        else:
            output+=i[j]
    output+=' '
            
print(output)
# 227b Baker St, London NW3 6XE7
            
            
            
            
        
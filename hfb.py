l=[]
for i in range(97,123):
    l.append(chr(i))
#print(l)
d={}
st,en=0,len(l)-1
for i in range(len(l)):
    d[l[st]] = l[en]
    st=st+1
    en=en-1
s="hi ra how are you"
print(s)
#print(d)
for i in s:
    if(i == ' '):
        print(' ',end='')
    else:
        for k,v in d.items():
            if(k == i):
                print(v,end='')
        
        

        
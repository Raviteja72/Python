from itertools import permutations
l=list(map(int,input().split()))
l=l*3
s=int(input())
perm=permutations(l,2)
pl=[]
for i in list(perm):
    pl.append((i))

kl=[]
pl=list(set(pl))
for i in range(len(pl)):
    pl[i]=tuple(sorted(pl[i]))
pl=list(set(pl))
print(pl)
c=0
for i in pl:
    if(sum(i)%s == 0):
        print(i,end=' ')
        c=c+1
print(c)
        
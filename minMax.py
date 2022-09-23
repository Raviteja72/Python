from itertools import permutations

l=list(map(int,input().split()))
l1=l
n=len(l)

l=l*n
perm = permutations(l,n)
perm1 = permutations(l,n-1)
l=[]
for i in list(perm):
    #print(i)
    l.append(i)
for i in list(perm1):
    #print(i)
    l.append(i)
    
l = list(set(l))
#print(l)

sums=[]
for i in l:
    sums.append(sum(i))
sums=list(set(sums))
#print(sums)

for i in range(l1[-1]+1,l1[-1]+6):
    if i not in sums:
        print(i)
        exit(0)
print('-1')


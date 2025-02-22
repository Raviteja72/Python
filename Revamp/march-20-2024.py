st = "RaaRe"
ans = ""
org = st

if(st == st[::-1]):
    print(st," is palindrome")
else:
    print(st," is not palindrome")

for i in range(len(st)-1,-1,-1):
    ans += st[i]
if(ans == org):
    print(st," is palindrome")
else:
    print(st," is not palindrome")


s = "Raviteja"
n = len(s)
for i in range(len(s)):
    for j in range(i+1,n+1):
        print(s[i:j])

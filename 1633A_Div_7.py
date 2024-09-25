def div_7(n):
    if n%7==0:
        return n
    m=-1
    s=str(n)
    for i in range(len(s)):
        t=s[:i]
        for j in range(10):
            h=int(t+str(j)+s[i+1:])
            if h%7==0:
                m=max(m,h)
    return m
for _ in range(int(input())):
    print(div_7(int(input())))

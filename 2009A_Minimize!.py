def minimize(a,b):
    mn=999999999
    for c in range(1,11):
        v=(c-a)+(b-c)
        mn=min(mn,v)
    return mn

for _ in range(int(input())):
    x,y=[int(i) for i in input().split()]
    print(minimize(x,y))

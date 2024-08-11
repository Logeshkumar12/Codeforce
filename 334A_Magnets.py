n=int(input())
series=""
for i in range(n):
    if i==0:    series+=input()
    else:
        v=input()
        if series[-1]=="1" and v[0]=="1":
            series+=" "+v
        elif series[-1]=="0" and v[0]=="0":
            series+=" "+v
        else:
            series+=v
print(len(series.strip().split()))

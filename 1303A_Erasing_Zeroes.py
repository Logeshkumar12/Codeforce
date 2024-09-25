def rem_0(s):
    if "0" not in s or "1" not in s:    return 0
    st,ed=0,len(s)-1
    while st<ed:
        if s[st]=="0" and s[ed]=="0":
            st+=1
            ed-=1
        elif s[st]=="0" and s[ed]=="1":
            st+=1
        elif s[st]=="1" and s[ed]=="0":
            ed-=1
        else:   return s[st:ed].count("0")
    return 0
for _ in range(int(input())):
    print(rem_0(input()))

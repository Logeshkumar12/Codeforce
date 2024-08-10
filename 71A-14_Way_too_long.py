def way_too_long(s : str) -> str:
    if len(s)<=10:
        return s
    return s[0]+str(len(s)-2)+s[-1]
n=int(input())
for i in range(n):
    print(way_too_long(input()))

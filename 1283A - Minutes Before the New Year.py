def minute_count(h,m):
    return ((23-h)*60)+(60-m)

n=int(input())
for _ in range(n):
    h,m=[int(i) for i in input().strip().split()]
    print(minute_count(h,m))

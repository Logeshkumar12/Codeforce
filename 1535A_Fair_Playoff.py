def is_fair(arr) -> str:
    w1=max(arr[:2])
    w2=max(arr[2:])
    l1,l2=min(arr[:2]),min(arr[2:])
    if l1>w2 or l2>w1:
        return "NO"
    return "YES"

if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        print(is_fair([int(i) for i in input().split()]))

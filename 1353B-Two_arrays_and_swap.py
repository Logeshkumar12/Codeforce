def attain_max_sum(a,b,k) -> int:
    for _ in range(k):
        mx=max(b)
        mn=min(a)
        if mn>=mx:
            return sum(a)
        else:
            a.remove(mn)
            a.append(mx)
            b.remove(mx)
            b.append(mn)
    return sum(a)

if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        l,k=tuple(map(int,input().split()))
        ar1=list(map(int,input().split()))
        ar2=list(map(int,input().split()))
        print(attain_max_sum(ar1,ar2,k))

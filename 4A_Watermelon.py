def watermelon(weight) -> str:
    if weight==2:
        return "NO"
    return "YES" if weight%2==0 else "NO"
kilo=int(input())
print(watermelon(kilo))

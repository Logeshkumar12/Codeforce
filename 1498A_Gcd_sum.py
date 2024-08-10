def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def gcd_sum(num):
    while True:
        if gcd(num,sum([int(i) for i in str(num)])) > 1:
            return num
        num+=1
n=int(input())
for i in range(n):
    x=int(input())
    print(gcd_sum(x))

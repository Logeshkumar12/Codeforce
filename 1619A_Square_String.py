def Square_string(x):
    for i in range(len(x)):
        if x[:i]==x[i:]:
            return "YES"
    return "NO"
    
if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        print(Square_string(input()))

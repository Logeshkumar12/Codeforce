def find_borrow(price,cash,no_of_banana) -> int:
    tot_cost=0
    for i in range(1,no_of_banana+1):
        tot_cost+=price*i
    if tot_cost<cash:
        return 0
    return tot_cost-cash
 
rate,wallet,no_of_B=[int(i) for i in input().split()]
print(find_borrow(rate,wallet,no_of_B))

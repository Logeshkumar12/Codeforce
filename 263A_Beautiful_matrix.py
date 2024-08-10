def beautiful_matrix(mat) -> int:
    if mat[2][2]==1:
        return 0
    quad=[]
    for i in range(5):
        for j in range(5):
            if mat[i][j]==1:
                return abs(3-(i+1))+abs(3-(j+1))
 
grid=[]
for i in range(5):
    tm=[int(i) for i in input().strip().split()]
    grid.append(tm)
print(beautiful_matrix(grid))

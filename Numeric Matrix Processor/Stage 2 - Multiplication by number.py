x, y = input().split() 
row = int(x)
col = int(y)
mat = []

for i in range (row):
    a = list(map(int,input().split()))
    mat.append(a)

mul = int(input())
result = [ [ 0 for i in range(col) ] for j in range(row) ] 

for i in range (row):
    for j in range (len(mat[0])):
        result[i][j] = mat[i][j] * mul

for row in result:
    print(*row)
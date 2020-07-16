x, y = input().split() 
row = int(x)
col = int(y)
mat = []

for i in range (row):
    a = list(map(int,input().split()))
    mat.append(a)

x, y = input().split() 
row2 = int(x)
col2 = int(y)

if row != row2 or col != col2:
    print("ERROR")

else:
    mat2 = []
    for i in range (row2):
        a = list(map(int,input().split()))
        mat2.append(a)

    result = res = [ [ 0 for i in range(col) ] for j in range(row) ] 

    for i in range (row2):
        for j in range (len(mat[0])):
            result[i][j] = mat[i][j] + mat2[i][j]

    for row in result:
        print(*row)
while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')

    choice = int(input('Your choice: '))

    if choice == 0:
        break

    elif choice == 2:
        x, y = input('Enter size of matrix: ').split() 
        row = int(x)
        col = int(y)
        print('Enter matrix: ')
        mat = []

        for i in range (row):
            a = list(map(float,input().split()))
            mat.append(a)

        mul = int(input('Enter constant: '))
        result = [ [ 0 for i in range(col) ] for j in range(row) ] 

        for i in range (row):
            for j in range (len(mat[0])):
                result[i][j] = mat[i][j] * mul
        print("The result is: ")
        for row in result:
            print(*row)

    elif  choice == 1:
        x, y = input('Enter size of first matrix: ').split() 
        row = int(x)
        col = int(y)
        mat = []
        print('Enter first matrix:')
        for i in range (row):
            a = list(map(float,input().split()))
            mat.append(a)

        x, y = input('Enter size of second matrix: ').split()
        row2 = int(x)
        col2 = int(y)

        if row != row2 or col != col2:
            print("The operation cannot be performed.")
        
        else:
            print('Enter second matrix:')
            mat2 = []
            for i in range (row2):
                a = list(map(float,input().split()))
                mat2.append(a)

            result = res = [ [ 0 for i in range(col) ] for j in range(row) ] 

            for i in range (row2):
                for j in range (len(mat[0])):
                    result[i][j] = mat[i][j] + mat2[i][j]
            print('The result is:')
            for i in range (row2):
                for j in range (col2):
                    print(result[i][j], end = " ")
                print()

    elif choice == 3:
        x, y = input('Enter size of first matrix: ').split() 
        row = int(x)
        col = int(y)
        mat = []
        print('Enter first matrix:')
        for i in range (row):
            a = list(map(float,input().split()))
            mat.append(a)

        x, y = input('Enter size of second matrix: ').split()
        row2 = int(x)
        col2 = int(y)

        if col != row2:
            print("The operation cannot be performed.")

        else:
            print('Enter second matrix:')
            mat2 = []
            for i in range (row2):
                a = list(map(float,input().split()))
                mat2.append(a)

            result = [ [ 0 for i in range(col2) ] for j in range(row) ] 

            for i in range (len(mat)):
                for j in range (len(mat2[0])):
                    for k in range(len(mat2)):
                        result[i][j] += mat[i][k] * mat2[k][j]
            print('The result is:')
            for i in range (row):
                for j in range (col2):
                    print(result[i][j], end = " ")
                print()




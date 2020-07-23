def matrix_input(choice, transpose_choice):
    # 1. Add matrices
    # 3. Multiply matrices
    if choice == 1 or choice == 3:
        dim_a = [int(x) for x in input("Enter size of first matrix: ").split()]

        n = 0
        matrix_a = []
        print("Enter first matrix:")
        while n < dim_a[0]:
            # get matrix row
            matrix_a.append(input().split())
            # convert data to int
            matrix_a[n] = [float(x) for x in matrix_a[n]]
            n += 1

        dim_b = [int(x) for x in input("Enter size of second matrix: ").split()]

        if (dim_a != dim_b and choice == 1) or (dim_a[1] != dim_b[0] and choice == 3):
            return print_result("ERROR")

        n = 0
        matrix_b = []
        print("Enter second matrix:")
        while n < dim_b[0]:
            # get matrix row
            matrix_b.append(input().split())
            # convert data to int
            matrix_b[n] = [float(x) for x in matrix_b[n]]
            n += 1

        if choice == 1:
            return matrix_add(dim_a, matrix_a, matrix_b)
        else: #choice 3
            return matrix_multiplication(dim_a, matrix_a, dim_b, matrix_b)

    else:
        # 2. Multiply matrix by a constant
        # 4. Transpose matrix
        # 5. Calculate a determinant
        # 6. Inverse matrix
        dim_a = [int(x) for x in input("Enter size of matrix:").split()]

        n = 0
        matrix_a = []
        print("Enter matrix:")
        while n < dim_a[0]:
            # get matrix row
            matrix_a.append(input().split())
            # convert data to int
            matrix_a[n] = [float(x) for x in matrix_a[n]]
            n += 1

        if choice == 2:
            constant = float(input("Enter constant:"))
            return matrix_multiply_constant(dim_a, matrix_a, constant)
        elif choice == 4:
            if transpose_choice == 1:
                return matrix_transpose_main (dim_a, matrix_a)
            elif transpose_choice == 2:
                return matrix_transpose_side (dim_a, matrix_a)
            elif transpose_choice == 3:
                return matrix_transpose_vertical (dim_a, matrix_a)
            return matrix_transpose_horizontal (dim_a, matrix_a)
        elif choice == 5:
            if dim_a[0] != dim_a[1]:
                return print_result("ERROR")
            return print_result(determinant_matrix(matrix_a))
        elif choice == 6:
            if dim_a[0] != dim_a[1]:
                return print_result("ERROR")
            return matrix_inverse(matrix_a)


def matrix_add(dim_a, matrix_a, matrix_b):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])
        for j in range(dim_a[1]):
            matrix_result[i].append(matrix_a[i][j] + matrix_b[i][j])
    return print_result(matrix_result)


def matrix_multiplication(dim_a, matrix_a, dim_b, matrix_b):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])  # add an empty element to the list
        for j in range(dim_b[1]):
            cell = 0
            for k in range(dim_a[1]):
                cell += matrix_a[i][k] * matrix_b[k][j]
            matrix_result[i].append(cell)
    return print_result(matrix_result)


def matrix_multiply_constant(dim_a, matrix_a, constant):
    for i in range(dim_a[0]):
        for j in range(dim_a[1]):
            matrix_a[i][j] *= constant
    return print_result(matrix_a)


def matrix_transpose_main(dim_a, matrix_a):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])
        for j in range(dim_a[1]):
            matrix_result[i].append(matrix_a[j][i])
    return print_result(matrix_result)


def matrix_transpose_side(dim_a, matrix_a):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])
        for j in range(dim_a[1]):
            matrix_result[i].append(matrix_a[(dim_a[0]-j-1)][(dim_a[0]-i-1)])
    return print_result(matrix_result)


def matrix_transpose_vertical(dim_a, matrix_a):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])
        for j in range(dim_a[1]):
            matrix_result[i].append(matrix_a[i][(dim_a[0]-j-1)])
    return print_result(matrix_result)


def matrix_transpose_horizontal(dim_a, matrix_a):
    matrix_result = []
    for i in range(dim_a[0]):
        matrix_result.append([])
        for j in range(dim_a[1]):
            matrix_result[i].append(matrix_a[(dim_a[0]-i-1)][j])
    return print_result(matrix_result)


def determinant_matrix(matrix_a):
    dim = len(matrix_a)
    det = 0

    # base cases
    if dim == 1:
        det = matrix_a[0][0]
    if dim == 2:
        det = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
    # general case
    if dim > 2:
        for j in range(dim):
            matrix_minor = []
            cofactor = (-1) ** j
            a_elem = matrix_a[j][0]
            for i in range(dim):
                if j != i:
                    matrix_minor.insert(i, matrix_a[i][1:])
            det += cofactor * a_elem * determinant_matrix(matrix_minor)
    return det


def matrix_inverse(matrix_a):
    det = determinant_matrix(matrix_a)
    if det == 0:
        return "DET_ZERO"

    dim = len(matrix_a)
    matrix_adj = []
    for k in range(dim):
        matrix_adj.append([])
        for j in range(dim):
            matrix_minor = []
            cofactor = (-1) ** (j + k)
            a_elem = matrix_a[j][k]
            for i in range(dim):
                if i != j:
                    matrix_minor.append(matrix_a[i][0:k] + matrix_a[i][k+1:dim])
            det_minor = cofactor * determinant_matrix(matrix_minor)
            matrix_adj[k].append(det_minor)
            #print(f'k = {k} j = {j} i = {i} a_elem = {a_elem} cofactor = {cofactor} result: {matrix_minor} det_minor {det_minor}')
    matrix_inversed = matrix_multiply_constant([dim, dim], matrix_adj, 1/det)
    return matrix_inversed

def print_result(result):
    if result == "ERROR":
        print("The operation cannot be performed.")
    elif result == "DET_ZERO":
        print("This matrix doesn't have an inverse.")
    else:
        print('The result is:')
        if isinstance(result, float):
            print(result)
        else:
            for row in result:
                print(*[round(x, 4) for x in row])
    print("\n")
    return main('')


def main(self):
    options = ('1. Add matrices',
               '2. Multiply matrix by a constant',
               '3. Multiply matrices',
               '4. Transpose matrix',
               '5. Calculate a determinant',
               '6. Inverse matrix',
               '0. Exit')
    for option in options:
        print(option)

    choice = int(input("Your choice:"))
    if choice == 0:
        exit
    else:
        transpose_choice = 0  # no transpose
        if choice == 4:
            transpose_options = ('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line')
            for option in transpose_options:
                print(option)
            transpose_choice = int(input())
        matrix_input(choice, transpose_choice)


main('')
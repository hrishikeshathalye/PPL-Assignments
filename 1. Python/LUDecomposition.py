#Program to find LU Decomposition of a Matrix by Doolittle method
def LUD(mat, n):
    l = [[0 for i in range(0, n)] for i in range(0, n)]
    u = [[0 for i in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for k in range(i, n):
            add = 0
            for j in range(i):
                add += (l[i][j] * u[j][k]);
            u[i][k] = mat[i][k] - add;

        for k in range(i, n):
            if (i == k):
                l[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (l[k][j] * u[j][i])
                l[k][i] = int((mat[k][i] - sum) / u[i][i])

    print("\nL Matrix:\n")
    for i in range(0, n):
        for j in range(0, n):
            print(l[i][j], end = "\t")
        print("")

    print("\nU Matrix:\n")
    for i in range(0, n):
        for j in range(0, n):
            print(u[i][j], end = "\t")
        print("")

n = int(input("Enter order of matrix :\n"))
matrix = input("Enter Matrix in row major form:\n").split()
matrix = [int(i) for i in matrix]
matrix = [matrix[i:i+n] for i in range(0, n*n, n)]
LUD(matrix, n)

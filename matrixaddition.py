def add_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix 1 values:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter Matrix 2 values:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix3 = add_matrices(matrix1, matrix2)

print("Resultant Matrix:")
for row in matrix3:
    print(row)

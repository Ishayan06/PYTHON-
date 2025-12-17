# Take matrix size
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# Declare matrices
A = []
B = []

print("Enter elements of matrix A:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of matrix B:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

# Result matrices
add = []
sub = []

for i in range(r):
    add_row = []
    sub_row = []
    for j in range(c):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])
    add.append(add_row)
    sub.append(sub_row)

print("Matrix Addition:")
for row in add:
    print(row)

print("Matrix Subtraction:")
for row in sub:
    print(row)

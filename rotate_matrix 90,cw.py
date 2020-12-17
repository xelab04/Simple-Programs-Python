x_matrix = int(input("How 'wide' is the matrix? "))
y_matrix = int(input("How 'tall' is the matrix? "))

matrix_array = []

for i in range(y_matrix):
    line = (input("Line >>> ")).split(",")
    matrix_array.append(line)

new_matrix = [[0 for y in range(y_matrix)] for x in range(x_matrix)]

for y in range(y_matrix):
    for x in range(x_matrix):
        new_matrix[x][y_matrix-1-y] = matrix_array[y][x]

for row in new_matrix:
    print(row)

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i+1} (space-separated values): ").split()
        matrix.append([int(x) for x in row])

    return matrix

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
matrix = get_matrix_from_user()
transposed_matrix = transpose(matrix)
print("Transposed matrix:")
for row in transposed_matrix:
    print(" ".join(str(x) for x in row))

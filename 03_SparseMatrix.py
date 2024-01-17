# A matrix - Sparsely populated
matrix = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 2, 0, 7],
    [0, 0, 0, 5]
]

num_rows = len(matrix)
num_cols = len(matrix[0])

rows = []
cols = []
values = []

rows.append(num_rows)
cols.append(num_cols)
values.append(0)

for i in range(num_rows):
    for j in range(num_cols):
        if matrix[i][j] != 0:
            rows.append(i)
            cols.append(j)
            values.append(matrix[i][j])
            values[0] += 1

print(rows)
print(cols)
print(values)
n = 4
matrix = [[0] * n for _ in range(n)]

# Starting values
val = 1
min_row, max_row = 0, n - 1
min_col, max_col = 0, n - 1
direction = 'right'
while val <= n*n:
    if direction == 'right':
        for i in range(max_row+1):
            if matrix[min_col][min_row+i] != 0:
                break
            matrix[min_col][min_row+i] = val
            val += 1
        min_col += 1
        direction = 'down'
    elif direction == 'left':
        for i in range(max_row+1):
            if matrix[max_col][max_row-i] != 0:
                break
            matrix[max_col][max_row-i] = val
            val += 1
        max_col -= 1
        direction = 'up'
    elif direction == 'down':
        for i in range(max_col):
            if  matrix[min_col+i][max_row] != 0:
                break
            matrix[min_col+i][max_row] = val
            val += 1
        max_row -= 1
        direction = 'left'
    elif direction == 'up':
        for i in range(max_col):
            if matrix[max_col-i][min_row] != 0:
                break
            matrix[max_col-i][min_row] = val
            val += 1
        min_row += 1
        direction = 'right'
print(matrix)
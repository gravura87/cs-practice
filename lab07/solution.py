import numpy as np

def reshape_rows(values, width):
    if len(values) == 0 or width <= 0:
        return []

    if len(values) % width != 0:
        return []

    arr = np.array(values)
    arr = np.round(arr, 6)

    return arr.reshape(-1, width).tolist()

# print(reshape_rows([1, 2, 3, 4, 5, 6], 3))

def block(matrix, rows, columns):
    arr = np.array(matrix)

    if arr.size == 0 or len(rows) == 0 or len(columns) == 0:
        return []

    result = arr[np.ix_(rows, columns)]
    return np.round(result, 6).tolist()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(block(matrix, [2, 0], [1, 2]))

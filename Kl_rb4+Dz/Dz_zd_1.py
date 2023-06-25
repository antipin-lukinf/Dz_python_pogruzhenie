# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4]]

t_matrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]


def transponir_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            t_matrix[j][i] = matrix[i][j]

    return t_matrix


print(transponir_matrix(matrix))

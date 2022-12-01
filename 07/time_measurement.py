import numpy as np
import matr_mul
import time


def matrix_mult(matrix_list):
    res = matrix_list[0]
    try:
        for i in range(1, len(matrix_list)):
            res = np.dot(res, matrix_list[i])
        return res
    except ValueError:
        return 'There are matrices with unsuitable dimensions in your sequence!'


a = np.array([[1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8]
              ])

b = np.array([[1, 0, 1, 2, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 2, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 2, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 2, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 2, 1, 1, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 2, 1, 1, 2, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8],
              [1, 0, 1, 1, 1, 2, 1, 4, 5, 6, 7, 7, 8, 9, 0, 5, 7, 8, 8]
              ])

corr_mat_lst = [a, b] * 12
incorr_mat_lst = [a, b] * 12


print('===python===')
start_time = time.time()
matrix_mult(corr_mat_lst)
end_time = time.time()
print(f"{round(end_time - start_time, 10)} is needed for python in case of correct matrices")
start_time = time.time()
matrix_mult(incorr_mat_lst)
end_time = time.time()
print(f"{round(end_time - start_time, 10)} is needed for python in case of incorrect matrices")
print('===cython===')
start_time = time.time()
matr_mul.matrix_mult(corr_mat_lst)
end_time = time.time()
print(f"{round(end_time - start_time, 10)} is needed for cython in case of correct matrices")
start_time = time.time()
matr_mul.matrix_mult(incorr_mat_lst)
end_time = time.time()
print(f"{round(end_time - start_time, 10)} is needed for cython in case of incorrect matrices")

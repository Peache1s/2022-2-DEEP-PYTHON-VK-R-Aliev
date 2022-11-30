import numpy as np
cimport numpy as np
from numpy cimport ndarray

cpdef matrix_mult(list matrix_list):
    cpdef ndarray res = matrix_list[0]
    try:
        for i in range(1, len(matrix_list)):
            res = np.dot(res, matrix_list[i])
        return res
    except ValueError:
        return 'There are matrices with unsuitable dimensions in your sequence!'

import pytest
import numpy as np
import matr_mul
from time_measurement import matrix_mult


class TestMatrixMultiplication:

    incorrect_data_str = 'There are matrices with unsuitable dimensions in your sequence!'

    @pytest.mark.parametrize('matrix_list, expected', [([np.array([[1, 0], [0, 1]]),
                                                         np.array([[0, 1], [1, 0]])],
                                                        np.array([[0, 1], [1, 0]])),
                                                       ([np.array([[1, 0], [0, 1]]),
                                                         np.array([[0, 1], [1, 0]]),
                                                         np.array([[1, 0], [0, 1]])],
                                                        np.array([[0, 1], [1, 0]])),
                                                       ([np.array([[1, 2], [3, 4]]),
                                                         np.array([[5], [6]]),
                                                         np.array([[6, 7, 8]])],
                                                        np.array([[102, 119, 136],
                                                                  [234, 273, 312]])),

                                                       ])
    def test_cython_and_python_right_case(self, matrix_list, expected):
        res_cython = matr_mul.matrix_mult(matrix_list)
        res_python = matrix_mult(matrix_list)
        bool_eq_cython = res_cython == expected
        bool_eq_python = res_python == expected
        assert bool_eq_cython.all()
        assert bool_eq_python.all()
        assert (res_python == res_cython).all()

    @pytest.mark.parametrize('matrix_list', [([np.array([[0, 1], [1, 0], [1, 1]]),
                                               np.array([[1, 0, 1], [0, 1, 1], [1, 2, 3]])]),
                                             ([np.array([1, 1, 1]), np.array([[2, 2], [3, 3]])])
                                            ])
    def test_cython_and_python_incorrect_case(self, matrix_list):
        res_cython = matr_mul.matrix_mult(matrix_list)
        res_python = matrix_mult(matrix_list)
        assert res_python == res_cython
        assert res_python == self.incorrect_data_str
        assert res_cython == self.incorrect_data_str

    @pytest.mark.parametrize('matrix_list, expected', [([np.array([[1, 0], [0, 1]]), np.array(2)],
                                                        np.array([[2, 0], [0, 2]])),
                                                       ([np.array(2), np.array([[1, 0], [0, 1]])],
                                                         np.array([[2, 0], [0, 2]]))
                                                       ])
    def test_mult_by_scalar(self, matrix_list, expected):
        res_cython = matr_mul.matrix_mult(matrix_list)
        res_python = matrix_mult(matrix_list)
        bool_eq_cython = res_cython == expected
        bool_eq_python = res_python == expected
        assert bool_eq_cython.all()
        assert bool_eq_python.all()
        assert (res_python == res_cython).all()

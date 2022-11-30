import numpy
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('matr_mul.pyx'),
    include_dirs=[numpy.get_include()]
)

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name='fuzzy-byte-search',
    ext_modules=cythonize('ld.pyx')
)

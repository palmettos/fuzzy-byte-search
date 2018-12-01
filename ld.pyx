from __future__ import division
import numpy as np

# An optimized version of Levenshtein Distance in Cython
cpdef double ld(a1, a2):
    cdef char [:] a1v = a1
    cdef char [:] a2v = a2

    cdef int m, n, i, j, cost
    m, n = len(a1), len(a2)

    d = np.zeros((m+1, n+1), dtype=np.double)
    cdef double [:, :] dview = d

    for i in range(1, m+1):
        dview[i, 0] = i
    
    for j in range(1, n+1):
        dview[0, j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if a1v[i-1] == a2v[j-1]:
                cost = 0
            else:
                cost = 1
        
            dview[i, j] = min(
                dview[i-1, j] + 1,
                dview[i, j-1] + 1,
                dview[i-1, j-1] + cost
            )

    return dview[m, n] / max(m, n)

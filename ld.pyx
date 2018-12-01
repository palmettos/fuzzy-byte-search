from __future__ import division
import numpy as np

# An optimized version of Levenshtein Distance in Cython
cpdef double ld(s1, s2):
    cdef int m, n, i, j, cost
    m, n = len(s1), len(s2)

    d = np.zeros((m+1, n+1), dtype=np.double)
    cdef double [:, :] dview = d

    for i in range(1, m+1):
        dview[i, 0] = i
    
    for j in range(1, n+1):
        dview[0, j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
        
            dview[i, j] = min(
                dview[i-1, j] + 1,
                dview[i, j-1] + 1,
                dview[i-1, j-1] + cost
            )

    return dview[m, n] / max(m, n)

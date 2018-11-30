from __future__ import division
from collections import defaultdict

def LD(s1, s2):
    m, n = len(s1), len(s2)
    d = defaultdict(lambda: 0)

    for i in range(1, m+1):
        d[(i, 0)] = i
    
    for j in range(1, n+1):
        d[(0, j)] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
        
            d[(i, j)] = min(
                d[(i-1, j)] + 1,
                d[(i, j-1)] + 1,
                d[(i-1, j-1)] + cost
            )

    return 1 - d[(m, n)] / max(m, n)

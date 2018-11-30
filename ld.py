from collections import defaultdict

def LD(src, dest):
    m, n = len(src), len(dest)
    d = defaultdict(lambda: 0)

    for i in range(1, m+1):
        d[(i, 0)] = i
    
    for j in range(1, n+1):
        d[(0, j)] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if src[i-1] == dest[j-1]:
                cost = 0
            else:
                cost = 1
        
            d[(i, j)] = min(
                d[(i-1, j)] + 1,
                d[(i, j-1)] + 1,
                d[(i-1, j-1)] + cost
            )

    return d[(m, n)]

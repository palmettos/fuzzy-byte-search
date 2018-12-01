from argparse import ArgumentParser, Namespace
import os
from Queue import PriorityQueue
from ld import ld
import time


if __name__ == '__main__':
    parser = ArgumentParser()

    pq = PriorityQueue()
    data = os.urandom(5000)
    s = os.urandom(10)
    win_sz = len(s)

    start = time.time()
    for i in range(0, len(data) - win_sz + 1):
        print i
        segment = data[i:i+win_sz]
        cost = ld(s, segment)
        pq.put((cost, segment))
    end = time.time()
    print end-start, 'seconds to execute'

    print(pq.get())

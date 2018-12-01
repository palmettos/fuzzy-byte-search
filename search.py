from argparse import ArgumentParser, Namespace
import os
from Queue import PriorityQueue
from ld import ld
from itertools import count
import time
import multiprocessing
import numpy as np
import progressbar


N_JOBS = multiprocessing.cpu_count()

data = np.random.randint(256, size=500, dtype=np.uint8)
s = np.random.randint(256, size=2, dtype=np.uint8)
win_sz = len(s)
uid = count()
pq = PriorityQueue()
bar = progressbar.ProgressBar(maxval=len(data)-len(s)+1, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

def compare(s1, s2):
    return ld(s1, s2), s1

def result_available(result):
    bar.update(bar.currval + 1)
    pq.put((result[0], next(uid), result[1]))

if __name__ == '__main__':
    parser = ArgumentParser()

    start = time.time()
    bar.start()
    pool = multiprocessing.Pool(N_JOBS)
    results = [pool.apply_async(compare, args=(data[i:i+win_sz], s), callback=result_available) for i in range(0, len(data)-win_sz+1)]
    pool.close()
    pool.join()
    bar.finish()
    end = time.time()
    print end - start, 'seconds to execute'
    print pq.get()

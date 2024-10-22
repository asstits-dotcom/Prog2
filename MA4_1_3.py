
"""
Solutions to module 4
Review date:
"""

student = "Erik Näsström"
reviewer = ""

import math as m
import random as r
import concurrent.futures as fut
from time import perf_counter as pc
import multiprocessing as mp


# Function to calculate volume of a hypersphere
def sphere_volume(n, d):
    f = lambda x: x**2
    lst = [[f(r.uniform(-1, 1)) for e in range(d)] for i in range(n)]
    inside = list(filter(less_or_eq, lst))
    return (len(inside) / n) * 2 ** d


def less_or_eq(num):
    return sum(num) <= 1

def hypersphere_exact(n, d):
    return (m.pi) ** (d / 2) / (m.gamma(((d / 2) + 1)))

def sphere_volume_parallel1(n, d, num_processes):



    with fut.ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(sphere_volume, n, d) for _ in range(10)]
        results = [f.result() for f in fut.as_completed(futures)]
    # Return the average of the results
    return sum(results) / len(results)


# Parallelizing the data by splitting it across processes (part 2)

def sphere_volume_parallel2(n, d, num_processes):
    n_split = n // num_processes
    with fut.ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(sphere_volume, n_split, d) for _ in range(num_processes)]
        result = [f.result() for f in futures]
    # Return the average of the results
    return sum(result) / len(result)


def main():
    n = 100000
    d = 11
    num_processes = 8

    # Timing non-parallel version (running the function 10 times in sequence)
    start = pc()
    for _ in range(10):
        result = sphere_volume(n, d)
        print(f"Non-parallel result: {result}")
    end = pc()
    print(f"Non-parallel execution time: {end - start} seconds\n")

    # Part 1 -- Timing parallelization of a for loop (10 processes, each with full n)
    start = pc()
    parallel_result1 = sphere_volume_parallel1(n, d, num_processes)
    print(f"Parallel loop result: {parallel_result1}")
    end = pc()
    print(f"Parallel loop execution time: {end - start} seconds\n")

    # Part 2 -- Timing parallelization by splitting the data (10 processes, each with n/10)
    start = pc()
    parallel_result2 = sphere_volume_parallel2(n, d, num_processes)
    print(f"Parallel data split result: {parallel_result2}")
    end = pc()
    print(f"Parallel data split execution time: {end - start} seconds\n")


if __name__ == '__main__':
    main()

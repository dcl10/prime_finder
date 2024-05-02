import time
import prime_finder.finder as finder

if __name__ == "__main__":
    # Time the pure python function
    py_start = time.time()
    primes = finder.find_primes(100)
    py_end = time.time()
    print(f"Python took {(py_end - py_start):4f}s")
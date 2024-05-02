import time
import finder
from prime_finder import find_primes_fast

if __name__ == "__main__":
    # Time the pure python function
    py_start = time.time()
    py_primes = finder.find_primes(100)
    py_time = time.time() - py_start
    print(f"Python took {py_time}s")

    # Time the pure python function
    rs_start = time.time()
    rs_primes = find_primes_fast(100)
    rs_time = time.time() - rs_start
    print(f"Rust took {rs_time}s")

    # Show speed up
    print(f"Rust is {(py_time / rs_time):.2f}x faster")

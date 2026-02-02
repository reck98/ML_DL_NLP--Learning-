import multiprocessing
import math
import time
import sys 
# import threading

sys.set_int_max_str_digits(100000)

numbers = [4000, 5000, 6000, 7000, 8000, 9000, 100]

def squareNumbers(n : int):
    return n**2


def getFact(m : int):
    return math.factorial(m)


if __name__ == '__main__':
    start = time.perf_counter()
    with multiprocessing.Pool() as pools:
        # t1 = threading.Thread(target=getFact, args=(numbers,))
        results = pools.map(getFact, numbers)
        resultsSquare = pools.map(squareNumbers, numbers)
    end = time.perf_counter()
    
    for result in results:
        print(result)
    for result in resultsSquare:
        print(result)
    print(f"Time taken = {end - start}")
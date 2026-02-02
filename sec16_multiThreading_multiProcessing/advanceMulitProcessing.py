from concurrent.futures import ProcessPoolExecutor
import time
import math

def task(n : int) -> float:
    time.sleep(1)
    return (math.sqrt(n))

numbers = [5,6,87,9,4,4,6,6,6,5,5,5,4]


if __name__ == '__main__':
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=12) as executors:
        results = executors.map(task, numbers)


    for i in results:
        print(i)
    
    # results = map(task, numbers)
    # for i in results:
    #     print(i)
        
        
    end = time.perf_counter()
    print(f"Time taken = {end - start}")
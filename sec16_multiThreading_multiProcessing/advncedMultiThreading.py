from concurrent.futures import ThreadPoolExecutor
import math
import time
import os 

def task(n : int) -> float:
    time.sleep(1)
    return (math.sqrt(n))

numbers = [5,6,87,9,4,4,6,6,6,5,5,5,4]


start = time.perf_counter()


with ThreadPoolExecutor(max_workers=60) as executors:
    results = executors.map(task, numbers)

for result in results:
    print(result)

end = time.perf_counter()

print(f"Time taken = {end - start}")


import multiprocessing
import time


NUM = 5

def squareNumbers(n : int) -> None:
    for i in range(n):
        print(f"Square of {i} : {i**2}")
        time.sleep(1)
        
def cubeNumbers(n : int) -> None:
    for i in range(n):
        print(f"Cube of {i} : {i**3}")
        time.sleep(1)
        

## Create 2 processes


p1 = multiprocessing.Process(target=squareNumbers, args=(NUM,))
p2 = multiprocessing.Process(target=cubeNumbers, args=(NUM,))


if __name__ == '__main__':
    startTime = time.perf_counter()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    endTime = time.perf_counter()

    print(f"Time Taken = {endTime - startTime}")




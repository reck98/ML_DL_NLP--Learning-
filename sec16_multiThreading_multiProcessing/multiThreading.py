'''
MultiThreading -> When to use 
    When I/O operations 
    Or bahut jyda kaam karna hai ek saath 
'''

import threading
import time


NUM = 5
STRING = "abcde"
def printNumbers(n : int):
    for i in range(n):
        print(f"Number : {i}")
        time.sleep(1)
        
def printLetters(S : str):
    for i in S:
        print(f"Letter is {i}")
        time.sleep(1)


t1 = threading.Thread(target=printNumbers, args=(NUM,))
t2 = threading.Thread(target=printLetters, args=(STRING,))


startTime = time.perf_counter()
t1.start()
t2.start()

t1.join()
t2.join()
# printNumbers(NUM)
# printLetters(STRING)
endTime = time.perf_counter()

timeTaken = endTime - startTime
print(timeTaken)

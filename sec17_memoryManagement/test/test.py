import time 

startTime = time.perf_counter()
sum = 0
for i in range(1_000_000):
    sum += i
    print(i)
    
print(sum)
endTime = time.perf_counter()

print(f"Time taken = {endTime - startTime}")


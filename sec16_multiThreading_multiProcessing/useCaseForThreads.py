from bs4 import BeautifulSoup
import requests
import threading
from utils.logger import getLogger
import time


logger_ = getLogger(__name__)


urls = [
    'https://code.visualstudio.com/docs/?dv=win64user', 
    'http://kaggle.com/datasets/ajinkyachintawar/employee-attrition-and-retention-analytics-dataset', 
    'https://docs.python.org/3/library/time.html'
]

def fetchContents(url):
    try:
        res = requests.get(url=url)
    except Exception as err:
        logger_.error(f"An error ocuured as {err}")
        
    logger_.info(f"Response received from url -> {url}")
    soup = BeautifulSoup(res.content, 'html.parser')
    print(f"Fetched {len(soup.text)} from the url -> {url}")
    logger_.info(f"Printed from url -> {url}")



threads = []

start = time.perf_counter()
for url in urls:
    thread = threading.Thread(target=fetchContents, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
end = time.perf_counter()

print(f"Time taken = {end - start}")
print("All Done")
    

# start = time.perf_counter()
# for url in urls:
#     fetchContents(url)
# end = time.perf_counter()

# print(f"Time taken = {end - start}")
"""
import time
def fetch_data(url:str):

    print("Fetch data from:",url)
    time.sleep(5)
    print("Data is fetch from",url)
    return "Data from" + url 

urls_list = [
    "https://example.com/api/data1",
    "https://example.com/api/data2",
    "https://example.com/api/data3",
    "https://example.com/api/data4",
    "https://example.com/api/data5"
]

for i in urls_list:
    fetch_data(i)"""


## above is old method --------


import time 
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url:str):
    
    print("getting data from",url)
    time.sleep(5)
    print("Data Fetch from",url)
    return "data from" + url

url_list = ["https://example.com/api/data1",
    "https://example.com/api/data2",
    "https://example.com/api/data3",
    "https://example.com/api/data4",
    "https://example.com/api/data5"]


result = []

with ThreadPoolExecutor(max_workers= len(url_list)) as executor:
    futures = executor.map(fetch_url,url_list)
    result.extend(futures)


print(result)





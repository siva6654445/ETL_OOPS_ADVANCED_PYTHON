"""import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url: str):

    print("Fetching data from:", url)
    time.sleep(5)
    print("Data fetched from:", url)
    return "Data from " + url

urls_list = ["https://example.com/api/data1", 
             "https://example.com/api/data2", 
             "https://example.com/api/data3", 
             "https://example.com/api/data4", 
             "https://example.com/api/data5"]


results = []
with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    futures = executor.map(fetch_data, urls_list)
    results.extend(futures)

print(results)"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URLS = [
    "https://api.example.com/users",
    "https://api.example.com/orders",
    "https://api.example.com/products"
]

def extract(url):
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def extract_parallel(urls):
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(extract, url) for url in urls]

        for future in as_completed(futures):
            try:
                data = future.result()
                results.append(data)
            except Exception as e:
                print("Error:", e)

    return results



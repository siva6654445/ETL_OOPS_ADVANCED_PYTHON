import pandas as pd
class data_ext:

    def __init__(self,path:str):
        self.path = path
    
    def fetch_csv(self):
        df = pd.read_csv(self.path)
        return df

    
    def fetch_json(self):
        df = pd.read_json(self.path)
        print(df.head())

    def fetch_parquet():
        df = pd.read_parquet(self.path)
        print(df.head())

_v1 = data_ext('C:/Users/ACER/Documents/vs_code/coding/spark/sample1.csv')

print(_v1.fetch_csv())

_v2 = data_ext("C:/Users/ACER/Documents/vs_code/coding/spark/e.json")
print(_v2.fetch_json())

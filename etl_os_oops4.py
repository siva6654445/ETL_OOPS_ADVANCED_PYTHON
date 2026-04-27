import pandas as pd
import os
class data_ext:

    def __init__(self,path:str):
        self.path = path
    
    def fetch_data(self):
        file_ext = os.path.splitext(self.path)[1].lower()

        
        if file_ext == '.csv':
            return pd.read_csv(self.path)

        elif file_ext == '.json':
            return pd.read_json(self.path)

        elif file_ext == '.parquet':
            return pd.read_parquet(self.path)

        else:
            raise ValueError(f"Unsupported file format: {file_ext}")

file1 = data_ext('C:/Users/ACER/Documents/vs_code/coding/spark/sample1.csv')
print(file1.fetch_data().head())

file2 = data_ext('C:/Users/ACER/Documents/vs_code/coding/spark/e.json')
print(file2.fetch_data().head())

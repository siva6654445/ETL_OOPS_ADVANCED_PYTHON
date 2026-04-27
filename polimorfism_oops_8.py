"""#Polimorphism & decorators

class api_fetch:


    def fetch(self):
        print(f"fetch data from api")


class dba_fetch:


    def fetch(self):
        print(f"fetch data from dba")


obj1 = dba_fetch()
obj1.fetch()"""


### industry example

from abc import ABC, abstractmethod
import pandas as pd

class Extractor(ABC):

    @abstractmethod
    def extract(self):
        pass


class CSVExtractor(Extractor):
    def __init__(self, path):
        self.path = path

    def extract(self):
        print("Extracting from CSV")
        return pd.read_csv(self.path)


class JSONExtractor(Extractor):
    def __init__(self, path):
        self.path = path

    def extract(self):
        print("Extracting from JSON")
        return pd.read_json(self.path)


class APIExtractor(Extractor):
    def __init__(self, url):
        self.url = url

    def extract(self):
        print("Extracting from API")
        # dummy data instead of real API call
        return pd.DataFrame({"name": ["A", "B"], "age": [25, 30]})

class Transformer:
    def transform(self, df):
        print("Transforming data")
        df.columns = df.columns.str.lower()
        return df
    

class Loader:
    def load(self, df):
        print("Loading data...")
        print(df.head())

def run_etl(extractor: Extractor):
    transformer = Transformer()
    loader = Loader()

    df = extractor.extract()     # <-- polymorphism here
    df = transformer.transform(df)
    loader.load(df)

csv_ext = CSVExtractor(r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv")
json_ext = JSONExtractor(r"C:\Users\ACER\Documents\vs_code\coding\spark\e.json")
api_ext = APIExtractor("https://api.example.com/data")

run_etl(csv_ext)
run_etl(json_ext)
run_etl(api_ext)
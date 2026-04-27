from abc import ABC, abstractmethod
import pandas as pd


# ---------------- Extractor ----------------
class Extractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class CSVExtractor(Extractor):
    def __init__(self, path):
        self.path = path


    def extract(self):
        print("Extracting CSV...")
        df =  pd.read_csv(self.path)
        return df
        
       


# ---------------- Transformer ----------------
class Transformer:
    def transform(self, df):
        print("Transforming data...")
        print(df.head()) 
        return df


# ---------------- Loader ----------------
class CSVLoader:
    def __init__(self, trg_path):
        self.trg_path = trg_path

    def load(self, df):
        print("Loading data...")
        df.to_csv(self.trg_path, index=False)


# ---------------- Pipeline ----------------
def run_etl():
    source_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv"
    target_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\target.csv"

    extractor = CSVExtractor(source_path)
    transformer = Transformer()
    loader = CSVLoader(target_path)

    df = extractor.extract()
    df = transformer.transform(df)
    loader.load(df)

    return df


# Run
result = run_etl()
print(result.head())
# extractors notebook

from abc import ABC, abstractmethod
import pandas as pd

class Extractor(ABC):
    @abstractmethod
    def extract(self):
        pass

class CSVExtractor(Extractor):
    def __init__(self, path, options):
        self.path = path
        self.options = options

    def extract(self):
        return pd.read_csv(**self.options).csv(self.path)
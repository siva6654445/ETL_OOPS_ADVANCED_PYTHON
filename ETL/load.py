class DeltaLoader:
    def __init__(self, path):
        self.path = path

    def load(self, df):
        df.write.mode("overwrite").format("delta").save(self.path)
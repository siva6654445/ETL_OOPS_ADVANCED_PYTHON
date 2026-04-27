%run ./extractors
%run ./transformer
%run ./loader

config = {
    "source": {"type": "csv", "path": "r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv"},
    "read_options": {"header": True, "inferSchema": True},
    "target": {"path": "r"C:\Users\ACER\Documents\vs_code\coding\spark\new"}
}

extractor = CSVExtractor(config["source"]["path"], config["read_options"])
transformer = Transformer()
loader = DeltaLoader(config["target"]["path"])

df = extractor.extract()
df = transformer.transform(df)
loader.load(df)
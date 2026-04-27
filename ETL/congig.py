# Databricks notebook

config = {
    "source": {
        "type": "csv",
        "path": "/Volumes/workspace/default/volume1/titanic.csv"
    },
    "read_options": {
        "header": True,
        "inferSchema": True
    },
    "transform": {
        "drop_nulls": True
    },
    "target": {
        "type": "delta",
        "path": "/Volumes/workspace/default/volume1/output/titanic_delta"
    }
}
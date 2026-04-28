from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

from pyspark.sql import SparkSession
import random

spark = SparkSession.builder \
    .appName("Broadcast Test") \
    .master("local[*]") \
    .getOrCreate()

# Sample values
names = ["Siva", "Karthik", "Adithya", "Rahul", "Priya", "Anjali", "Ravi", "Sneha"]
places = ["Hyderabad", "Mumbai", "Pune", "Bangalore", "Chennai", "Delhi"]

# Generate 1000 rows
data = [(random.choice(names), random.choice(places)) for _ in range(1000)]

schema = ["name", "birth_place"]

df = spark.createDataFrame(data, schema)

df.show(10)
print("Total rows:", df.count())


small_data = [
    ("Siva", "A"),
    ("Karthik", "B"),
    ("Adithya", "C")
]

small_schema = ["name", "category"]

small_df = spark.createDataFrame(small_data, small_schema)


from pyspark.sql.functions import broadcast

joined_df = df.join(
    broadcast(small_df),
    on="name",
    how="left"
)

joined_df.show()
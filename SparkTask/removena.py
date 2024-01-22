from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Remove_Null").getOrCreate()

data = [("A", 1, None), ("B", None, "13"), ("B", 3, "46"), ("D", None, None)]
columns = ["Name", "Value", "id"]

df = spark.createDataFrame(data, schema=columns)
ans = df.na.drop(subset=['id'])
ans.show()

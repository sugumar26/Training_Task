from pyspark.sql import SparkSession
from pyspark.sql.functions import stddev, avg, col, split, explode, length
from pyspark.sql.types import DoubleType
spark = SparkSession.builder.appName('GCSFilesRead').getOrCreate()
key_path = "C:\\Users\\HI\\Downloads\\bustling-syntax-405306-0abc624c5bd9.json"
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", key_path)
bucket_name = "sugumar-spark"
path = f"gs://{bucket_name}/data.csv"
df = spark.read.csv(path, header=True)
df = df.withColumn("ReadingScore", df["ReadingScore"].cast(DoubleType()))
def one():
    result = df.agg(stddev('ReadingScore').alias('std'), avg('ReadingScore').alias('avg'))
    result.show()
def two():
    ans = (
        df.groupBy('EthnicGroup')
          .count()
          .orderBy(col('count').desc())
          .limit(5)
     )
    ans.show()
def three():
    df.describe("ReadingScore").show()
    df.select("ReadingScore").summary("min", "max").show()
    pc = df.approxQuantile("ReadingScore", [0.25, 0.5, 0.75], 0.001)
    print("q25", pc[0])
    print("q75", pc[2])
    # df.select(median("ReadingScore")).show()
def four():
    df2 = df.withColumnRenamed("ParentEduc", "Parent-Education")
    df2.show()
def five():
    df_split = df.withColumn("words", split(col("ParentEduc"), " "))
    df_exploded = df_split.select(explode(col("words")).alias("word"))
    df_word_length = df_exploded.withColumn("word_length", length(col("word")))
    df_word_length.show(truncate=False)
one()
two()
three()
four()
five()

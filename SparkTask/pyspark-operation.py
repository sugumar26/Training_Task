from pyspark.sql import SparkSession
from pyspark.sql.functions import stddev, avg, col ,split ,explode ,length , median
import numpy as np
import pandas as pd
spark = SparkSession.builder.appName("example").getOrCreate()
df = spark.read.csv('data.csv', header=True, inferSchema=True)
def one():
    result = df.agg(stddev('ReadingScore').alias('std'), avg('ReadingScore').alias('avg'))
    result.show()
one()  
def two():
    ans = (
    df.groupBy('EthnicGroup')
      .count()
      .orderBy(col('count').desc())
      .limit(5)
     )
    ans.show()  
two() 
def three():
    df.describe("ReadingScore").show()
    df.select("ReadingScore").summary("min","max").show()
    pc=df.approxQuantile("ReadingScore", [0.25, 0.5, 0.75],0.001)
    print("q25",pc[0])
    print("q75",pc[2])
    df.select(median("ReadingScore")).show()
three()    
def four():
    df2=df.withColumnRenamed("ParentEduc", "Parent-Education")
    df2.show()
four()  
def five():
    df_split = df.withColumn("words", split(col("ParentEduc"), " "))
    df_exploded = df_split.select(explode(col("words")).alias("word"))
    df_word_length = df_exploded.withColumn("word_length", length(col("word")))
    df_word_length.show(truncate=False)

five()


    


      

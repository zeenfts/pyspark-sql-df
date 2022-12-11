import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Hello World").getOrCreate()

parquet_file = sys.argv[1]

# Read file
df = spark.read.parquet(parquet_file)

df.printSchema()
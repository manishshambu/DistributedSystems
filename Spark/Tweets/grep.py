from pyspark.context import SparkContext, SparkConf
import time
from pyspark import sql
from pyspark.sql import SparkSession

startTime = time.time()
spark = SparkSession\
    .builder\
        .appName("PythonTweets")\
        .getOrCreate()


lines = spark.read.text("tweets.txt")
linesWithSpark = lines.filter(lines.value.contains("Boulder"))
print("Total words ------ "+str(lines.filter(lines.value.contains("Boulder")).count()))
print("--- %s seconds ---" % (time.time() - startTime))

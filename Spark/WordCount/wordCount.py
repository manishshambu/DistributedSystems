from pyspark.context import SparkContext
sc = SparkContext.getOrCreate()
lines = sc.textFile("README.md")
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).map(lambda word: (word, 1))
counts.saveAsTextFile("README.count")
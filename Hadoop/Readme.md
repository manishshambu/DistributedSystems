Word Count algorithm
Delete all the output folders
hdfs dfs -rm output/* and hdfs dfs -rmdir output
yarn jar ~/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount clickStream/* output
output is  present in output directory of hdfs.


Page Rank algorithm
cd into pageRank/googlepagerank/mapreduce job folder
Run ./run_mapreduce.sh job
output is printed in results folder

Grep Tweets
hdfs dfs -rm output1/* and hdfs dfs -rmdir output1
yarn jar ~/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar grep "tweets/*" output1 "Boulder"
Output is present in output1 directory of hdfs

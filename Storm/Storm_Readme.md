Firstly, to compile the source jave code

run "mvn compile package" in storm/examples/storm-starter directory


To run the page rank algorithm
Go to storm folder in home directory
bin/storm jar /home/ubuntu/apache-storm-0.9.5/examples/storm-starter/target/storm-starter-0.9.5.jar storm.starter.PageRankMainTopology


To run the word count algorithm
Go to storm folder in home directory
bin/storm jar /home/ubuntu/apache-storm-0.9.5/examples/storm-starter/target/storm-starter-0.9.5.jar storm.starter.WordCountTopologyFile

To run the twitter algorithm 
Go to storm folder in home directory
bin/storm jar /home/ubuntu/apache-storm-0.9.5/examples/storm-starter/target/storm-starter-0.9.5.jar storm.starter.TwitterTopology

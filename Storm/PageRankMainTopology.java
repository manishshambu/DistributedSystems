package storm.starter;


import backtype.storm.Config;
import backtype.storm.LocalCluster;
import backtype.storm.topology.BoltDeclarer;
import backtype.storm.topology.TopologyBuilder;
import storm.starter.spout.PageRankSpout;
import storm.starter.bolt.PageRankFixPoint;
import storm.starter.bolt.PageRankUpdate;
import storm.starter.bolt.PageRankSink;

public class PageRankMainTopology {

	public static void main(String[] args) {
		TopologyBuilder builder = new TopologyBuilder();
		builder.setSpout("spout", new PageRankSpout());
		BoltDeclarer fixpoint = builder.setBolt("fixpoint", new PageRankFixPoint());
		BoltDeclarer updater = builder.setBolt("updater", new PageRankUpdate(), 1);
		BoltDeclarer sink = builder.setBolt("sink", new PageRankSink());
		/////////////////////////////////
		fixpoint.globalGrouping("spout");
		/////////////////////////////////
		updater.globalGrouping("fixpoint", "toupdater");
		fixpoint.globalGrouping("updater");
		/////////////////////////////////
		sink.globalGrouping("fixpoint", "tosink");
		
		Config conf = new Config();
		conf.setDebug(false);
		conf.setMaxTaskParallelism(20);
		LocalCluster cluster = new LocalCluster();
		cluster.submitTopology("scc", conf, builder.createTopology());
	}
}

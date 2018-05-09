package storm.starter.bolt;

import java.util.Map;

import backtype.storm.task.OutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseRichBolt;
import backtype.storm.tuple.Tuple;

public class PageRankSink extends BaseRichBolt {

	@Override
	public void prepare(Map stormConf, TopologyContext context,
			OutputCollector collector) {
		
	}

	@Override
	public void execute(Tuple input) {
		// TODO Auto-generated method stub
		int node = input.getIntegerByField("node");
		Double pagerank = input.getDoubleByField("result");
		System.out.println("received by sink: node="+node+", value="+pagerank);
	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		
	}

}

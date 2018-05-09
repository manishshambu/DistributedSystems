/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package storm.starter.spout;

import backtype.storm.spout.SpoutOutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseRichSpout;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Values;
import backtype.storm.utils.Utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.Map;
import java.util.Random;
import java.util.concurrent.atomic.AtomicLong;

public class TwitterSpout extends BaseRichSpout {
  SpoutOutputCollector _collector;
  Random _rand;
  String fileName;
  BufferedReader reader; 
  AtomicLong linesRead;  

  @Override
  public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
    _collector = collector;
    _rand = new Random();
    linesRead = new AtomicLong(0);
    try 
    {
      //reader = new BufferedReader(new FileReader("/home/ubuntu/twitter.txt"));
      reader = new BufferedReader(new FileReader("/home/ubuntu/tweets/tweets.txt"));
    }
    catch (Exception e)
    {
      throw new RuntimeException(e);
    }	
    	
  }

  @Override
  public void nextTuple() {
    
    //Utils.sleep(100);
    try
    {
       String line = reader.readLine();
       if (line != null)
       { 
         long id = linesRead.incrementAndGet();
         _collector.emit(new Values(line), id); 
       }
       else
       {
         System.out.println("Finished reading file, " + linesRead.get() + " lines read");
         Thread.sleep(10000);
       }
    }
    catch (Exception e)	
    {
       e.printStackTrace();
    } 

    /*
    String[] sentences = new String[]{ "the cow jumped over the moon", "an apple a day keeps the doctor away",
        "four score and seven years ago", "snow white and the seven dwarfs", "i am at two with nature" };
    String sentence = sentences[_rand.nextInt(sentences.length)];
    _collector.emit(new Values(sentence));
   */
  
 }

  @Override
  public void ack(Object id) {
  }

  @Override
  public void fail(Object id) {
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    declarer.declare(new Fields("word"));
  }

}

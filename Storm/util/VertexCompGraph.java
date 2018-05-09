
package storm.starter.util;

import java.util.HashMap;
import java.util.Map;

public class VertexCompGraph<T>{
	public Map<Integer, T> _vertices=null;
	
	public VertexCompGraph(){
		_vertices=new HashMap<Integer, T>();
	}
	
	public void setValue(int node, T value){
		_vertices.put(node, value);
	}
}

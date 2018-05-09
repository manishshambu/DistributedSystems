
package storm.starter.util;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class StaticDirectedGraph {
	//node -> target neighbors
	public Map<Integer, Set<Integer>> _toVertices = null;
	//node -> source neighbors
	public Map<Integer, Set<Integer>> _fromVertices = null;
	
	public StaticDirectedGraph() {
		_toVertices = new HashMap<Integer, Set<Integer>>();
		_fromVertices = new HashMap<Integer, Set<Integer>>();
	}

	public void insertEdge(int sourceNode, int targetNode) {
		if (!_toVertices.containsKey(sourceNode)) {
			_toVertices.put(sourceNode, new HashSet<Integer>());
		}
		_toVertices.get(sourceNode).add(targetNode);
		if (!_fromVertices.containsKey(targetNode)){
			_fromVertices.put(targetNode, new HashSet<Integer>());
		}
		_fromVertices.get(targetNode).add(sourceNode);
	}
}


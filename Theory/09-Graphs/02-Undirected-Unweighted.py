'''
This is the simple code to build the graphs.
Let's do this. We are never worried about anything.
'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.numNodes = 0

        # index -> [other index-1, other index-2]
        self.adjacentList = {}

    def addVertex(self, value):
        if self.adjacentList.get(value, None) is None:
            self.adjacentList[value] = []
            self.numNodes += 1
            
    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
        else:
            raise NotImplementedError("Either `{}` or `{}` not found in the graph. Consider adding them before connecting them.")
        
    def showConnections(self):
        for key in self.adjacentList.keys():
            print("[{}] --> {}".format(key, 
                                         self.adjacentList[key]))
            


myGraph = Graph();
myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');
myGraph.addEdge('3', '1'); 
myGraph.addEdge('3', '4'); 
myGraph.addEdge('4', '2'); 
myGraph.addEdge('4', '5'); 
myGraph.addEdge('1', '2'); 
myGraph.addEdge('1', '0'); 
myGraph.addEdge('0', '2'); 
myGraph.addEdge('6', '5');

myGraph.showConnections(); 

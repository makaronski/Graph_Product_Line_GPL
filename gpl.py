#
# My Graph Library implementation in Python
#
# Petar Petrov h11729352@s.wu.ac.at
#
# How to run: `python gpl.py`
#

#
# Prerequisites
#

import unittest

class Base:
  #
  # Begin of my implementation
  # ---------------%<------------------
  #
  # (Pls. enter your code here.)
    class Graph:
        def __init__(self,directed = 0):
            self._edges = []
            self._nodes = {}
            self.node_count = 0
            self._edgescheck = []
            #0 for Undirected, 1 for Directed
            self.directed = directed

        def add(self,node1,node2):


            #Check if edge already exists
            if ([node1.getNode,node2.getNode] not in self._edgescheck
            and [node2.getNode,node1.getNode] not in self._edgescheck):
                #Append new edge
                newedge = Base.Edge(node1.getNode, node2.getNode)
                self._edges.append(newedge)
                self._edgescheck.append([newedge.getA(),newedge.getB()])

            #Add Nodes to the dict:
            if node1.nodename not in self._nodes:
                self._nodes[node1.nodename] = self.node_count
                self.node_count += 1
            if node2.nodename not in self._nodes:
                self._nodes[node2.nodename] = self.node_count
                self.node_count += 1


    class Node:
        counter = 0
        def __init__(self):
            self.__class__.counter += 1
            self.nodename = 'node'+ str(self.__class__.counter)

        @property
        def getNode(self):
            return self

        def getNodeName(self):
            return self.nodename


    class Edge:
        def __init__(self,a,b,weight=1):
            self._a = a
            self._b = b
            self._weight = weight

        def getA(self):
            return self._a
        def getB(self):
            return self._b
        def getWeight(self):
            return self._weight


    class Graph_Pretty(Graph):
        def __init__(self,directed=0):
            super().__init__()
            self.directed = directed

        def prettyprint(self):
            if self.directed == 0:
                outputstring = 'graph g{ \nnode[label=""];\n\n'
                for edge in self._edges:
                    outputstring += (str(edge.getA().getNodeName()) +" -- "+str(edge.getB().getNodeName()) + '\n')
                outputstring += "}"
                return outputstring
            else:
                outputstring = 'digraph g{ \nnode[label=""];\n\n'
                for edge in self._edges:
                    outputstring += (str(edge.getA().getNodeName()) + " -> " + str(edge.getB().getNodeName()) + '\n')
                outputstring += "}"
                return outputstring

    class Weighted_Graph(Graph):
        def __init__(self):
            super().__init__()

        def add(self, node1, node2, weight=1):
            if weight < 0:
                print("Please enter a non-negative weight")
            elif([node1.nodename, node2.nodename] not in self._edges
            or [node2.nodename, node1.nodename] not in self._edges):
                #Append new edge
                newedge = Base.Edge(node1.getNode, node2.getNode,weight=weight)
                self._edges.append(newedge)

            if node1.nodename not in self._nodes:
                self._nodes[node1.nodename] = self.node_count
                self.node_count += 1
            if node2.nodename not in self._nodes:
                self._nodes[node2.nodename] = self.node_count
                self.node_count += 1

    class Weighted_Graph_Pretty(Weighted_Graph):
        def __init__(self,directed=0):
            super().__init__()
            self.directed =directed

        def prettyprint(self):
            if self.directed == 0:
                outputstring = 'graph g{ \nnode[label=""];\n\n'
                for edge in self._edges:
                    outputstring += (str(edge.getA().getNodeName())+" -- "+str(edge.getB().getNodeName())
                                     + '[label=' +str(edge._weight) + ']\n')
                outputstring += "}"
                return outputstring
            else:
                outputstring = 'digraph g{ \nnode[label=""];\n\n'
                for edge in self._edges:
                    outputstring += (str(edge.getA().getNodeName())+" -> "+str(edge.getB().getNodeName())
                                     + '[label=' +str(edge._weight) + ']\n')
                outputstring += "}"
                return outputstring





class NeighbourList:

    class Graph(Base.Graph):
        def __init__(self):
            super().__init__()
            self._nodes = []

        def add(self,node1,node2):
            if node1 not in self._nodes:
                self._nodes.append(node1.getNode)
            if node2 not in self._nodes:
                self._nodes.append(node2.getNode)

            if (node1.checkNeighbour(node2) != 1 and node2.checkNeighbour(node1) != 1):
                node1.addNeighbour(node2)

    class Graph_Pretty(Graph):
        def __init__(self,directed=0):
            super().__init__()
            self.directed = directed

        def prettyprint(self):
            if self.directed == 0:
                outputstring = 'graph g{ \nnode[label=""];\n\n'
                for node in self._nodes:
                    for neighbour in node.neighbours:
                        outputstring += (node.getNodeName() + " -- " + neighbour.getNodeName() + '\n')
                outputstring += "}"
                return outputstring
            else:
                outputstring = 'digraph g{ \nnode[label=""];\n\n'
                for node in self._nodes:
                    for neighbour in node.neighbours:
                        outputstring += (node.getNodeName() + " -> " + neighbour.getNodeName() + '\n')
                outputstring += "}"
                return outputstring

    class Neighbour():
        def __init__(self,opposite,weight=1):
            self.opposite = opposite
            self.weight = weight

        def getOpposite(self):
            return self.opposite

        def getWeight(self):
            return self.weight

    class Node ():
        counter = 0

        def __init__(self):
            self.__class__.counter += 1
            self.nodename = 'node' + str(self.__class__.counter)
            self.neighbours = []
            self.weight = 1
            #self.neighbour = NeighbourList.Neighbour(self.getNode)

        @property
        def getNode(self):
            return self

        def getNodeName(self):
            return self.nodename

        def addNeighbour(self,neighbour,weight=1):
            opposite = NeighbourList.Neighbour(neighbour,weight=weight)
            self.neighbours.append(opposite)



        def getWeight(self):
            return self.weight

        def checkNeighbour(self,neighbour):
            for node in self.neighbours:
                if neighbour.getNodeName() == node.getOpposite().getNodeName():
                    return 1

        def getNeighbours(self):
            return self.neighbours


    class Weighted_Graph(Graph):
        def __init__(self,directed=0):
            super().__init__()
            self._nodes = []
            self.directed = directed

        def add(self,node1,node2,weight=1):
            if weight < 0:
                print("Please enter a non-negative weight")
            else:
                if node1 not in self._nodes:
                    self._nodes.append(node1.getNode)
                if node2 not in self._nodes:
                    self._nodes.append(node2.getNode)
                if (node1.checkNeighbour(node2) != 1 and node2.checkNeighbour(node1) != 1):
                    node1.addNeighbour(node2,weight=weight)


    class Weighted_Graph_Pretty(Weighted_Graph):
        def __init__(self,directed=0):
            super().__init__()
            self._nodes =[]
            self.directed = directed

        def prettyprint(self):
            if self.directed == 0:
                outputstring = 'graph g{ \nnode[label=""];\n\n'
                for node in self._nodes:
                    for neighbour in node.neighbours:
                        outputstring += (node.getNodeName() + " -- " + neighbour.getOpposite().getNodeName()
                                         + '[label=' +str(neighbour.getWeight()) + ']\n')
                outputstring += "}"
                return outputstring
            else:
                outputstring = 'digraph g{ \nnode[label=""];\n\n'
                for node in self._nodes:
                    for neighbour in node.neighbours:
                        outputstring += (node.getNodeName() + " -> " + neighbour.getOpposite().getNodeName()
                                         + '[label=' + str(neighbour.getWeight()) + ']\n')
                outputstring += "}"
                return outputstring







 # ---------------%<------------------
 # End of my implementation
 #


#
# Test suite
#


class Test(unittest.TestCase):
    def test_acceptance(self):
        #
        # Acceptance tests
        #
        self.assertEqual(hasattr(Base,"Graph") and isinstance(Base.Graph, type), True)
        self.assertEqual(hasattr(Base,"Edge") and isinstance(Base.Edge, type), True)
        self.assertEqual(hasattr(Base,"Node") and isinstance(Base.Node, type), True)
        self.assertEqual(hasattr(Base.Graph, "add") and callable(Base.Graph.add), True)

    def test_my(self):
        #
        # Begin of my tests
        # See also https://docs.python.org/3.4/library/unittest.html
        # ---------------%<------------------
        # (Pls. enter your additional tests here.)

        #Test 1 - Create Graph from Assignment and check for the exact number of nodes and edges
        graph = Base.Graph()
        n1,n2,n3,n4,n5,n6,n7,n8 = Base.Node(),Base.Node(),Base.Node(),Base.Node(),Base.Node(),Base.Node(),Base.Node(),Base.Node()
        graph.add(n1,n2)
        graph.add(n1,n3)
        graph.add(n1,n4)
        graph.add(n1,n5)
        graph.add(n5,n6)
        graph.add(n5,n7)
        graph.add(n5,n8)
        print ("The number of edges in the graph is : "+ str(len(graph._edges)))
        print ("The number of nodes in the graph is : "+ str(len(graph._nodes)))
        self.assertEqual(len(graph._edges)==7,True)
        self.assertEqual(len(graph._nodes)==8,True)

        #Test 2 - Pretty Print
        g2 = Base.Graph_Pretty()
        g2.add(n1,n2)
        g2.add(n1,n3)
        g2.add(n1,n4)
        g2.add(n1,n5)
        g2.add(n5,n6)
        g2.add(n5,n7)
        g2.add(n5,n8)
        print(g2.prettyprint())
        self.assertEqual(hasattr(Base, "Graph_Pretty") and isinstance(Base.Graph, type), True)


        #Test 3 - Compare with required output:
        checkstring = 'graph g{ \nnode[label=""];\n\nnode1 -- node2\nnode1 -- node3\nnode1 -- node4\nnode1 -- node5\nnode5 -- node6\nnode5 -- node7\nnode5 -- node8\n}'
        self.assertEqual(checkstring,str(Base.Graph_Pretty.prettyprint(g2)), True)
        pass


        #Test 4 = Edge List Weighted Undirected Graph
        wgraph = Base.Weighted_Graph_Pretty()
        wgraph.add(n1,n2,1)
        wgraph.add(n1,n3,4)
        wgraph.add(n1,n4,5)
        wgraph.add(n1,n5,1)
        wgraph.add(n5,n6,10)
        wgraph.add(n5,n7,2)
        wgraph.add(n5,n8,7)
        print(wgraph.prettyprint())

        ###NeighbourList Undirected Weighted:
        nn1, nn2, nn3, nn4, nn5, nn6, nn7, nn8 = NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node(), NeighbourList.Node()
        nwdgraph = NeighbourList.Weighted_Graph_Pretty(directed=0)
        nwdgraph.add(nn1, nn2)
        nwdgraph.add(nn1, nn3,4)
        nwdgraph.add(nn1, nn4,5)
        nwdgraph.add(nn1, nn5)
        nwdgraph.add(nn5, nn6,10)
        nwdgraph.add(nn5, nn7,2)
        nwdgraph.add(nn5, nn8,7)
        nwdgraph.add(nn5, nn8)
        nwdgraph.add(nn8, nn5)
        print(nwdgraph.prettyprint())



        #Test 5 = Edge List Weighted Directed Graph
        wdgraph = Base.Weighted_Graph_Pretty(directed=1)
        wdgraph.add(n1,n2,1)
        wdgraph.add(n2,n3,4)
        wdgraph.add(n2,n4,5)
        wdgraph.add(n2,n5,1)
        wdgraph.add(n6,n5,10)
        wdgraph.add(n5,n7,2)
        wdgraph.add(n5,n8,7)
        print(wdgraph.prettyprint())


        ###NeighbourList Directed Weighted:
        nn1,nn2,nn3,nn4,nn5,nn6,nn7,nn8 = NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node(),NeighbourList.Node()
        nwdgraph = NeighbourList.Weighted_Graph_Pretty(directed=1)
        nwdgraph.add(nn1,nn2)
        nwdgraph.add(nn2,nn3,4)
        nwdgraph.add(nn2,nn4,5)
        nwdgraph.add(nn2,nn5)
        nwdgraph.add(nn6,nn5,10)
        nwdgraph.add(nn5,nn7,2)
        nwdgraph.add(nn5,nn8,7)
        print(nwdgraph.prettyprint())



        # ---------------%<------------------
        # End of my tests
        #

if __name__ == '__main__':
    unittest.main()




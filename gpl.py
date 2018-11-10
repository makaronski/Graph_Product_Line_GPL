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
        def __init__(self,edges=[],nodes={},node_count=0):
            self._edges = edges
            self._nodes = nodes
            self.node_count = node_count

        def add(self,*args):
            for edge in args:
                #Check if edge already exists
                if ([args[0].nodename,args[1].nodename] not in self._edges 
                and [args[1].nodename,args[0].nodename] not in self._edges): 
                    #Append new edge
                    newedge = Base.Edge(args[0].nodename,args[1].nodename)
                    self._edges.append([newedge.getA(),newedge.getB()])
            
            #Add Nodes to the dict:
            if args[0].nodename not in self._nodes:
                self._nodes[args[0].nodename] = self.node_count
                self.node_count += 1
            if args [1].nodename not in self._nodes:
                self._nodes[args[1].nodename] = self.node_count
                self.node_count += 1
                

    class Node:
        counter = 0
        def __init__(self):
            self.__class__.counter += 1
            self.nodename = 'node'+ str(self.__class__.counter)
           

    class Edge:
        def __init__(self,a,b):
            self._a = a
            self._b = b
        def getA(self):
            return self._a
        def getB(self):
            return self._b
       
def prettyprint(graph):
    outputstring = 'graph g{ \nnode[label=""];\n\n'
    for edge in graph._edges:
        outputstring += (" -- ".join(edge)+'\n')
    outputstring += "}"
    return outputstring
  # 
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
        print(prettyprint(graph))
      
        #Test 3 - Compare with required output:
        checkstring = 'graph g{ \nnode[label=""];\n\nnode1 -- node2\nnode1 -- node3\nnode1 -- node4\nnode1 -- node5\nnode5 -- node6\nnode5 -- node7\nnode5 -- node8\n}'
        self.assertEqual(checkstring,str(prettyprint(graph)), True)
        pass
  
        # ---------------%<------------------
        # End of my tests
        #    

if __name__ == '__main__':
    unittest.main()
    

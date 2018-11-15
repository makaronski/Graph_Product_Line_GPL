# Graph_Product_Line_GPL
* Implementation of a library to create graphs using python and tcl.

* https://dreampuf.github.io/GraphvizOnline/ to visualize the graphs

## Step 1
### Implementing a Graph Library with Variability

The objective of this home assignment is to design and to implement a library offering graph data structures and graph algorithms in two out of four different scripting languages: JavaScript, Ruby, Python, and NX/Tcl.

The library is required to support different configurations of data structures and algorithms for representing and computing on graphs, that is, their variability, to better serve different design, implementation, and analysis tasks on graphs. Therefore, we refer to this graph library as a Graph Product Line (GPL).

### Feature Diagram:
  ![feature_diagram](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/fm.png)
  
 Implement a Graph Product Line which supports two different configurations, as shown in the feature diagram. The feature Base refers to the core structure and core behaviour of graph data structures. The feature DOT provides for serializing a graph structure into a graph visualization definition expressed in the DOT language  for pretty printing and rendering graphs.
  
### Class Diagram: 

 Implement the Base feature by sticking a closely as possible to the following UML models, one for the Base structure (class diagram), one for a particular behavioural detail (sequence diagram).
 
![class_diagram](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/cd.png)

 
![sequence_diagram](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/sd.png)

### Implementing DOT pretty printer

There are no specific structural or behavioural models as prescriptive descriptions of your DOT implementation. Pretty printing involves, once a graph structure has been defined, to traverse the graph structure in an adequate manner and to serialize this traversal into a valid specification expressed in the DOT language  to standard output (stdout).

Make sure, for some graph structure, that the resulting visualization realizes as follows:

![graph1](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/gv.png)

* Test 2 and 3 test for this specific graph.

## Step 2

### From Stage 1 to Stage 2
Study the evolved feature diagram below carefully!

 ![feature_diagram2](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/fm2.png)
 
At stage 2, your are expected to realise the following additional features and variabilities:

* Neighbour-list representation: At stage 1, graph objects maintained the data on their connectedness in terms of so-called edge lists (i.e. vectors or lists of edge objects) only. Edge lists should be preserved at stage 2. Alternatively, a neighbour representation must be introduced. Future clients of your graph library will be able to choose whether to use graphs based on edge or neighbour lists.
* Directedness: At stage 1, graphs were purely undirected. Starting with stage 2, your graph library must be enabled to represent directed ("digraphs") and undirected graphs ("undirgraphs").
* Weight: Annotating edges is an important representational feature of graphs (e.g., to encode link costs in routing graphs). All graph kinds in your GPL should optionally support managing weights as edge annotations.

### Neighbour-list representation

There are several representation choices for graphs, e.g.: edge lists, adjacency matrices, and adjacency lists. They can also be blended. The actual choice of a particular representation will depend on the usage scenario of the graph (e.g., the kind of graph-analysis algorithm to be executed) and the conditions of the represented graph (e.g., the sparseness of a graph). This choice is left to future users of your GPL, that is, developers integrating with your graph library being aware of the usage scenario and graph conditions.

At stage 2, you will extend your graph library to offer two options to developers:
* Edge lists: This is what you basically implemented at stage 1;
* Neighbour lists;

A neighbour list is a variant of the adjacency-list representation. See also the class-diagram fragment below:

* A Graph object maintains a list of Node objects.
* A Node object maintains a list of Neighbour objects.
* A Neighbour object maintains a reference to a Node object, which represents the opposite end of an edge.

This representation choice has a number of important consequences. Most importantly:

* It does not require an explicit Edge entity in contrast to the edge-list representation.
* Graph::add(): The internal behavior of the "add" operation is substantially different using neighbour lists.

![class_diagram2](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/cd2.png)

### Undirected and directed graphs

It is needless to say that digraphs and undigraphs are needed both to represent (i.e. to "model") different domains. At this stage, extend your graph library and its concepts (Graph, Edge, Node, Neighbour) in a way that both types of graphs can be created and managed.

### Edge weights

Realise support for edge annotations ("weights") which fulfil the following requirements:

* Edges can be weighted with non-negative numbers or unweighted.
* Weights can be attached to directed and undirected edges alike.
* A weighted graph (digraph, undigraph) is a graph, in which all edges carry weights.

See below for a unidgraph and a digraph, respectively, with annotated edges:

![dot1](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/dot1.png)
![dot2](https://github.com/makaronski/Graph_Product_Line_GPL/blob/master/images/dot2.png)

* Tests 8 and 9 check for the above graphs respectively

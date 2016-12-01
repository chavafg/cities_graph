#!/usr/bin/python
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import shortest_path
from networkx import draw, Graph
import networkx as nx 
import matplotlib.pyplot as plt
from pylab import show
import numpy
import re

a = [0, 289, 549, 195, 331, 206, 220, 233, 333, 383] # GDL
b = [0, 0, 310, 448, 0, 0, 314, 197, 336, 330]     # MORELIA
c = [0, 0, 0, 0, 0, 0, 574, 408, 418, 238]        # CDMX
d = [0, 0, 0, 0, 378, 0, 0, 0, 0, 0]             # COLIMA
e = [0, 0, 0, 0, 0, 162, 0, 0, 0, 0]            # VALLARTA
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]              # TEPIC
g = [0, 0, 0, 0, 0, 0, 0, 124, 166, 0]         # AGS
h = [0, 0, 0, 0, 0, 0, 0, 0, 181, 168]       # LEON
i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 212]       # SLP
j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]         # QUERETARO

X = csr_matrix([a, b, c, d, e, f, g, h, i, j])

print X
print X.toarray().astype(int)

str_repr= str(X)
mylist = []

def getTuples( mymatrix ):
    str_repr= str( mymatrix )
    mylist = []
    for line in str_repr.splitlines():
        m = re.search('\((.+?)\)', line)
        mytuple = m.group(1)
    
        a= int(mytuple.split(', ', 1)[0])
        b= int(mytuple.split(', ', 1)[1])
        t = ()
        t = t + (a,)
        t = t + (b,)
        mylist.append(t)
    return mylist


Tcsr = minimum_spanning_tree(X)
print Tcsr.toarray().astype(int)
print Tcsr

sp = shortest_path(X, method='FW', directed=False)
print sp

allConnections = getTuples( X )
g = nx.Graph()
g.add_edges_from(allConnections)
pos=nx.spring_layout(g) 
nx.draw_networkx_nodes(g,pos,node_size=700, node_color="gray")
nx.draw_networkx_edges(g,pos,width=3,alpha=0.7,edge_color='red')
nx.draw_networkx_labels(g,pos,font_size=10)
print(nx.shortest_path(g,source=6,target=2))
#nx.draw_networkx_labels(g,pos,font_size=10,font_family='sans-serif')

#draw(g)
#draw_networkx_edges_labels(g,pos=nx.spring_layout(G))

mst = getTuples(Tcsr)
g2 = Graph()
g2.add_edges_from(mst)
draw(g2)

show()

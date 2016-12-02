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



def get_sp_tuple( myarray ):
    #print len(myarray)
    #print myarray[0]
    #print myarray[1]
    mylist = []
    for i in range(len(myarray)-1):
        #print i
        #print myarray[i] 
        a = myarray[i]
        b = myarray[i+1]
        t = ()
        t = t + (a,)
        t = t + (b,)
        mylist.append(t)
    return mylist


mst = getTuples(X)
g = nx.Graph()
g.add_edges_from(mst)
pos=nx.spring_layout(g)
sp = nx.shortest_path(g, source=3, target=9)
sp_tuple = get_sp_tuple(sp)
print sp_tuple
nx.draw_networkx_nodes(g,pos,node_size=700, node_color="gray")
nx.draw_networkx_edges(g,pos,width=3,alpha=0.4,edge_color='red')
nx.draw_networkx_labels(g,pos,font_size=10)

g2 = nx.Graph()
g2.add_edges_from(sp_tuple)
nx.draw_networkx_nodes(g2,pos,node_size=700, node_color="gray")
nx.draw_networkx_edges(g2,pos,width=3,alpha=0.7,edge_color='green')
nx.draw_networkx_labels(g2,pos,font_size=10)


show()

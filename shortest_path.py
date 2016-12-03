#!/usr/bin/python
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import shortest_path
from networkx import draw, Graph
import networkx as nx 
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import numpy
import re

a = [0, 289, 549, 195, 0, 206, 220, 233, 333, 0] # GDL
b = [0, 0, 310, 448, 0, 0, 314, 0, 336, 330]     # MORELIA
c = [0, 0, 0, 0, 0, 0, 574, 408, 418, 238]       # CDMX
d = [0, 0, 0, 0, 378, 0, 0, 0, 0, 0]             # COLIMA
e = [0, 0, 0, 0, 0, 162, 0, 0, 0, 0]             # VALLARTA
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]               # TEPIC
g = [0, 0, 0, 0, 0, 0, 0, 124, 166, 0]           # AGS
h = [0, 0, 0, 0, 0, 0, 0, 0, 181, 168]           # LEON
i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 212]             # SLP
j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]               # QUERETARO

X = csr_matrix([a, b, c, d, e, f, g, h, i, j])
fixed_positions = {0:(0,0),1:(3,2),2:(7,-1), 
                    3:(1,-3),4:(-3,-2),5:(-6,1),
                    6:(-3,5),7:(1,6),8:(3,9),9:(6,5)}

# Get tuples to draw all conections
def getTuples( mymatrix ):
    str_repr= str( mymatrix )
    mylist = []
    for line in str_repr.splitlines():
        m = re.search('\((.+?)\)', line)
        mytuple = m.group(1)
        t = ()
        t = t + (int(mytuple.split(', ', 1)[0]),)
        t = t + (int(mytuple.split(', ', 1)[1]),)
        mylist.append(t)
    return mylist

# Get tuples to draw shortest path
def get_sp_tuple( myarray ):
    mylist = []
    for i in range(len(myarray)-1):
        t = ()
        t = t + (myarray[i],)
        t = t + (myarray[i+1],)
        mylist.append(t)
    return mylist

# Draw the paths
def draw_sp( src, trgt, color ):
    # First draw all Connections
    all_connections = getTuples(X)
    g = nx.Graph()
    g.add_edges_from(all_connections)
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(g,pos=fixed_positions, fixed = fixed_nodes)
    nx.draw_networkx_nodes(g,pos,node_size=700, node_color="gray")
    nx.draw_networkx_edges(g,pos,width=3,alpha=0.4,edge_color='red')
    nx.draw_networkx_labels(g,pos,font_size=10)
    # Then, get the shortest path
    sp = nx.shortest_path(g, source=src, target=trgt)
    sp_tuple = get_sp_tuple(sp)
    sp_matrix = shortest_path(X, method='FW', directed=False)
    print 'Shortest Path:'
    print sp_matrix
    print sp_tuple
    g2 = nx.Graph()
    g2.add_edges_from(sp_tuple)
    nx.draw_networkx_nodes(g2,pos,node_size=700, node_color="gray")
    nx.draw_networkx_edges(g2,pos,width=3,alpha=0.7,edge_color=color)
    nx.draw_networkx_labels(g2,pos,font_size=10)

while 1:
    source = int(input('\nsource: '))
    target = int(input('\ntarget: '))
    if source and target < 10:
        draw_sp(source, target, "black")
        show()
        continue

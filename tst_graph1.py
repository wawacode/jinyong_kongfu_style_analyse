import networkx
import json
from matplotlib import pyplot
g=networkx.Graph()
g.add_node("李一")

g.add_edge("李二","李三")
pos=networkx.spring_layout(g)
networkx.draw_networkx_nodes(g,pos,nodelist=["李一","李二","李三"],node_color="r",node_size=50)
networkx.draw_networkx_edges(g,pos,edgelist=[("李一","李二"),("李二","李三")],edge_color="b",width=1)
networkx.draw_networkx_labels(g,pos,font_size=20,font_color="k",font_family='SimHei')
#networkx.draw(g)
pyplot.show()
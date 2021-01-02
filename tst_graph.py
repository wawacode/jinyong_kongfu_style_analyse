import networkx
import json
from matplotlib import pyplot
g=networkx.Graph()
with open("person_list.json","r",encoding="utf8") as f:
    str=f.read()
datas=eval(str)
nodelist=[]
edgelist=[]

for  data in datas.items():
    sub_values=data[1]
    sub_values=dict(sub_values)
    if data[0]=="盖运聪" or data[0]=="姜文" or data[0]=="齐堂主" or data[0]=="易堂主" or data[0]=="周孤桐" or data[0]=="吴柏英" or data[0]=="侯景" or data[0]=="萧绎":
        continue
    #print(data[0])
    #print(data[1])
    if sub_values!={}:
        g.add_node(data[0])
        nodelist.append(data[0])
    else:
        continue

    for sub_value in sub_values.items():
          g.add_node(sub_value[0])
          g.add_edge(data[0],sub_value[0])
          edgelist.append((data[0],sub_value[0]))

pos=networkx.random_layout(g)
networkx.draw_networkx_nodes(g,pos,nodelist=nodelist,node_color="r",node_size=50)
networkx.draw_networkx_edges(g,pos,edgelist=edgelist,edge_color="b",width=1)
networkx.draw_networkx_labels(g,pos,font_size=10,font_color="k",font_family='SimHei')
pyplot.show()
#pyplot.savefig("graph.png", dpi=5000)


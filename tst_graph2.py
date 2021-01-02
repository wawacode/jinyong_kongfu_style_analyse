import networkx
import json
from matplotlib import pyplot
g=networkx.Graph()
with open("person_list.json","r",encoding="utf8") as f:
    str=f.read()
datas=eval(str)
nodelists=set({})

for  data in datas.items():
    sub_values=data[1]
    sub_values=dict(sub_values)
    if sub_values=={}:
        continue
    for sub_value in sub_values.items():
        nodelists.add((data[0],sub_value[0],sub_value[1]))
print(nodelists)
print(len(nodelists))
nodelists=sorted(nodelists,key=lambda x:x[2],reverse=True)
for node1 in nodelists:
    for node2 in nodelists:
        if node1==node2:
            continue
        if node1[0]==node2[1] and node1[1]==node2[0]:
            nodelists.remove(node2)
            continue
print(nodelists)
print(len(nodelists))
arrlist=nodelists[:100]
nodelist=[]
edgelist=[]
for  data in arrlist:
        g.add_node(data[0])
        g.add_node(data[1])
        nodelist.append(data[0])
        nodelist.append(data[1])
        g.add_edge(data[0],sub_value[0])
        edgelist.append((data[0],data[1]))

pos=networkx.shell_layout(g)
networkx.draw_networkx_nodes(g,pos,nodelist=nodelist,node_color="r",node_size=50)
networkx.draw_networkx_edges(g,pos,edgelist=edgelist,edge_color="b",width=1)
networkx.draw_networkx_labels(g,pos,font_size=10,font_color="k",font_family='SimHei')
#pyplot.show()

#networkx.draw(g,pos = networkx.random_layout(g),node_color = 'b',edge_color = 'r',with_labels = True,font_size =18,node_size =20)
pyplot.savefig("graph1.png", dpi=1000)


import networkx as nx
import matplotlib.pyplot as plt
import pylab
def wage_graph():
    '''graf do historyjki 2'''
    G = nx.DiGraph()
    #G.add_edges_from([('A', 'B'),('C','D'),('G','D')], weight=1)
    def_names=['funkcja_1','funkcja_2','funkcja_3']      #tu bedzie tablica zawierajaca nazwy funkcji użyte w innej fukcji
    for x in def_names:
        tab_X=[]
        xtimes=5                    # tutaj będzie ile razy jakas funkcja byla uzyta w innej funkcji
        #print(x,'jest ',xtimes)
        tab_X.append(x)
        x1 = 'main'                 #tutaj będą nazwy funkcji w których następuje wywołanie innych funkcji
        your_list_with_tuples = [(x1, k) for k in tab_X]
        G.add_edges_from(your_list_with_tuples, weight=xtimes)
    val_map = {'main':1.0}
    values = [val_map.get(node, 0.45) for node in G.nodes()]
    edge_labels=dict([((u,v,),d['weight'])
            for u,v,d in G.edges(data=True)])
    #red_edges = your_list_with_tuples
    #edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    pos=nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G,pos, with_labels=True, font_weight='bold',node_color = values, node_size=1500,edge_cmap=plt.cm.Reds)
    pylab.show()

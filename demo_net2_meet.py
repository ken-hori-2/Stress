import matplotlib.pyplot as plt
import networkx as nx

# Graphオブジェクトの作成
G = nx.Graph()
 
# nodeデータの追加
G.add_nodes_from(["A", "B", "C", "D"])
 
# edgeデータの追加
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D")])

# G.add_edge("A", "B", length = 9)
# G.add_edge("B", "C", length = 7)
# G.add_edge("C", "D", length = 5)

G.add_edge("A", "B", length = 3)
G.add_edge("B", "C", length = 2)
G.add_edge("C", "D", length = 1)

# G.add_edge("A", "X", length = 5)

pos = nx.spring_layout(G)
 
# ネットワークの可視化
# nx.draw(G, with_labels = True)
# plt.show()
# nx.draw(G, with_labels=True, node_color = "red", edge_color = "gray", node_size = 500, width = 5)
# plt.show()


colors = ["green", "red", "magenta", "yellow"]
#nx.draw(G, with_labels=True, node_color = colors)  # 色付きノードとエッジ3

import random
import numpy as np
List = [0.5,0.6,0.7,0.8,0.9,1.0]
sNumbers = np.random.choice(List, 1, p=[0.10,0.15,0.20,0.25,0.20,0.10])
x0 = 0
x1 = round(0.0,10)
for i in range(10):
    x1 += round(0.10,1)
    x1 = round(x1,1)
    print('x1={},{}回目'.format(x1,i+1))
    if sNumbers <= x1:
        a_lm = 1
        x0 = 1
        
        print('x1 = {}'.format(x1))
        print('発見')

    if x0 == 1:
        x2 = 1.0 - x1
        x2 = round(x2,1)
        print('基準距離とのズレ:{}'.format(x2))
        break

# ネットワーク全体の次数の平均値を計算
# average_deg = sum(d for n, d in G.degree()) / G.number_of_nodes()

# ノードの次数に比例するようにサイズを設定
# sizes = [300*deg/average_deg for node, deg in G.degree()]
# sizes = [10, (1-x1)*500, (1-0.7)*500, (1-0.5)*500]
sizes = [10, round((1-0.9)*500*2,1), round((1-0.7)*500*4,1), round((1-0.5)*500*8,1)]

print(sizes)
# [150.0, 450.0, 600.0, 150.0, 150.0, 300.0]
 
# グラフの出力
plt.figure(figsize = (10,5))
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color = colors, node_size = sizes, edge_color = "black")

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={('A', 'B'): '0.9', 
                 ('B', 'C'): '0.7', 
                 ('C', 'D'): '0.5'},
    font_color='red'
)
# nx.draw_networkx_edge_labels(G, pos)
# plt.show() # ←棒グラフと並べて表示する場合は消します。



print("deg2:{}".format(G.degree))
X_num = [('A', 0),('B', round(1 - 0.9,1)),('C', round(1 - 0.7,1)),('D', round(1 - 0.5,1))]
# X_num2 = [('A', 'B','0.9'), 
#             ('B', 'C','0.7'), 
#             ('C', 'D', '0.5')]

# 棒グラフ
# 次数の多い順番でnodeを並び替える
# nodes_sorted_by_degree = sorted(G.degree(), key=lambda x: x[1], reverse=True)
nodes_sorted_by_degree = sorted(X_num, key=lambda x: x[1], reverse=True)
print(nodes_sorted_by_degree)
# [('C', 4), ('B', 3), ('F', 2), ('A', 1), ('D', 1), ('E', 1)]
 
# 色のリストを次数順に並び替える
colors_dict = dict(zip(G.nodes(), colors))
colors_sorted = [colors_dict[node] for node, _ in nodes_sorted_by_degree]
print(colors_sorted)
# ['red', 'green', 'yellow', 'lightblue', 'cyan', 'magenta']


# グラフの出力
x, height = list(zip(*nodes_sorted_by_degree))
plt.subplot(122)
plt.xlabel("Number of degrees")
plt.ylabel("Name of node")
plt.barh(x, height, color = colors_sorted)
plt.show()

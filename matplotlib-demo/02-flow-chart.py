import matplotlib.pyplot as plt
import networkx as nx

# 创建有向图
G = nx.DiGraph()

# 添加节点
G.add_node('A', label='Records identified through\ndatabase searching (n=565)')
G.add_node('B', label='Additional records identified\nthrough other sources (n=0)')
G.add_node('C', label='Records after duplicates removed\n(n=554)')
G.add_node('D', label='Records screened\n(n=554)')
G.add_node('E', label='Records excluded\n(n=372)')
G.add_node('F', label='Full-text articles assessed for eligibility\n(n=182)')
G.add_node('G', label='Full-text articles excluded with reason (n=109)\n- Not necessary for integration of FSP\n  modelling for digital twins in agriculture')
G.add_node('H', label='Studies included\nin background (n=73)')

# 添加边
G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('F', 'G'), ('F', 'H')])

# 定义布局
pos = {
    'A': (0, 3), 'B': (2, 3), 'C': (1, 2.5), 'D': (1, 2),
    'E': (0, 1.5), 'F': (2, 1.5), 'G': (2, 1), 'H': (2, 0.5)
}

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='white', edgecolors='black')

# 绘制边
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)

# 添加标签
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels, font_size=8, verticalalignment='center', horizontalalignment='center')

# 显示图
plt.title('Literature Review Methodology Diagram')
plt.axis('off')  # 关闭坐标轴
plt.show()

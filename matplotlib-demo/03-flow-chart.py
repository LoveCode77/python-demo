import matplotlib.pyplot as plt
import networkx as nx

# 创建有向图
G = nx.DiGraph()

# 添加节点
G.add_node('A', label='Init()\n\nInitialization:\n• Load and initialize global parameters\n• Initialize environmental conditions\n• Initialize plants')
G.add_node('B', label='Run()\n\nGrowth step(hourly)\n• Update sun and sky\n• Run light model\n• Apply rules\n  • Update existing organs\n  • Morphology(formation of new organs)\n  • Rules defining local transport of substances\n• Update output')
G.add_node('C', label='Stop()\n\nSummary/Final output\n• Yield\n• Scenarios')

# 添加边
G.add_edges_from([('A', 'B'), ('B', 'C')])
# G.add_edge('B', 'B', label='Main loop')

# 定义布局
pos = {
    'A': (0, 0), 'B': (1, 0), 'C': (2, 0)
}

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=16000, node_color='white', edgecolors='black')

# 绘制边
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=40)
nx.draw_networkx_edge_labels(G, pos, edge_labels={('B', 'B'): 'Main loop'}, font_size=8)

# 添加标签
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels, font_size=8, verticalalignment='center', horizontalalignment='center')

# 显示图
plt.title('Process Flow Diagram')
plt.axis('off')  # 关闭坐标轴
plt.show()

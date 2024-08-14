import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data
papers = [
    "Moshrefzadeh et al., 2020", "Angin et al., 2020", "Skobelev et al., 2020",
    "Skobelev et al., 2020", "Jans-Singh et al., 2020", "Ahmed et al., 2019",
    "Hemming et al., 2020", "Wang et al., 2020", "Howard et al., 2020",
    "Monteiro et al., 2018", "Chaux et al., 2021", "Alves et al., 2019"
]

layers = ["Device layer", "IoT", "API", "3D modelling", "Mathematical modelling",
          "3D functional modelling", "Application layer", "Intelligence layer"]

# Matrix indicating which paper includes which layer
matrix = [
    [1, 1, 1, 0, 0, 0, 0, 0],  # Moshrefzadeh et al., 2020
    [1, 1, 0, 1, 1, 0, 0, 0],  # Angin et al., 2020
    [1, 1, 1, 0, 0, 0, 0, 0],  # Skobelev et al., 2020
    [1, 1, 1, 0, 0, 0, 0, 0],  # Skobelev et al., 2020 (repeated)
    [1, 1, 1, 0, 0, 0, 1, 1],  # Jans-Singh et al., 2020
    [1, 1, 1, 0, 1, 0, 1, 1],  # Ahmed et al., 2019
    [1, 1, 1, 0, 1, 0, 0, 1],  # Hemming et al., 2020
    [1, 1, 1, 0, 1, 0, 0, 1],  # Wang et al., 2020
    [1, 1, 1, 0, 0, 0, 1, 1],  # Howard et al., 2020
    [1, 1, 1, 0, 0, 0, 0, 1],  # Monteiro et al., 2018
    [1, 1, 1, 0, 1, 0, 1, 1],  # Chaux et al., 2021
    [1, 1, 1, 0, 0, 0, 1, 1],  # Alves et al., 2019
]


# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val:
            ax.broken_barh([(j, 0.9)], (i - 0.4, 0.3), facecolors='black')

ax.set_yticks(range(len(papers)))
ax.set_yticklabels(papers)

ax.set_xlim(left=-0.5)
print(len(layers))
# ax.set_xticks(range(len(layers)))
ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
ax.set_xticklabels(layers, rotation=45, ha='right')

# Add dotted line to indicate non-existent 3D functional modeling
# ax.axvline(x=5, color='black', linestyle='dotted')
# 设置矩形的左下角坐标和宽度、高度
# 例如，在x=2的位置，y=0.5的位置，宽度为3，高度为0.8
rect = Rectangle((5, -0.7), width=0.9, height=len(papers) - 0.2, facecolor='none', edgecolor='black', linestyle='--',
                 linewidth=1)
ax.add_patch(rect)
ax.set_xlabel('Layers of existing DT in agriculture')
ax.set_ylabel('Papers')

# plt.title('Composition of layers of existing DTs in agriculture domain')
plt.tight_layout()
# 将图形保存为PNG文件
plt.savefig('example_graph.tiff',dpi=300)
plt.show()

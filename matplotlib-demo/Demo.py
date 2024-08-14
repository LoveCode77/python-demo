import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 读取图片并转换为灰度图
image_path = 'avatar.jpg'  # 替换为你的图片路径
image = Image.open(image_path).convert('L')
image = image.resize((100, 100))  # 调整图片大小以减少计算量

# 获取图片的像素值
pixel_values = np.array(image)

# 创建一个图形和一个坐标轴
fig, ax = plt.subplots()

# 设置点的颜色和大小
scatter_kwargs = {'c': 'red', 'alpha': 0.5}

# 根据像素值生成不同的点
points_x, points_y, points_size = [], [], []
for i in range(pixel_values.shape[0]):
    for j in range(pixel_values.shape[1]):
        brightness = pixel_values[i, j]
        if brightness < 128:  # 可以根据需要调整阈值
            points_x.append(j)
            points_y.append(pixel_values.shape[0] - i)  # 翻转y轴
            points_size.append((255 - brightness) / 5)  # 根据亮度调整点的大小

# 绘制点
ax.scatter(points_x, points_y, s=5, **scatter_kwargs)

# 设置坐标轴范围和隐藏坐标轴
ax.set_xlim(0, pixel_values.shape[1])
ax.set_ylim(0, pixel_values.shape[0])
ax.axis('off')

# 显示图形
plt.show()

import numpy as np

# 设置随机种子，以确保结果可复现
np.random.seed(42)

# 生成100个随机二维点
points = np.random.rand(100, 2) * np.array([60, 100])

# 打印生成的随机二维点
for point in points:
    print(point)

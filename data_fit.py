import numpy as np
import matplotlib.pyplot as plt

# 生成一些样本数据
x = np.array([0.284786087,0.12945381,-0.074728547,-0.256955812,-0.399115034])
y = np.array([-8206.226946,-2289.993967,293.8983481,-3127.71489,-10068.41365])

# 进行多项式拟合，这里使用3次多项式（可以根据需求调整次数）
coefficients = np.polyfit(x, y, 4)

# 生成拟合曲线的函数
fit_function = np.poly1d(coefficients)

# 生成拟合后的y值
y_fit = fit_function(x)

# 打印拟合的多项式系数
print("拟合多项式系数:", coefficients)

# 绘制原始数据和拟合曲线
plt.scatter(x, y, label='orignal')
plt.plot(x, y_fit, label='fit', color='red')
plt.legend()
plt.show()

# 打印拟合多项式的每个系数
print("fit coef:")
for i, coef in enumerate(coefficients):
    print(f"coef {len(coefficients) - i - 1}: {coef}")

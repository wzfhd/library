import numpy as np

# 定义多项式函数
def polynomial(x, c, d):
    return c * x**2 + d * x

# 定义均方误差损失函数
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# 定义模型参数
c, d = -75000, -9000

# 训练数据
x_train = np.array([0.208492142 , -0.06594651 , -0.258053567])
y_true = np.array([-251.7114242 , 9.843791673 , 300.2996041])

# 定义学习率和训练步数
learning_rate = 0.01
num_steps = 500000

# 训练模型
for step in range(num_steps):
    # 计算模型预测值
    y_pred = polynomial(x_train, c, d)
    
    # 计算损失
    loss = mse_loss(y_true, y_pred)
    
    # 计算梯度
    gradient_c = -2 * np.mean((y_true - y_pred) * x_train**2)
    gradient_d = -2 * np.mean((y_true - y_pred) * x_train)
    
    # 更新模型参数
    c -= learning_rate * gradient_c
    d -= learning_rate * gradient_d
    
    # 打印训练过程
    if step % 10000 == 0:
        print(f"Step {step}, Loss: {loss}")

# 打印最终模型参数
print(f"Final parameters: c={c}, d={d}")

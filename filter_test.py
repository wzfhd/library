import numpy as np
from scipy.signal import butter, freqz
import matplotlib.pyplot as plt

# 采样频率和截止频率
fs = 1000  # 采样频率
cutoff = 100  # 截止频率

# 计算归一化的截止频率
nyquist = 0.5 * fs
normalized_cutoff = cutoff / nyquist

# 使用巴特沃斯滤波器设计函数计算滤波器系数
b, a = butter(2, normalized_cutoff, btype='low', analog=False, output='ba')

# 计算滤波器的频率响应
w, h = freqz(b, a, worN=8000)

# 绘制幅频响应曲线
plt.figure()
plt.plot(w, np.abs(h))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Frequency Response')
plt.grid()

plt.savefig('plot0.png')  # 将图形保存为plot.png文件

# 绘制相频响应曲线
plt.figure()
plt.plot(w, np.angle(h))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase Frequency Response')
plt.grid()

plt.savefig('plot1.png')  # 将图形保存为plot.png文件


import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

def plot_filter_response(b, a, fs):
    # 计算滤波器的频率响应
    w, h = freqz(b, a, worN=8000, fs=fs)

    # 绘制幅频响应曲线
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Magnitude Frequency Response')
    plt.grid()

    # 绘制相频响应曲线
    plt.figure()
    plt.plot(w, np.angle(h))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')
    plt.title('Phase Frequency Response')
    plt.grid()

    plt.show()




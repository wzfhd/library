"""module : process SPL data"""

def read_txt_file(file_path):
    """
    逐行读取txt文件的内容并返回一个包含每行内容的列表。

    Parameters:
    - file_path (str): 文件路径。

    Returns:
    - lines (list): 包含文件每行内容的列表。
    """
    lines = []
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
            data.append(line.replace(':',""))
    return lines , data

def sign_re(h):
    """
    将字符 '0', '1', 'E', 'F' 转换为对应的整数值。

    Parameters:
    - h (str): 输入字符。

    Returns:
    - d (int): 转换后的整数值。
    """
    if h == '0':
        d = 0
    elif h == '1':
        d = 1
    elif h == 'E':
        d = 2
    elif h == 'F':
        d = 3
    else:
        d = 0
    return d

file_path = 'C:/Users/huadi/Documents/WXWork/1688854286477398/Cache/File/2023-11/11-14_5000_1.6KHz_SPLU.txt'
content_lines , s = read_txt_file(file_path)
print(content_lines[0,0])
# 打印每一行的内容
mem = [[""] * 6 for _ in range(len(s)*4)]

for i in range(len(s)):
    data = s[i]
    mem[(i - 1) * 4] = data[9:14]
    mem[(i - 1) * 4 + 1] = data[17:22]
    mem[(i - 1) * 4 + 2] = data[25:30]
    mem[(i - 1) * 4 + 3] = data[33:38]

#print(mem)
dec = [0] * len(mem)
for i in range(len(mem)):
    d0 = int(mem[i][4])
    d1 = int(mem[i][5], 16)
    d2 = int(mem[i][2], 16)
    d3 = int(mem[i][3], 16)
    d4 = int(mem[i][0], 16)
    d5 = int(mem[i][1], 16)

    sum0 = d0 * 2**20 + d1 * 2**16 + d2 * 2**12 + d3 * 2**8 + d4 * 2**4 + d5
    if sum0 <= 2**21 - 1:
        dec[i] = sum0
    else:
        dec[i] = sum0 - 2**22

data_out = [d / 2**21 for d in dec]
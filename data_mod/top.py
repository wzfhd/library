# 将MATLAB代码打包成函数

# Assuming you have a MATLAB code snippet that you want to convert into a Python function,
# here's an example of how you can package it into a function:

import numpy as np
from openpyxl import Workbook

def sign_re(h):

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

def h2d(h):

    if h == '0':
        d = 0
    elif h == '1':
        d = 1
    elif h == '2':
        d = 2
    elif h == '3':
        d = 3
    elif h == '4':
        d = 4
    elif h == '5':
        d = 5
    elif h == '6':
        d = 6
    elif h == '7':
        d = 7
    elif h == '8':
        d = 8
    elif h == '9':
        d = 9
    elif h == 'A':
        d = 10
    elif h == 'B':
        d = 11
    elif h == 'C':
        d = 12
    elif h == 'D':
        d = 13
    elif h == 'E':
        d = 14
    elif h == 'F':
        d = 15
    else:
        d = None  # Handle invalid input

    return d

def write_data_to_excel_with_name(data_matrix, excel_file_path):
    # 创建一个新的工作簿
    workbook = Workbook()
    # 选择默认的活动工作表
    worksheet = workbook.active
    # 添加表头
    headers = ['dec']
    worksheet.append(headers)
    # 写入数据
    for row in data_matrix:
        worksheet.append(row)
    # 保存工作簿
    workbook.save(excel_file_path)


# 指定文件地址
file_path = 'C:/Users/huadi/JINSHAN/MCU/emu外包/竞品测试/模拟测试数据/spl_011.txt'
excel_file_path = 'C:/Users/huadi/JINSHAN/MCU/emu外包/竞品测试/模拟测试数据/spl_011.xlsx'

# 打开文件并读取内容
with open(file_path, 'r') as file:
    Rbuffer = file.read()

# 处理文件内容
print(Rbuffer)

index = []

for i in range(len(Rbuffer)):
    if Rbuffer[i] == ":":
        index.append(i)

print(index)

start = 3
stop = len(index) - 2

t = list(range(start, stop))

data =  []
data_len = 4

for i in range(start, stop):
    data.append(Rbuffer[index[i]+9:index[i]+9+data_len])
    data.append(Rbuffer[index[i]+9+data_len+4:index[i]+9+data_len+4+data_len])
    data.append(Rbuffer[index[i]+9+data_len+4+data_len+4:index[i]+9+data_len+4+data_len+4+data_len])
    data.append(Rbuffer[index[i]+9+data_len+4+data_len+4+data_len+4:index[i]+9+data_len+4+data_len+4+data_len+4+data_len])

print(data)


data_dec =  []

for i in range(len(data)):
    d0 = sign_re(data[i][2])
    d1 = h2d(data[i][3])
    d2 = h2d(data[i][0])
    d3 = h2d(data[i][1])
    print(data[i][2])
    d = d0*2**12 + d1*2**8 + d2*2**4 + d3
    if d<=2**13-1:
        d = d
    else:
        d = d - 2**14
    data_dec.append(d/2**13)

my_vector = np.array(data_dec)


data_dec0 = my_vector.reshape(-1, 1)


data_dec1 = data_dec0.tolist()

write_data_to_excel_with_name(data_dec1, excel_file_path)



"""

start=3
stop=length(Rbuffer)-2

s=Rbuffer(start:stop)

mem=char(zeros(length(s)*4,4))

for i=1:length(s)
    data=char(s(i));
    mem((i-1)*4+1,:)=data(9:12)
    mem((i-1)*4+2,:)=data(17:20)
    mem((i-1)*4+3,:)=data(25:28)
    mem((i-1)*4+4,:)=data(33:36)
end


dec=zeros(length(mem),1);
for i=1:length(mem)
    d0=sign_re(mem(i,3));
    d1=h2d(mem(i,4));
    d2=h2d(mem(i,1));
    d3=h2d(mem(i,2));

    sum=d0*2^12 + d1*2^8 + d2*2^4 + d3;
    if sum<2^13-1
        dec(i)=sum;
    else
        dec(i)=sum-2^14;
    end
end

data_out=dec/2^13;

"""



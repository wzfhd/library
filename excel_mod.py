"""module : get excel name and data"""

import os
import pandas as pd
from openpyxl import Workbook
import matplotlib.pyplot as plt

def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot')
    plt.savefig('plot.png')

def get_file_names(directory_path):
    files = os.listdir(directory_path)
    file_name = [name.split('.')[0] for name in files]
    return files,file_name

def read_excel_file(file_path):
    data = pd.read_excel(file_path)
    s0 = data.iloc[2,0]
    s1 = data.iloc[2,1]
    #print(data)
    return s0 , s1

def write_data_to_excel(data, excel_file_path):
    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False)
    print("数据已成功写入Excel文件！")

def hex_to_decimal(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num

def write_data_to_excel_with_name(data_matrix, excel_file_path):
    # 创建一个新的工作簿
    workbook = Workbook()
    # 选择默认的活动工作表
    worksheet = workbook.active
    # 添加表头
    headers = ['reat T', 'low hex', 'high hex', 'dec', 'test T']
    worksheet.append(headers)
    # 写入数据
    for row in data_matrix:
        worksheet.append(row)
    # 保存工作簿
    workbook.save(excel_file_path)

###################################################################
# 测试示例
excel_file_path = 'G:/test.xlsx'  # 指定要保存的Excel文件路径
directory_path = 'G:/code/library/excel_data'

# 1. get file name and temperature
file_full_name , t = get_file_names(directory_path)

# 2. get data of every temperature
# temperature|low hex|high hex|dec|tmp
data_matrix = [[""] * 5 for _ in range(len(t))]
#for name in file_full_name:
for i in range(len(t)):
    name = file_full_name[i]
    full_dir = directory_path + '/' + name
    data_matrix[i][0] = t[i]
    data_matrix[i][1] , data_matrix[i][2] = read_excel_file(full_dir)

    sum_dec = hex_to_decimal(data_matrix[i][1]) + (hex_to_decimal(data_matrix[i][2])*(2**8))

    if sum_dec <= 2**15-1:
        data_matrix[i][3] = sum_dec
    else:
        data_matrix[i][3] = sum_dec - 2**16

    data_matrix[i][4] = data_matrix[i][3]*0.00278 - 12

print(data_matrix)
# 3. write data to excel
write_data_to_excel_with_name(data_matrix, excel_file_path)


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plot_data(x, y)

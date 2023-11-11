"""module : get excel name and data"""

import os
import pandas as pd

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

# 测试示例

excel_file_path = 'G:/test.xlsx'  # 指定要保存的Excel文件路径

directory_path = 'G:/code/library/excel_data'

#write_data_to_excel(data, excel_file_path)

# 1. get file name and temperature
file_full_name , t = get_file_names(directory_path)

# 2. get data of every temperature
data_matrix = [[""] * 3 for _ in range(len(t))]
#for name in file_full_name:
for i in range(5):
    name = file_full_name[i]
    full_dir = directory_path + '/' + name
    data_matrix[i][0] = t[i]
    data_matrix[i][1] , data_matrix[i][2] = read_excel_file(full_dir)
    #print(data)

# 3. write data to excel
write_data_to_excel(data_matrix, excel_file_path)
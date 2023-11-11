import os
import pandas as pd

def get_file_names(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        first_file_name = file
        print(first_file_name)
        #print(file)

def read_excel_file(file_path):
    data = pd.read_excel(file_path)
    s = data.iloc[2,0]
    #print(data)
    print(s)

if __name__ == "__main__":
    directory_path = "D:/BaiduNetdisk"  # 替换为你想要读取文件名的目录路径
    get_file_names(directory_path)

    excel_file_path = 'C:/Users/Windows11/Desktop/emu会议纪要.xlsx'
    read_excel_file(excel_file_path)

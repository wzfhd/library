import os
import shutil

def classify_files_by_keyword(source_folder, destination_folder_1, destination_folder_2, keyword):
    # 获取源文件夹下的所有文件
    files = os.listdir(source_folder)

    # 创建两个目标文件夹，用于存储分类后的文件
    if not os.path.exists(destination_folder_1):
        os.makedirs(destination_folder_1)
    if not os.path.exists(destination_folder_2):
        os.makedirs(destination_folder_2)

    # 遍历文件并分类存储
    for file in files:
        file_path = os.path.join(source_folder, file)

        # 判断文件名中是否包含关键字
        if keyword in file:
            # 如果包含关键字，将文件移动到目标文件夹1
            shutil.move(file_path, os.path.join(destination_folder_1, file))
            print(f"文件 '{file}' 包含关键字 '{keyword}'，已移动到目标文件夹1。")
        else:
            # 如果不包含关键字，将文件移动到目标文件夹2
            shutil.move(file_path, os.path.join(destination_folder_2, file))
            print(f"文件 '{file}' 不包含关键字 '{keyword}'，已移动到目标文件夹2。")

if __name__ == "__main__":
    # 替换为你的源文件夹路径、目标文件夹1路径、目标文件夹2路径和关键字
    source_folder = 'C:/Users/huadi/JINSHAN/MCU/RTC/扫温测试/dfi_TEMP_1115'
    destination_folder_1 = 'C:/Users/huadi/JINSHAN/MCU/RTC/扫温测试/dfi_TEMP_1115/1'
    destination_folder_2 = 'C:/Users/huadi/JINSHAN/MCU/RTC/扫温测试/dfi_TEMP_1115/2'
    keyword = '(1)'

    classify_files_by_keyword(source_folder, destination_folder_1, destination_folder_2, keyword)

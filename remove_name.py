import os
import shutil
import tkinter as tk
from tkinter import filedialog

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

def browse_folder(entry):
    folder_selected = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(tk.END, folder_selected)

def start_classification():
    source_folder = source_entry.get()
    destination_folder_1 = dest1_entry.get()
    destination_folder_2 = dest2_entry.get()
    keyword = keyword_entry.get()

    classify_files_by_keyword(source_folder, destination_folder_1, destination_folder_2, keyword)

# 创建主窗口
root = tk.Tk()
root.title("文件分类工具")

# 设置主窗口样式
root.geometry("600x400")
root.resizable(width=False, height=False)

# 创建标签和输入框，并使用网格布局
tk.Label(root, text="源文件夹:").grid(row=0, column=0, padx=10, pady=5)
source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=lambda: browse_folder(source_entry)).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="目标文件夹1:").grid(row=1, column=0, padx=10, pady=5)
dest1_entry = tk.Entry(root)
dest1_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=lambda: browse_folder(dest1_entry)).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="目标文件夹2:").grid(row=2, column=0, padx=10, pady=5)
dest2_entry = tk.Entry(root)
dest2_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="浏览", command=lambda: browse_folder(dest2_entry)).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="关键字:").grid(row=3, column=0, padx=10, pady=5)
keyword_entry = tk.Entry(root)
keyword_entry.grid(row=3, column=1, padx=10, pady=5)

# 创建按钮并设置样式
process_button = tk.Button(root, text="开始分类", command=start_classification, bg="#4CAF50", fg="white", padx=10, pady=5)
process_button.grid(row=4, column=0, columnspan=3, pady=10)

# 运行主循环
root.mainloop()

from openpyxl import Workbook

file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/I1_2.5ms_1212.log'

def write_data_to_excel_with_name(data_matrix, excel_file_path,headers):
    # 创建一个新的工作簿
    workbook = Workbook()
    # 选择默认的活动工作表
    worksheet = workbook.active
    # 添加表头
    # headers = ['dec']
    worksheet.append(headers)
    # 写入数据
    for row in data_matrix:
        worksheet.append([row])
    # 保存工作簿
    workbook.save(excel_file_path)



FastRMSU = []
FastRMSI1 = []
FastRMSI2 = []
FastP1 = []
FastQ1 = []
FastP2 = []
FastQ2 = []
FastS1 = []
FastS2 = []

RMSU = []
RMSI1 = []
RMSI2 = []
P1 = []
Q1 = []
P2 = []
Q2 = []
S1 = []
S2 = []

FreqU = []

index = 1
index_all = 0
index0 = 0
index1 = 0
index2 = 0
index3 = 0
index4 = 0
index5 = 0
index6 = 0
index7 = 0
index8 = 0

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        if line[0:1] == 'B1':
            d = int(line[len(line)-5:len(line)], 16)
            FastRMSI1.append(d)
        elif line[0:1] == 'B2':
            d = int(line[len(line)-5:len(line)], 16)
            FastRMSI2.append(d)
        elif line[0:1] == 'B3':
            d = int(line[len(line)-5:len(line)], 16)
            FastRMSU.append(d)
        elif line[0:1] == 'B4':
            d = int(line[len(line)-5:len(line)], 16)
            RMSI1.append(d)
        elif line[0:1] == 'B5':
            d = int(line[len(line)-5:len(line)], 16)
            RMSI2.append(d)
        elif line[0:1] == 'B6':
            d = int(line[len(line)-5:len(line)], 16)
            RMSU.append(d)
        elif line[0:1] == 'C0':
            d = int(line[len(line)-3:len(line)], 16)
            f = 819200/(d*2)
            FreqU.append()
        elif line[0:1] == 'D1':
            d = int(line[len(line)-7:len(line)], 16)
            FastP1.append(d)
        elif line[0:1] == 'D2':
            d = int(line[len(line)-7:len(line)], 16)
            FastQ1.append(d)
        elif line[0:1] == 'D3':
            d = int(line[len(line)-7:len(line)], 16)
            FastP2.append(d)
        elif line[0:1] == 'D4':
            d = int(line[len(line)-7:len(line)], 16)
            FastQ2.append(d)
        elif line[0:1] == 'D5':
            d = int(line[len(line)-7:len(line)], 16)
            FastS1.append(d)
        elif line[0:1] == 'D6':
            d = int(line[len(line)-7:len(line)], 16)
            FastS2.append(d)
        elif line[0:1] == 'E1':
            d = int(line[len(line)-7:len(line)], 16)
            P1.append(d)
        elif line[0:1] == 'E2':
            d = int(line[len(line)-7:len(line)], 16)
            Q1.append(d)
        elif line[0:1] == 'E3':
            d = int(line[len(line)-7:len(line)], 16)
            P2.append(d)
        elif line[0:1] == 'E4':
            d = int(line[len(line)-7:len(line)], 16)
            Q2.append(d)
        elif line[0:1] == 'E5':
            d = int(line[len(line)-7:len(line)], 16)
            S1.append(d)
        elif line[0:1] == 'E6':
            d = int(line[len(line)-7:len(line)], 16)
            S2.append(d)

        # Process each line


excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastRMSU.xlsx'
headers = ['FastRMSU']
# num_list = list(map(int, str(FastRMSU)))
write_data_to_excel_with_name(FastRMSU, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastRMSI1.xlsx'
headers = ['FastRMSI1']
write_data_to_excel_with_name(FastRMSI1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastRMSI2.xlsx'
headers = ['FastRMSI2']
write_data_to_excel_with_name(FastRMSI2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/RMSU.xlsx'
headers = ['RMSU']
# num_list = list(map(int, str(FastRMSU)))
write_data_to_excel_with_name(RMSU, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/RMSI1.xlsx'
headers = ['RMSI1']
write_data_to_excel_with_name(RMSI1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/RMSI2.xlsx'
headers = ['RMSI2']
write_data_to_excel_with_name(RMSI2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastP1.xlsx'
headers = ['FastP1']
write_data_to_excel_with_name(FastP1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastP2.xlsx'
headers = ['FastP2']
write_data_to_excel_with_name(FastP2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastQ1.xlsx'
headers = ['FastQ1']
write_data_to_excel_with_name(FastQ1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastQ2.xlsx'
headers = ['FastQ2']
write_data_to_excel_with_name(FastQ2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastS1.xlsx'
headers = ['FastS1']
write_data_to_excel_with_name(FastS1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FastS2.xlsx'
headers = ['FastS2']
write_data_to_excel_with_name(FastS2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/P1.xlsx'
headers = ['P1']
write_data_to_excel_with_name(P1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/P2.xlsx'
headers = ['P2']
write_data_to_excel_with_name(P2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/Q1.xlsx'
headers = ['Q1']
write_data_to_excel_with_name(Q1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/Q2.xlsx'
headers = ['Q2']
write_data_to_excel_with_name(Q2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/S1.xlsx'
headers = ['S1']
write_data_to_excel_with_name(S1, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/S2.xlsx'
headers = ['S2']
write_data_to_excel_with_name(S2, excel_file_path,headers)

excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/FreqU.xlsx'
headers = ['FreqU']
write_data_to_excel_with_name(FreqU, excel_file_path,headers)


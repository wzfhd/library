from openpyxl import Workbook
import numpy as np

file_path = 'C:/Users/huadi/JINSHAN/MCU/emu外包/竞品测试/U_500mV_I1_400mV_3.7ms.log'

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
        #print(line)
        print(line[0:2])
        #print(line[len(line)-9:len(line)-1])

        if line[0:2] == 'B1':
            d = int(line[len(line)-7:len(line)-1], 16)
            #print(line[len(line)-6:len(line)-1])
            FastRMSI1.append(d)
        elif line[0:2] == 'B2':
            d = int(line[len(line)-7:len(line)-1], 16)
            FastRMSI2.append(d)
        elif line[0:2] == 'B3':
            d = int(line[len(line)-7:len(line)-1], 16)
            FastRMSU.append(d)
        elif line[0:2] == 'B4':
            d = int(line[len(line)-7:len(line)-1], 16)
            RMSI1.append(d)
        elif line[0:2] == 'B5':
            d = int(line[len(line)-7:len(line)-1], 16)
            RMSI2.append(d)
        elif line[0:2] == 'B6':
            d = int(line[len(line)-7:len(line)-1], 16)
            RMSU.append(d)
        elif line[0:2] == 'C0':
            d = int(line[len(line)-5:len(line)-1], 16)
            f = 819200/(d*2)
            FreqU.append(f)
        elif line[0:2] == 'D1':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastP1.append(f)
        elif line[0:2] == 'D2':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastQ1.append(f)
        elif line[0:2] == 'D3':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastP2.append(f)
        elif line[0:2] == 'D4':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastQ2.append(f)
        elif line[0:2] == 'D5':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastS1.append(f)
        elif line[0:2] == 'D6':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            FastS2.append(f)
        elif line[0:2] == 'E1':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            P1.append(f)
        elif line[0:2] == 'E2':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            Q1.append(f)
        elif line[0:2] == 'E3':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            P2.append(f)
        elif line[0:2] == 'E4':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            Q2.append(f)
        elif line[0:2] == 'E5':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            S1.append(f)
        elif line[0:2] == 'E6':
            d = int(line[len(line)-9:len(line)], 16)
            if d>=2**31:
                f = d - 2**32
            else:
                f = d
            S2.append(f)


        # Process each line
result = []
result.append(sum(FastRMSI1)/len(FastRMSI1))
result.append(sum(FastRMSI2)/len(FastRMSI2))
result.append(sum(FastRMSU)/len(FastRMSU))
result.append(sum(RMSI1)/len(RMSI1))
result.append(sum(RMSI2)/len(RMSI2))

result.append(sum(RMSU)/len(RMSU))
result.append(sum(FreqU)/len(FreqU))
result.append(sum(FastP1)/len(FastP1))
result.append(sum(FastQ1)/len(FastQ1))
result.append(sum(FastP2)/len(FastP2))

result.append(sum(FastQ2)/len(FastQ2))
result.append(sum(FastS1)/len(FastS1))
result.append(sum(FastS2)/len(FastS2))
result.append(sum(P1)/len(P1))
result.append(sum(Q1)/len(Q1))

result.append(sum(P2)/len(P2))
result.append(sum(Q2)/len(Q2))
result.append(sum(S1)/len(S1))
result.append(sum(S2)/len(S2))
print(result[2])

re = np.zeros((1,19))
for i in range(19):
    re[0,i] = result[i]
print(re)

FastRMSI1.append(sum(FastRMSI1)/len(FastRMSI1))
FastRMSI2.append(sum(FastRMSI2)/len(FastRMSI2))
FastRMSU.append(sum(FastRMSU)/len(FastRMSU))
RMSI1.append(sum(RMSI1)/len(RMSI1))
RMSI2.append(sum(RMSI2)/len(RMSI2))
RMSU.append(sum(RMSU)/len(RMSU))
FreqU.append(sum(FreqU)/len(FreqU))
FastP1.append(sum(FastP1)/len(FastP1))
FastQ1.append(sum(FastQ1)/len(FastQ1))
FastP2.append(sum(FastP2)/len(FastP2))
FastQ2.append(sum(FastQ2)/len(FastQ2))
FastS1.append(sum(FastS1)/len(FastS1))
FastS2.append(sum(FastS2)/len(FastS2))
P1.append(sum(P1)/len(P1))
Q1.append(sum(Q1)/len(Q1))
P2.append(sum(P2)/len(P2))
Q2.append(sum(Q2)/len(Q2))
S1.append(sum(S1)/len(S1))
S2.append(sum(S2)/len(S2))







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


excel_file_path = 'C:/Users/huadi/JINSHAN/mcu/emu外包/竞品测试/EMU测试3/test.xlsx'
headers = ['FastRMSI1','FastRMSI2','FastRMSU','RMSI1','RMSI2','RMSU','FreqU','FastP1','FastQ1','FastP2','FastQ2','FastS1','FastS2','P1','Q1','P2','Q2','S1','S2']
write_data_to_excel_with_name(result, excel_file_path,headers)

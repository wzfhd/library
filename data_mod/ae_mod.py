from openpyxl import Workbook

file_path = 'G:/code/library/data_mod/data.txt'

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
FastPWR1 = []

SlowRMSU = []
SlowRMSI1 = []
SlowRMSI2 = []
SlowPWR1 = []

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
        index_all = index_all + 1
        if index == 1 or index == 5 or index == 9 or index == 13:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            FastRMSU.append(d)
            index0 = index0 + 1
        elif index == 2 or index == 6 or index == 10 or index == 14:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            FastRMSI1.append(d)
            index1 = index1 + 1
        elif index == 3 or index == 7 or index == 11 or index == 15:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            FastRMSI2.append(d)
            index2 = index2 + 1
        elif index == 4 or index == 8 or index == 12 or index == 16:
            d = decimal_number = int(line[len(line)-6:len(line)], 16)
            if d>=2**31:
                dd = d - 2**32
            else:
                dd = d
            FastPWR1.append(dd)
            index3 = index3 + 1
        elif index == 17:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            SlowRMSU.append(d)
            index4 = index4 + 1
        elif index == 18:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            SlowRMSI1.append(d)
            index5 = index5 + 1
        elif index == 19:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            SlowRMSI2.append(d)
            index6 = index6 + 1
        elif index == 20:
            d = decimal_number = int(line[len(line)-6:len(line)], 16)
            if d>=2**31:
                dd = d - 2**32
            else:
                dd = d
            SlowPWR1.append(dd)
            index7 = index7 + 1
        else:
            d = decimal_number = int(line[len(line)-5:len(line)], 16)
            f = 819200/(d*2)
            FreqU.append(f)
            index8 = index8 + 1
        if index == 21:
            index = 1
        else:
            index = index + 1
        # Process each line

if index0 + index1 + index2 + index3 + index4 + index5 + index6 + index7 + index8 == index_all:
    print('yes')
    print(index0 + index1 + index2 + index3 + index4 + index5 + index6 + index7 + index8)
    print(index_all)
else:
    print('wrong')
    print(index0 + index1 + index2 + index3 + index4 + index5 + index6 + index7 + index8)
    print(index_all)


excel_file_path = 'G:/code/library/data_mod/FastRMSU.xlsx'
headers = ['FastRMSU']
# num_list = list(map(int, str(FastRMSU)))
write_data_to_excel_with_name(FastRMSU, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/FastRMSI1.xlsx'
headers = ['FastRMSI1']
write_data_to_excel_with_name(FastRMSI1, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/FastRMSI2.xlsx'
headers = ['FastRMSI2']
write_data_to_excel_with_name(FastRMSI2, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/FastPWR1.xlsx'
headers = ['FastPWR1']
write_data_to_excel_with_name(FastPWR1, excel_file_path,headers)


excel_file_path = 'G:/code/library/data_mod/SlowRMSU.xlsx'
headers = ['SlowRMSU']
write_data_to_excel_with_name(SlowRMSU, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/SlowRMSI1.xlsx'
headers = ['SlowRMSI1']
write_data_to_excel_with_name(SlowRMSI1, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/SlowRMSI2.xlsx'
headers = ['SlowRMSI2']
write_data_to_excel_with_name(SlowRMSI2, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/SlowPWR1.xlsx'
headers = ['SlowPWR1']
write_data_to_excel_with_name(SlowPWR1, excel_file_path,headers)

excel_file_path = 'G:/code/library/data_mod/FreqU.xlsx'
headers = ['FreqU']
write_data_to_excel_with_name(FreqU, excel_file_path,headers)


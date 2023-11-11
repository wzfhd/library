
import pandas as pd

def read_excel_file(file_path):
    data = pd.read_excel(file_path)
    name = data.iloc[:,0]
    direction = data.iloc[:,1]
    width = data.iloc[:,2]
    return name , direction , width , data

def write_to_v_file(data, file_path):
    with open(file_path, 'w') as f:
        # 写入.v文件头部信息
        f.write("`timescale 1ns/1ps\n")
        f.write("module data_module\n")
        f.write("   (\n")
        for i in range(len(data)-1):
            if data.iloc[i, 1] == "I":
                f.write("       input      [{}:0]       {},\n".format(data.iloc[i,2]-1 , data.iloc[i,0]))
            else:
                f.write("       output     [{}:0]       {},\n".format(data.iloc[i,2]-1 , data.iloc[i,0]))
        if data.iloc[len(data)-1, 1] == "I":
            f.write("       input      [{}:0]       {}\n".format(data.iloc[i,2]-1 , data.iloc[i,0]))
        else:
            f.write("       output     [{}:0]       {}\n".format(data.iloc[i,2]-1 , data.iloc[i,0]))
        f.write("       );\n")
        f.write("\n")
        f.write("\n")
        f.write("endmodule\n")


file_path = 'G:/接口列表.xlsx'
name , direction , width , data = read_excel_file(file_path)
print(data)

file_path = 'G:/test.v'
write_to_v_file(data, file_path)


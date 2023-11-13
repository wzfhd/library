def remove_character(input_string, target_character):
    result_string = input_string.replace(target_character, "")
    return result_string

# 例子
input_string = "Hello(1), World!"
target_character = "(1)"
print(input_string)
result = remove_character(input_string, target_character)
print(result)

hex_string = "0x76 0x12"

# 去除空格并拆分成列表
hex_values = hex_string.replace(" ", "").split("0x")

# 剔除空字符串并转换为整数
integer_values = [int(value, 16) for value in hex_values if value]
for value in hex_values:
    print(value)

# 打印结果
print(integer_values)

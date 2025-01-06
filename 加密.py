import struct

# 定义64进制字母表
BASE64_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@"

# 将二进制转化为64进制
def binary_to_base64(binary_str):
    # 将二进制分成6位一组
    groups = [binary_str[i:i+6] for i in range(0, len(binary_str), 6)]
    # 转换每一组为对应的64进制字符
    base64_result = ''.join(BASE64_ALPHABET[int(group, 2)] for group in groups)
    return base64_result

# 计算校验码（简单异或实现）
def calculate_checksum(binary_str):
    checksum = 0
    for bit in binary_str:
        checksum ^= int(bit)
    # 转成5位二进制
    return f"{checksum:05b}"

# 主函数
def convert_to_base64(input_str):
    if len(input_str) != 3:
        raise ValueError("输入必须是3个字符！")

    # 将每个字符转为UTF-16编码的二进制
    binary_utf16 = ''.join(f"{ord(char):016b}" for char in input_str)

    # 计算校验码
    checksum = calculate_checksum(binary_utf16)

    # 拼接最终的二进制字符串
    final_binary = f"0{checksum}{binary_utf16}"

    # 转换为64进制
    base64_result = binary_to_base64(final_binary)
    return base64_result

# 测试
try:
    input_str = input("请输入3个字符：")
    result = convert_to_base64(input_str)
    print("结果：", result)
except ValueError as e:
    print("错误：", e)

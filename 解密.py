import struct

# 定义64进制字母表
BASE64_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@"

# 将64进制转换为二进制
def base64_to_binary(base64_str):
    binary_str = ''.join(f"{BASE64_ALPHABET.index(char):06b}" for char in base64_str)
    return binary_str

# 校验校验码是否正确
def verify_checksum(binary_str):
    checksum = binary_str[1:6]  # 提取5位校验码
    data_bits = binary_str[6:]  # 提取数据部分

    calculated_checksum = 0
    for bit in data_bits:
        calculated_checksum ^= int(bit)
    
    return checksum == f"{calculated_checksum:05b}"

# 解密函数
def decode_from_base64(base64_str):
    # 转换64进制为二进制
    binary_str = base64_to_binary(base64_str)

    # 校验第一位是否为0
    if binary_str[0] != '0':
        raise ValueError("无效的数据格式：首位不是0！")

    # 校验校验码
    if not verify_checksum(binary_str):
        raise ValueError("校验码错误！")

    # 提取有效数据（去掉前6位：首位 + 校验码）
    data_bits = binary_str[6:]

    # 将数据部分按16位分组，还原为UTF-16字符
    chars = [chr(int(data_bits[i:i+16], 2)) for i in range(0, len(data_bits), 16)]
    return ''.join(chars)

# 测试
try:
    input_str = input("请输入64进制字符串：")
    result = decode_from_base64(input_str)
    print("解密结果：", result)
except ValueError as e:
    print("错误：", e)

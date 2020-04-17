def bin_add(str1, str2):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    temp_add = bin(int1 + int2)
    temp_add = str(temp_add)[2:]
    if len(temp_add) > 16:
        temp_add = bin(int(temp_add[-16:], 2) + 1)
        temp_add = str(temp_add)[2:]
    for l in range(len(temp_add), 16):
        temp_add = '0' + temp_add
    return temp_add


def bin_invert(_str):
    temp_str = list(_str)
    for i in range(len(temp_str)):
        if temp_str[i] == '0':
            temp_str[i] = '1'
        else:
            temp_str[i] = '0'
    return ''.join(temp_str)


if __name__ == '__main__':
    str1 = input("输入第一个16比特的字：")
    str2 = input("输入第二个16比特的字：")
    str3 = input("输入第三个16比特的字：")
    _add = bin_add(str1, str2)
    _add2 = bin_add(_add, str3)
    check_sum = bin_invert(_add2)
    print("UDP检验和为", check_sum)
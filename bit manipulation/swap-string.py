def swapStr(str1, str2):
    str1 = str1 + str2
    str2 = str1[0:(len(str1) - len(str2))]
    str1 = str1[(len(str1) - len(str2)):len(str1)]
    print(str1 + str2)


if __name__ == '__main__':
    swapStr('World', 'Hello')

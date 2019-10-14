def get_binary(i):
    if i > 1:
        get_binary(i // 2)
    return i % 2


if __name__ == '__main__':
    print(get_binary(4))

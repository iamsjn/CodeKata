def find_gcd(a, b):
    if a < b:
        a = a+b
        b = a-b
        a = a-b
    if a == 0:
        return b
    if b == 0:
        return a
    mod = a % b
    if mod == 0:
        return b
    else:
        a = b
        b = mod
        return find_gcd(a, b)


if __name__ == '__main__':
    print('GCD is ', find_gcd(35, 10))

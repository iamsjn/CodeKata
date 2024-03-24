def rolling_hash(s: str) -> int:
    _p = 31
    _m = 1e9 + 9
    _pow_of_p = 1
    _hash_value = 0

    for i in range(len(s)):
        _hash_value = (_hash_value + ((ord(s[i]) - ord('a') + 1) * _pow_of_p)) % _m
        _pow_of_p = (_pow_of_p * _p) % _m

    return int(_hash_value)


if __name__ == "__main__":
    print(rolling_hash("Alchemist"))
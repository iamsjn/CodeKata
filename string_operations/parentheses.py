# from typing import List
#
#
# def generate(result: List[str], s: str, _open: int, close: int, n: int):
#     if _open == n and close == n:
#         result.append(s)
#         return
#     # If the number of _open parentheses is less than the given n
#     if _open < n:
#         print("How many times", _open)
#         generate(result, s + "(", _open + 1, close, n)
#     # If we need more close parentheses to balance
#     if close < _open:
#         generate(result, s + ")", _open, close + 1, n)
#
#


def generate_parenthesis(n):
    combinations = []
    generate_all('', 0, combinations)
    return combinations


def generate_all(current, pos, result):
    print(len(current))
    if (current != '') and (pos == len(current)):
        if valid(current):
            result.append(str(current))
    else:
        current += '('
        generate_all(current, pos+1, result)
        current += ')'
        generate_all(current, pos+1, result)


def valid(current):
    balance = 0
    for i in range(len(current)):
        if current[i] == '(':
            balance = balance + 1
        else:
            balance = balance - 1

        if balance < 0:
            return False

    return balance == 0


if __name__ == "__main__":
    #     # Resultant list
    #     result = []
    #     # Recursively generate parentheses
    #     generate(result, "", 0, 0, 3)
    #     print(result)
    print(generate_parenthesis(3))

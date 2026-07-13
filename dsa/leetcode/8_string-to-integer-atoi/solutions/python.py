def solve(s: str) -> int:
    index = 0
    while index < len(s) and s[index] == " ":
        index += 1

    sign = 1
    if index < len(s) and s[index] in "+-":
        sign = -1 if s[index] == "-" else 1
        index += 1

    limit = 2**31 if sign < 0 else 2**31 - 1
    value = 0
    while index < len(s) and "0" <= s[index] <= "9":
        digit = ord(s[index]) - ord("0")
        if value > (limit - digit) // 10:
            return -limit if sign < 0 else limit
        value = value * 10 + digit
        index += 1
    return sign * value

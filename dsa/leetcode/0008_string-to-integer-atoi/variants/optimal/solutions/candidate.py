def solve(s: str) -> int:
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1

    sign = 1
    if i < len(s) and s[i] in "+-":
        sign = -1 if s[i] == "-" else 1
        i += 1

    limit = 2**31 if sign < 0 else 2**31 - 1
    value = 0
    while i < len(s) and "0" <= s[i] <= "9":
        digit = ord(s[i]) - ord("0")
        if value > (limit - digit) // 10:
            return -limit if sign < 0 else limit
        value = value * 10 + digit
        i += 1

    return sign * value

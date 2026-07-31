def solve(s):
    chars = list(s)
    index = 0

    while index < len(chars) and chars[index] == "a":
        index += 1

    if index == len(chars):
        chars[-1] = "z"
    else:
        while index < len(chars) and chars[index] != "a":
            chars[index] = chr(ord(chars[index]) - 1)
            index += 1

    return "".join(chars)

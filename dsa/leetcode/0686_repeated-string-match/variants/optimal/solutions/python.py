def solve(a: str, b: str) -> int:
    prefix = [0] * len(b)
    matched = 0
    for index in range(1, len(b)):
        while matched > 0 and b[index] != b[matched]:
            matched = prefix[matched - 1]
        if b[index] == b[matched]:
            matched += 1
        prefix[index] = matched

    matched = 0
    for index in range(len(a) + len(b) - 1):
        character = a[index % len(a)]
        while matched > 0 and character != b[matched]:
            matched = prefix[matched - 1]
        if character == b[matched]:
            matched += 1
            if matched == len(b):
                return (index + len(a)) // len(a)

    return -1


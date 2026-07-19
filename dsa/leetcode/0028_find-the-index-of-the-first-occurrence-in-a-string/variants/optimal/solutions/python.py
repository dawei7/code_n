def solve(haystack: str, needle: str) -> int:
    lps = [0] * len(needle)
    border = 0
    for index in range(1, len(needle)):
        while border and needle[index] != needle[border]:
            border = lps[border - 1]
        if needle[index] == needle[border]:
            border += 1
            lps[index] = border

    matched = 0
    for index, char in enumerate(haystack):
        while matched and char != needle[matched]:
            matched = lps[matched - 1]
        if char == needle[matched]:
            matched += 1
            if matched == len(needle):
                return index - len(needle) + 1
    return -1

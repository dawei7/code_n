def solve(haystack: str, needle: str) -> int:
    lps = [0] * len(needle)
    border = 0
    for i in range(1, len(needle)):
        while border and needle[i] != needle[border]:
            border = lps[border - 1]
        if needle[i] == needle[border]:
            border += 1
            lps[i] = border

    matched = 0
    for i, char in enumerate(haystack):
        while matched and char != needle[matched]:
            matched = lps[matched - 1]
        if char == needle[matched]:
            matched += 1
            if matched == len(needle):
                return i - len(needle) + 1
    return -1

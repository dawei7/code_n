def solve(strs: list[str]) -> str:
    common = len(strs[0])
    for word in strs[1:]:
        index = 0
        while index < common and index < len(word) and strs[0][index] == word[index]:
            index += 1
        common = index
        if common == 0:
            return ""
    return strs[0][:common]

def solve(words):
    frequencies = {}
    answer = 0
    for word in words:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord("a"))
        answer += frequencies.get(mask, 0)
        frequencies[mask] = frequencies.get(mask, 0) + 1
    return answer

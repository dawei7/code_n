def solve(word: str) -> int:
    frequencies = [0] * (1 << 10)
    frequencies[0] = 1
    mask = 0
    answer = 0

    for character in word:
        mask ^= 1 << (ord(character) - ord("a"))
        answer += frequencies[mask]
        for bit in range(10):
            answer += frequencies[mask ^ (1 << bit)]
        frequencies[mask] += 1

    return answer

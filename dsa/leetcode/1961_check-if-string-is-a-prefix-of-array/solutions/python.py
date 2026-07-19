def solve(s: str, words: list[str]) -> bool:
    position = 0

    for word in words:
        for character in word:
            if position == len(s) or s[position] != character:
                return False
            position += 1

        if position == len(s):
            return True

    return False

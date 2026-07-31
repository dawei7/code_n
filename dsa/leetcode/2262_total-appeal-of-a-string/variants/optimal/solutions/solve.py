def solve(s: str) -> int:
    last_index = [-1] * 26
    ending_appeal = 0
    total = 0

    for index, character in enumerate(s):
        letter = ord(character) - ord("a")
        ending_appeal += index - last_index[letter]
        total += ending_appeal
        last_index[letter] = index

    return total

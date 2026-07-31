def solve(s: str) -> str:
    vowel_order = "AEIOUaeiou"
    vowel_index = {char: index for index, char in enumerate(vowel_order)}
    counts = [0] * len(vowel_order)

    for char in s:
        index = vowel_index.get(char)
        if index is not None:
            counts[index] += 1

    result = list(s)
    next_vowel = 0
    for index, char in enumerate(result):
        if char not in vowel_index:
            continue
        while counts[next_vowel] == 0:
            next_vowel += 1
        result[index] = vowel_order[next_vowel]
        counts[next_vowel] -= 1

    return "".join(result)

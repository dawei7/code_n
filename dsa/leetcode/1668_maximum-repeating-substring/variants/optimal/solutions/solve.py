def solve(sequence: str, word: str) -> int:
    prefix = [0] * len(word)
    matched = 0
    for index in range(1, len(word)):
        while matched and word[index] != word[matched]:
            matched = prefix[matched - 1]
        if word[index] == word[matched]:
            matched += 1
        prefix[index] = matched

    repeats = [0] * len(sequence)
    matched = 0
    answer = 0
    width = len(word)

    for index, character in enumerate(sequence):
        while matched and character != word[matched]:
            matched = prefix[matched - 1]
        if character == word[matched]:
            matched += 1
        if matched == width:
            repeats[index] = 1 + (repeats[index - width] if index >= width else 0)
            answer = max(answer, repeats[index])
            matched = prefix[matched - 1]

    return answer

from collections import Counter


def solve(words, puzzles):
    counts = Counter()
    for word in words:
        mask = 0
        for ch in set(word):
            mask |= 1 << (ord(ch) - ord("a"))
        if mask.bit_count() <= 7:
            counts[mask] += 1

    answers = []
    for puzzle in puzzles:
        first = 1 << (ord(puzzle[0]) - ord("a"))
        rest = 0
        for ch in puzzle[1:]:
            rest |= 1 << (ord(ch) - ord("a"))
        total = 0
        sub = rest
        while True:
            total += counts[sub | first]
            if sub == 0:
                break
            sub = (sub - 1) & rest
        answers.append(total)
    return answers

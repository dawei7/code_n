def solve(wordsDict: list[str], queries: list[list[str]]) -> list[int]:
    positions: dict[str, list[int]] = {}
    for index, word in enumerate(wordsDict):
        positions.setdefault(word, []).append(index)

    answers: list[int] = []
    for word1, word2 in queries:
        left = positions[word1]
        right = positions[word2]
        i = j = 0
        best = len(wordsDict)
        while i < len(left) and j < len(right):
            best = min(best, abs(left[i] - right[j]))
            if left[i] < right[j]:
                i += 1
            else:
                j += 1
        answers.append(best)
    return answers

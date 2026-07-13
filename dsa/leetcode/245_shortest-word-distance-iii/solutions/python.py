def solve(wordsDict: list[str], word1: str, word2: str) -> int:
    answer = len(wordsDict)
    if word1 == word2:
        previous = -1
        for index, word in enumerate(wordsDict):
            if word == word1:
                if previous >= 0:
                    answer = min(answer, index - previous)
                previous = index
        return answer

    latest1 = latest2 = -1
    for index, word in enumerate(wordsDict):
        if word == word1:
            latest1 = index
        elif word == word2:
            latest2 = index
        if latest1 >= 0 and latest2 >= 0:
            answer = min(answer, abs(latest1 - latest2))
    return answer

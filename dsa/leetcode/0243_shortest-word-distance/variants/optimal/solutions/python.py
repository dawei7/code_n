def solve(wordsDict: list[str], word1: str, word2: str) -> int:
    latest1 = latest2 = -1
    answer = len(wordsDict)
    for index, word in enumerate(wordsDict):
        if word == word1:
            latest1 = index
        elif word == word2:
            latest2 = index
        if latest1 >= 0 and latest2 >= 0:
            answer = min(answer, abs(latest1 - latest2))
    return answer

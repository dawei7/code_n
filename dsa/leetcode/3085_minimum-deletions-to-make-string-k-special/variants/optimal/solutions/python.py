from collections import Counter


def solve(word: str, k: int) -> int:
    frequencies = list(Counter(word).values())
    answer = len(word)

    for minimum in frequencies:
        deletions = 0
        for frequency in frequencies:
            if frequency < minimum:
                deletions += frequency
            elif frequency > minimum + k:
                deletions += frequency - minimum - k
        answer = min(answer, deletions)

    return answer

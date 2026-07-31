from typing import List


def solve(words: List[str], groups: List[int]) -> List[str]:
    count = len(words)
    lengths = [1] * count
    previous = [-1] * count
    best_end = 0

    for end in range(count):
        for start in range(end):
            if groups[start] == groups[end]:
                continue
            if len(words[start]) != len(words[end]):
                continue

            differences = 0
            for left, right in zip(words[start], words[end]):
                if left != right:
                    differences += 1
                    if differences > 1:
                        break

            if differences == 1 and lengths[start] + 1 > lengths[end]:
                lengths[end] = lengths[start] + 1
                previous[end] = start

        if lengths[end] > lengths[best_end]:
            best_end = end

    answer = []
    while best_end != -1:
        answer.append(words[best_end])
        best_end = previous[best_end]
    answer.reverse()
    return answer

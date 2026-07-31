def solve(word: str, forbidden: list[str]) -> int:
    forbidden_set = set(forbidden)
    left = 0
    answer = 0

    for right in range(len(word)):
        earliest = max(left, right - 9)
        for start in range(right, earliest - 1, -1):
            if word[start:right + 1] in forbidden_set:
                left = start + 1
                break

        answer = max(answer, right - left + 1)

    return answer

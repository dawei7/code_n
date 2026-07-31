def solve(s: str) -> list[int]:
    answer: list[int] = []

    for index in range(len(s)):
        representation = str(index)
        start = index - len(representation) + 1
        if start >= 0 and s[start : index + 1] == representation:
            answer.append(index)

    return answer

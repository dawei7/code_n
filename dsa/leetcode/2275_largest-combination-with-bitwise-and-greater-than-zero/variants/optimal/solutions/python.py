def solve(candidates: list[int]) -> int:
    answer = 0
    bit = 1
    maximum = max(candidates)

    while bit <= maximum:
        answer = max(
            answer,
            sum(1 for value in candidates if value & bit),
        )
        bit <<= 1

    return answer

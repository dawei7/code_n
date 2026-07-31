def solve(s: str, num1: int, num2: int) -> int:
    frequencies = {0: 1}
    score = 0
    answer = 0

    for character in s:
        if character == "0":
            score += num2
        else:
            score -= num1
        answer += frequencies.get(score, 0)
        frequencies[score] = frequencies.get(score, 0) + 1

    return answer

import sys


def digit_score(value: int) -> int:
    even = odd = 0
    while value:
        digit = value % 10
        if digit & 1:
            odd += digit
        else:
            even += digit
        value //= 10
    return abs(even - odd)


def build_answers(max_n: int) -> list[int]:
    limit = 2 * max_n + 2
    prefix = [0] * (limit + 1)
    weighted = [0] * (limit + 1)
    for value in range(1, limit + 1):
        score = digit_score(value)
        prefix[value] = prefix[value - 1] + score
        weighted[value] = weighted[value - 1] + score * value

    answers = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        first = (weighted[n + 1] - weighted[1]) - (prefix[n + 1] - prefix[1])
        sum_v = prefix[2 * n] - prefix[n + 1]
        sum_w = weighted[2 * n] - weighted[n + 1]
        second = (2 * n + 1) * sum_v - sum_w
        answers[n] = first + second
    return answers


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    queries = data[1:]
    answers = build_answers(max(queries, default=0))
    sys.stdout.write("\n".join(str(answers[n]) for n in queries))


if __name__ == "__main__":
    main()

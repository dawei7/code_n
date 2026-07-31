def solve(n: int) -> list[list[int]]:
    odd = list(range(1, n + 1, 2))
    even = list(range(2, n + 1, 2))
    answers: list[list[int]] = []
    path: list[int] = []

    def generate(used: int) -> None:
        if len(path) == n:
            answers.append(path.copy())
            return

        if not path:
            candidates = odd if n % 2 else range(1, n + 1)
        elif path[-1] % 2:
            candidates = even
        else:
            candidates = odd

        for value in candidates:
            bit = 1 << (value - 1)
            if used & bit == 0:
                path.append(value)
                generate(used | bit)
                path.pop()

    generate(0)
    return answers

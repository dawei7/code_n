def solve(n: int) -> list[list[int]]:
    combinations: list[list[int]] = []

    def search(remainder: int, minimum: int, path: list[int]) -> None:
        factor = minimum
        while factor * factor <= remainder:
            if remainder % factor == 0:
                quotient = remainder // factor
                combinations.append(path + [factor, quotient])
                search(quotient, factor, path + [factor])
            factor += 1

    search(n, 2, [])
    return combinations

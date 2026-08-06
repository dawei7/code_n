from functools import lru_cache


def solve(expression: str) -> list[int]:
    @lru_cache(maxsize=None)
    def evaluate(part: str) -> tuple[int, ...]:
        results: list[int] = []

        for i, operator in enumerate(part):
            if operator not in "+-*":
                continue

            for left in evaluate(part[:i]):
                for right in evaluate(part[i + 1 :]):
                    if operator == "+":
                        results.append(left + right)
                    elif operator == "-":
                        results.append(left - right)
                    else:
                        results.append(left * right)

        return tuple(results) if results else (int(part),)

    return list(evaluate(expression))

from functools import lru_cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @lru_cache(maxsize=None)
        def evaluate(part: str) -> tuple[int, ...]:
            results = []
            for index, operator in enumerate(part):
                if operator not in "+-*":
                    continue
                for left in evaluate(part[:index]):
                    for right in evaluate(part[index + 1 :]):
                        if operator == "+":
                            results.append(left + right)
                        elif operator == "-":
                            results.append(left - right)
                        else:
                            results.append(left * right)
            return tuple(results) if results else (int(part),)

        return list(evaluate(expression))

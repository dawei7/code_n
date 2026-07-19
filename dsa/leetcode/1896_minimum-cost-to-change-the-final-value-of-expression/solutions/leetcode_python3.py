from typing import Optional, Tuple


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def combine(
            left: Tuple[int, int],
            right: Tuple[int, int],
            operator: str,
        ) -> Tuple[int, int]:
            costs = [10**9, 10**9]
            for left_value in (0, 1):
                for right_value in (0, 1):
                    base = left[left_value] + right[right_value]
                    for chosen_operator in ("&", "|"):
                        result = (
                            left_value & right_value
                            if chosen_operator == "&"
                            else left_value | right_value
                        )
                        costs[result] = min(
                            costs[result],
                            base + (chosen_operator != operator),
                        )
            return costs[0], costs[1]

        stack: list[tuple[Optional[Tuple[int, int]], Optional[str]]] = []
        current: Optional[Tuple[int, int]] = None
        operator: Optional[str] = None

        for token in expression:
            if token in "01":
                term = (0, 1) if token == "0" else (1, 0)
                if current is None:
                    current = term
                else:
                    current = combine(current, term, operator or "")
                    operator = None
            elif token in "&|":
                operator = token
            elif token == "(":
                stack.append((current, operator))
                current = None
                operator = None
            else:
                term = current
                outer_value, outer_operator = stack.pop()
                if outer_value is None:
                    current = term
                else:
                    current = combine(outer_value, term or (0, 0), outer_operator or "")
                operator = None

        if current is None:
            raise RuntimeError("a valid expression must produce a value")
        return current[1] if current[0] == 0 else current[0]

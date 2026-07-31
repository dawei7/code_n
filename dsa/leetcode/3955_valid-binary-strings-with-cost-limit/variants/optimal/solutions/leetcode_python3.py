class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        valid_strings = []
        path = []

        def backtrack(index: int, cost: int, previous_one: bool) -> None:
            if index == n:
                valid_strings.append("".join(path))
                return

            path.append("0")
            backtrack(index + 1, cost, False)
            path.pop()

            if not previous_one and cost + index <= k:
                path.append("1")
                backtrack(index + 1, cost + index, True)
                path.pop()

        backtrack(0, 0, False)
        return valid_strings

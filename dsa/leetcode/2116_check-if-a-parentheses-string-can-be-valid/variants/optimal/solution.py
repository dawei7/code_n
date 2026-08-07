class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        minimum_open = 0
        maximum_open = 0

        for character, state in zip(s, locked):
            if state == "0":
                minimum_open -= 1
                maximum_open += 1
            elif character == "(":
                minimum_open += 1
                maximum_open += 1
            else:
                minimum_open -= 1
                maximum_open -= 1

            if maximum_open < 0:
                return False
            minimum_open = max(minimum_open, 0)

        return minimum_open == 0

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        additions = 0

        for character in s:
            if character == "(":
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                additions += 1

        return additions + open_count


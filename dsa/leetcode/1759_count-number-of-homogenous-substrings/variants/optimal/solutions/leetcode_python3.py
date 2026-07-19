class Solution:
    def countHomogenous(self, s: str) -> int:
        modulus = 1_000_000_007
        total = 0
        run_length = 0
        previous = ""

        for character in s:
            if character == previous:
                run_length += 1
            else:
                previous = character
                run_length = 1
            total = (total + run_length) % modulus

        return total

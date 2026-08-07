class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        value = {}
        for digit, letters in enumerate(
            ("ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"),
            start=1,
        ):
            for letter in letters:
                value[letter] = digit

        answer = 0
        for average in range(1, 10):
            balance = 0
            frequency = {0: 1}
            for character in word:
                balance += value[character] - average
                answer += frequency.get(balance, 0)
                frequency[balance] = frequency.get(balance, 0) + 1

        return answer

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remainder = 0
        answer = []

        for digit in word:
            remainder = (remainder * 10 + ord(digit) - ord("0")) % m
            answer.append(int(remainder == 0))

        return answer

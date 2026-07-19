class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest_after_replacing(replaced: str) -> int:
            left = 0
            replacements = 0
            best = 0

            for right, answer in enumerate(answerKey):
                if answer == replaced:
                    replacements += 1
                while replacements > k:
                    if answerKey[left] == replaced:
                        replacements -= 1
                    left += 1
                best = max(best, right - left + 1)

            return best

        return max(longest_after_replacing("F"), longest_after_replacing("T"))

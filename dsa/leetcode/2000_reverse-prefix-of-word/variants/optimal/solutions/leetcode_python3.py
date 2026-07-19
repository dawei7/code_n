class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        boundary = word.find(ch)
        if boundary == -1:
            return word
        return word[: boundary + 1][::-1] + word[boundary + 1 :]

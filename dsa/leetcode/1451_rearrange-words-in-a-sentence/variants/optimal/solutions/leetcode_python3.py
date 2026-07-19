class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key=len)
        arranged = " ".join(words)
        return arranged[0].upper() + arranged[1:]

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        characters = list(s)
        for start in range(0, len(characters), 2 * k):
            end = min(start + k, len(characters))
            characters[start:end] = reversed(characters[start:end])
        return "".join(characters)

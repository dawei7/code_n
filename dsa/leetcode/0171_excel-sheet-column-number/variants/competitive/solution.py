class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for character in columnTitle:
            total = total * 26 + ord(character) - ord("A") + 1
        return total

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        middle = len(s) // 2
        balance = 0

        for index, character in enumerate(s):
            if character in vowels:
                balance += 1 if index < middle else -1

        return balance == 0

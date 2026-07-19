class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        characters = list(palindrome)
        for index in range(len(characters) // 2):
            if characters[index] != "a":
                characters[index] = "a"
                return "".join(characters)
        characters[-1] = "b"
        return "".join(characters)

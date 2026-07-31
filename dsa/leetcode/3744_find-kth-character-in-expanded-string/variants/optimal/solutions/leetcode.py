class Solution:
    def kthCharacter(self, s: str, k: int) -> str:
        position_in_word = 1

        for character in s:
            if character == " ":
                if k == 0:
                    return character
                k -= 1
                position_in_word = 1
            else:
                if k < position_in_word:
                    return character
                k -= position_in_word
                position_in_word += 1

        return ""

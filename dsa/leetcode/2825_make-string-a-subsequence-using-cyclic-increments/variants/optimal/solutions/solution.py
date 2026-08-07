class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        target_index = 0

        for char in str1:
            if target_index == len(str2):
                return True

            next_char = chr((ord(char) - ord("a") + 1) % 26 + ord("a"))
            if char == str2[target_index] or next_char == str2[target_index]:
                target_index += 1

        return target_index == len(str2)

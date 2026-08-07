class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        operations = 0
        index = 1

        while index < len(word):
            if abs(ord(word[index]) - ord(word[index - 1])) <= 1:
                operations += 1
                index += 2
            else:
                index += 1

        return operations

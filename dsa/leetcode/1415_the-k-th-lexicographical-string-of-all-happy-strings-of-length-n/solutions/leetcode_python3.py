class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""

        answer = []
        previous = ""
        for index in range(n):
            choices = [character for character in "abc" if character != previous]
            block_size = 1 << (n - index - 1)
            block = (k - 1) // block_size
            character = choices[block]
            answer.append(character)
            previous = character
            k -= block * block_size
        return "".join(answer)

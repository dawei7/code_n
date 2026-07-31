class Solution:
    def robotWithString(self, s: str) -> str:
        remaining = [0] * 26
        for character in s:
            remaining[ord(character) - ord("a")] += 1

        stack = []
        written = []
        smallest = 0

        for character in s:
            index = ord(character) - ord("a")
            stack.append(character)
            remaining[index] -= 1
            while smallest < 26 and remaining[smallest] == 0:
                smallest += 1
            while stack and (smallest == 26 or ord(stack[-1]) - ord("a") <= smallest):
                written.append(stack.pop())

        return "".join(written)

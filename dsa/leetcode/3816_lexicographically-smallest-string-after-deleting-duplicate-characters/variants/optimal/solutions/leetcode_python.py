class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        remaining = [0] * 26
        for char in s:
            remaining[ord(char) - ord("a")] += 1

        kept = [0] * 26
        stack = []

        for char in s:
            char_index = ord(char) - ord("a")
            remaining[char_index] -= 1

            while stack and stack[-1] > char:
                top_index = ord(stack[-1]) - ord("a")
                if kept[top_index] + remaining[top_index] == 1:
                    break
                kept[top_index] -= 1
                stack.pop()

            stack.append(char)
            kept[char_index] += 1

        while stack:
            top_index = ord(stack[-1]) - ord("a")
            if kept[top_index] == 1:
                break
            kept[top_index] -= 1
            stack.pop()

        return "".join(stack)

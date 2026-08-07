from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        text = deque()
        reversed_order = False

        for character in s:
            if character == "i":
                reversed_order = not reversed_order
            elif reversed_order:
                text.appendleft(character)
            else:
                text.append(character)

        if reversed_order:
            text.reverse()
        return "".join(text)

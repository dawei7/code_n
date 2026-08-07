class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {character: index for index, character in enumerate(s)}
        stack = []
        included = set()

        for index, character in enumerate(s):
            if character in included:
                continue
            while stack and stack[-1] > character and last_index[stack[-1]] > index:
                included.remove(stack.pop())
            stack.append(character)
            included.add(character)

        return "".join(stack)

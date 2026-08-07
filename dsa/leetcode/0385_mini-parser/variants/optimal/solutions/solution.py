class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))

        root = NestedInteger()
        stack = [root]
        number_start = None

        for index, character in enumerate(s):
            if character == "[":
                if index > 0:
                    nested = NestedInteger()
                    stack[-1].add(nested)
                    stack.append(nested)
            elif character == "," or character == "]":
                if number_start is not None:
                    stack[-1].add(NestedInteger(int(s[number_start:index])))
                    number_start = None
                if character == "]" and len(stack) > 1:
                    stack.pop()
            elif number_start is None:
                number_start = index

        return root

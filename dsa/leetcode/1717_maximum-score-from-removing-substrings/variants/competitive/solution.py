class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            first, second = "ab", "ba"
            first_score, second_score = x, y
        else:
            first, second = "ba", "ab"
            first_score, second_score = y, x

        def remove_pair(text: str, pair: str, score: int) -> tuple[str, int]:
            stack = []
            gained = 0
            for character in text:
                if stack and stack[-1] == pair[0] and character == pair[1]:
                    stack.pop()
                    gained += score
                else:
                    stack.append(character)
            return "".join(stack), gained

        remaining, total = remove_pair(s, first, first_score)
        _, gained = remove_pair(remaining, second, second_score)
        return total + gained

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []

        for start in range(0, len(s), k):
            group_sum = 0
            for index in range(start, start + k):
                group_sum += ord(s[index]) - ord('a')
            result.append(chr(ord('a') + group_sum % 26))

        return "".join(result)

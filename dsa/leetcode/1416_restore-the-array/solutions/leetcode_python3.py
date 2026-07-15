class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulus = 1_000_000_007
        length = len(s)
        max_digits = len(str(k))
        ways = [0] * (length + 1)
        ways[length] = 1

        for start in range(length - 1, -1, -1):
            if s[start] == "0":
                continue
            value = 0
            for end in range(start, min(length, start + max_digits)):
                value = value * 10 + ord(s[end]) - ord("0")
                if value > k:
                    break
                ways[start] = (ways[start] + ways[end + 1]) % modulus
        return ways[0]

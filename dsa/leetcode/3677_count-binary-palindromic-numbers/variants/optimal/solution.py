class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        length = n.bit_length()
        answer = 1

        for shorter_length in range(1, length):
            answer += 1 << ((shorter_length - 1) // 2)

        half_length = (length + 1) // 2
        prefix = n >> (length - half_length)
        answer += prefix - (1 << (half_length - 1))

        palindrome = prefix
        remaining = prefix >> (length & 1)
        while remaining:
            palindrome = (palindrome << 1) | (remaining & 1)
            remaining >>= 1

        if palindrome <= n:
            answer += 1

        return answer

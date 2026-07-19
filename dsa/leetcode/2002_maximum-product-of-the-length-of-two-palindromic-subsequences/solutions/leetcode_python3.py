class Solution:
    def maxProduct(self, s: str) -> int:
        length = len(s)
        limit = 1 << length
        palindrome_length = [0] * limit

        for mask in range(1, limit):
            subsequence = [
                s[index] for index in range(length) if mask & (1 << index)
            ]
            if subsequence == subsequence[::-1]:
                palindrome_length[mask] = len(subsequence)

        best_submask = palindrome_length.copy()
        for index in range(length):
            bit = 1 << index
            for mask in range(limit):
                if mask & bit:
                    best_submask[mask] = max(
                        best_submask[mask],
                        best_submask[mask ^ bit],
                    )

        full_mask = limit - 1
        return max(
            palindrome_length[mask] * best_submask[full_mask ^ mask]
            for mask in range(limit)
        )

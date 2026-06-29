


def solve():
    def longestValidSubstring(s):
        freq = [0] * 26
        left = 0
        max_len = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')
            limit = idx + 1

            freq[idx] += 1

            while freq[idx] > limit:
                left_idx = ord(s[left]) - ord('a')
                freq[left_idx] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solve()

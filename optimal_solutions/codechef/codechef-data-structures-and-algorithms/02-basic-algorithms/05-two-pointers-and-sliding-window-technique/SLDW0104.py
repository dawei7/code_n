


def solve():
    class Solution:
        def findMaxSubstring(self, s: str) -> int:
            n = len(s)
            left = 0
            right = 0
            mp = {}
            max_size = float('-inf')

            while right < n:
                mp[s[right]] = mp.get(s[right], 0) + 1

                while mp[s[right]] > (ord(s[right]) - ord('a') + 1):
                    mp[s[left]] -= 1
                    left += 1

                max_size = max(max_size, right - left + 1)
                right += 1

            return max_size


if __name__ == "__main__":
    solve()

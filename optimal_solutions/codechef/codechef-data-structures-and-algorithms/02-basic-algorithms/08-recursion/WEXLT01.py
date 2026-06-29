


def solve():
    class Solution:

        def is_palindrome(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(self, index, s, path, result):
            if index == len(s):
                result.append(path[:])
                return

            for end in range(index, len(s)):
                if self.is_palindrome(s, index, end):
                    path.append(s[index:end + 1])
                    self.backtrack(end + 1, s, path, result)
                    path.pop()

        def partitionString(self, inputString):
            result = []
            self.backtrack(0, inputString, [], result)
            return result


if __name__ == "__main__":
    solve()




def solve():
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def valid_palindrome(s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Check by skipping either left character or right character
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True

    if __name__ == "__main__":
        import sys
        input = sys.stdin.read
        data = input().split()

        n = int(data[0])
        s = data[1]
        print("true" if valid_palindrome(s) else "false")


if __name__ == "__main__":
    solve()

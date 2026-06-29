


def solve():
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def find_longest_palindrome(s):
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expand_around_center(s, i, i)
            if len(odd) > len(longest):
                longest = odd

            # Even length palindrome
            even = expand_around_center(s, i, i + 1)
            if len(even) > len(longest):
                longest = even
        return longest


if __name__ == "__main__":
    solve()

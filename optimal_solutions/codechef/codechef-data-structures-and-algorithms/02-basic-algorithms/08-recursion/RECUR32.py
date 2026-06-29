


def solve():
    def longest_palindromic_subsequence(s, start, end):
        # Base cases
        if start > end:
            return 0  # If the start index is greater than the end, return 0
        if start == end:
            return 1  # A single character is a palindrome of length 1

        # If the characters at the start and end indices match
        if s[start] == s[end]:
            return 2 + longest_palindromic_subsequence(s, start + 1, end - 1)
        else:
            # If the characters do not match, we have two options:
            # 1. Exclude the current start character and recurse
            # 2. Exclude the current end character and recurse
            return max(longest_palindromic_subsequence(s, start + 1, end),
                       longest_palindromic_subsequence(s, start, end - 1))

    # Main function
    if __name__ == "__main__":
        s = input()
        result = longest_palindromic_subsequence(s, 0, len(s) - 1)
        print(result)


if __name__ == "__main__":
    solve()

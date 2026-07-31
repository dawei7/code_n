def solve(s: str) -> int:
    n = len(s)
    longest = 0

    def expand(left: int, right: int) -> None:
        nonlocal longest

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        palindrome_length = right - left - 1
        longest = max(longest, palindrome_length)

        if left >= 0 or right < n:
            longest = max(longest, palindrome_length + 1)

        if left < 0 or right >= n:
            return

        skip_left = left - 1
        keep_right = right
        candidate_length = palindrome_length + 1
        while skip_left >= 0 and keep_right < n and s[skip_left] == s[keep_right]:
            skip_left -= 1
            keep_right += 1
            candidate_length += 2
        longest = max(longest, candidate_length)

        keep_left = left
        skip_right = right + 1
        candidate_length = palindrome_length + 1
        while keep_left >= 0 and skip_right < n and s[keep_left] == s[skip_right]:
            keep_left -= 1
            skip_right += 1
            candidate_length += 2
        longest = max(longest, candidate_length)

    for center in range(n):
        expand(center - 1, center + 1)
        expand(center - 1, center)

    return longest

def solve(s: str, t: str) -> int:
    def longest_palindrome_from(text: str) -> list[int]:
        longest = [1] * len(text)

        for center in range(len(text)):
            left = right = center
            while left >= 0 and right < len(text) and text[left] == text[right]:
                longest[left] = max(longest[left], right - left + 1)
                left -= 1
                right += 1

            left, right = center, center + 1
            while left >= 0 and right < len(text) and text[left] == text[right]:
                longest[left] = max(longest[left], right - left + 1)
                left -= 1
                right += 1

        return longest

    reversed_t = t[::-1]
    palindrome_s = longest_palindrome_from(s)
    palindrome_t = longest_palindrome_from(reversed_t)
    answer = max(max(palindrome_s), max(palindrome_t))

    next_row = [0] * (len(t) + 1)
    for i in range(len(s) - 1, -1, -1):
        current_row = [0] * (len(t) + 1)
        for j in range(len(t) - 1, -1, -1):
            if s[i] != reversed_t[j]:
                continue

            middle_s = palindrome_s[i + 1] if i + 1 < len(s) else 0
            middle_t = palindrome_t[j + 1] if j + 1 < len(t) else 0
            current_row[j] = 2 + max(
                middle_s,
                middle_t,
                next_row[j + 1],
            )
            answer = max(answer, current_row[j])

        next_row = current_row

    return answer

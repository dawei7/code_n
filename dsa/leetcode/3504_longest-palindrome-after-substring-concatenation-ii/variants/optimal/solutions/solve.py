def solve(s: str, t: str) -> int:
    def longest_palindrome_from(text: str) -> list[int]:
        length = len(text)
        odd = [0] * length
        left, right = 0, -1

        for center in range(length):
            radius = 1 if center > right else min(odd[left + right - center], right - center + 1)
            while center - radius >= 0 and center + radius < length and text[center - radius] == text[center + radius]:
                radius += 1
            odd[center] = radius
            if center + radius - 1 > right:
                left = center - radius + 1
                right = center + radius - 1

        even = [0] * length
        left, right = 0, -1
        for center in range(length):
            radius = 0 if center > right else min(even[left + right - center + 1], right - center + 1)
            while (
                center - radius - 1 >= 0
                and center + radius < length
                and text[center - radius - 1] == text[center + radius]
            ):
                radius += 1
            even[center] = radius
            if center + radius - 1 > right:
                left = center - radius
                right = center + radius - 1

        longest = [1] * length
        for center, radius in enumerate(odd):
            start = center - radius + 1
            longest[start] = max(longest[start], 2 * radius - 1)
        for center, radius in enumerate(even):
            if radius:
                start = center - radius
                longest[start] = max(longest[start], 2 * radius)

        for start in range(1, length):
            longest[start] = max(longest[start], longest[start - 1] - 2)

        return longest

    reversed_t = t[::-1]
    palindrome_s = longest_palindrome_from(s)
    palindrome_t = longest_palindrome_from(reversed_t)
    answer = max(max(palindrome_s), max(palindrome_t))

    next_row = [0] * (len(t) + 1)
    for i in range(len(s) - 1, -1, -1):
        current_row = [0] * (len(t) + 1)
        middle_s = palindrome_s[i + 1] if i + 1 < len(s) else 0

        for j in range(len(t) - 1, -1, -1):
            if s[i] != reversed_t[j]:
                continue

            middle_t = palindrome_t[j + 1] if j + 1 < len(t) else 0
            current_row[j] = 2 + max(
                middle_s,
                middle_t,
                next_row[j + 1],
            )
            answer = max(answer, current_row[j])

        next_row = current_row

    return answer

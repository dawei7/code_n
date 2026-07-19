def solve(s: str) -> bool:
    length = len(s)
    palindrome = [[False] * length for _ in range(length)]

    for left in range(length - 1, -1, -1):
        for right in range(left, length):
            palindrome[left][right] = (
                s[left] == s[right]
                and (right - left < 2 or palindrome[left + 1][right - 1])
            )

    for first in range(length - 2):
        if not palindrome[0][first]:
            continue
        for second in range(first + 1, length - 1):
            if (
                palindrome[first + 1][second]
                and palindrome[second + 1][length - 1]
            ):
                return True

    return False

def solve(s: str) -> list[list[str]]:
    size = len(s)
    palindrome = [[False] * size for _ in range(size)]
    for right in range(size):
        for left in range(right, -1, -1):
            palindrome[left][right] = s[left] == s[right] and (
                right - left < 2 or palindrome[left + 1][right - 1]
            )

    result: list[list[str]] = []
    path: list[str] = []

    def partition(start: int) -> None:
        if start == size:
            result.append(path.copy())
            return
        for end in range(start, size):
            if not palindrome[start][end]:
                continue
            path.append(s[start:end + 1])
            partition(end + 1)
            path.pop()

    partition(0)
    return result

def _reverse(s: list[str], left: int, right: int) -> None:
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def solve(s: list[str]) -> None:
    _reverse(s, 0, len(s) - 1)

    start = 0
    for end in range(len(s) + 1):
        if end == len(s) or s[end] == " ":
            _reverse(s, start, end - 1)
            start = end + 1

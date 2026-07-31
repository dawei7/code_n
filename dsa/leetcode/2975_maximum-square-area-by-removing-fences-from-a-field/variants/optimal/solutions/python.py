from typing import List


def solve(m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    horizontal = sorted([1, m, *hFences])
    vertical = sorted([1, n, *vFences])

    horizontal_spans = {
        horizontal[right] - horizontal[left]
        for right in range(1, len(horizontal))
        for left in range(right)
    }
    vertical_spans = {
        vertical[right] - vertical[left]
        for right in range(1, len(vertical))
        for left in range(right)
    }

    common = horizontal_spans & vertical_spans
    if not common:
        return -1

    side = max(common)
    return side * side % 1_000_000_007

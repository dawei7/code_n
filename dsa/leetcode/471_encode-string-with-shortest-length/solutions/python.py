"""Interval dynamic programming for LeetCode 471."""


def solve(s: str) -> str:
    length = len(s)
    best = [[""] * length for _ in range(length)]
    for width in range(1, length + 1):
        for left in range(length - width + 1):
            right = left + width - 1
            text = s[left : right + 1]
            answer = text

            for split in range(left, right):
                candidate = best[left][split] + best[split + 1][right]
                if len(candidate) < len(answer):
                    answer = candidate

            period = (text + text).find(text, 1)
            if period < width and width % period == 0:
                unit = best[left][left + period - 1]
                candidate = f"{width // period}[{unit}]"
                if len(candidate) < len(answer):
                    answer = candidate
            best[left][right] = answer
    return best[0][length - 1]

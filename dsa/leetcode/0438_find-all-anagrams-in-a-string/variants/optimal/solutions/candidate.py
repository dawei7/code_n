def solve(s: str, p: str) -> list[int]:
    window_length = len(p)
    if window_length > len(s):
        return []

    offset = ord("a")
    pattern_counts = [0] * 26
    window_counts = [0] * 26
    for x, y in zip(p, s):
        pattern_counts[ord(x) - offset] += 1
        window_counts[ord(y) - offset] += 1

    answer = [0] if window_counts == pattern_counts else []
    for right in range(window_length, len(s)):
        left = right - window_length
        window_counts[ord(s[left]) - offset] -= 1
        window_counts[ord(s[right]) - offset] += 1
        if window_counts == pattern_counts:
            answer.append(left + 1)
    return answer

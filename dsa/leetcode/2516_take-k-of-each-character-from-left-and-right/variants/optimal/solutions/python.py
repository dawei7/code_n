def solve(s: str, k: int) -> int:
    total = [0, 0, 0]
    for character in s:
        total[ord(character) - ord("a")] += 1

    if any(count < k for count in total):
        return -1

    allowed = [count - k for count in total]
    window = [0, 0, 0]
    left = 0
    longest_kept = 0

    for right, character in enumerate(s):
        index = ord(character) - ord("a")
        window[index] += 1

        while window[index] > allowed[index]:
            window[ord(s[left]) - ord("a")] -= 1
            left += 1

        longest_kept = max(longest_kept, right - left + 1)

    return len(s) - longest_kept

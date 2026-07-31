def solve(s: str, k: int) -> int:
    counts = [0, 0]
    left = 0
    answer = 0

    for right, bit in enumerate(s):
        counts[int(bit)] += 1
        while counts[0] > k and counts[1] > k:
            counts[int(s[left])] -= 1
            left += 1
        answer += right - left + 1

    return answer

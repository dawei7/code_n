def solve(s: str) -> int:
    counts = [0] * 26
    left = 0
    answer = 0

    for right, char in enumerate(s):
        index = ord(char) - ord("a")
        counts[index] += 1

        while counts[index] > 2:
            counts[ord(s[left]) - ord("a")] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer

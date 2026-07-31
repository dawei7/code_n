def solve(s: str) -> int:
    n = len(s)
    first = [n] * 26
    last = [-1] * 26

    for index, character in enumerate(s):
        code = ord(character) - ord("a")
        first[code] = min(first[code], index)
        last[code] = index

    answer = -1
    for left, character in enumerate(s):
        if first[ord(character) - ord("a")] != left:
            continue

        required_right = -1
        for right in range(left, n):
            code = ord(s[right]) - ord("a")
            if first[code] < left:
                break
            required_right = max(required_right, last[code])
            if right >= required_right and (left > 0 or right < n - 1):
                answer = max(answer, right - left + 1)

    return answer

def solve(s: str) -> int:
    seen: set[tuple[int, int, int]] = set()
    mod1 = 1_000_000_007
    mod2 = 1_000_000_009

    for left in range(len(s)):
        counts = [0] * 10
        distinct = 0
        maximum = 0
        hash1 = 0
        hash2 = 0

        for right in range(left, len(s)):
            digit = ord(s[right]) - ord("0")
            if counts[digit] == 0:
                distinct += 1
            counts[digit] += 1
            maximum = max(maximum, counts[digit])
            hash1 = (hash1 * 11 + digit + 1) % mod1
            hash2 = (hash2 * 11 + digit + 1) % mod2

            length = right - left + 1
            if maximum * distinct == length:
                seen.add((length, hash1, hash2))

    return len(seen)

def solve(s: str, t: int) -> int:
    modulus = 1_000_000_007
    counts = [0] * 26

    for character in s:
        counts[ord(character) - ord("a")] += 1

    for _ in range(t):
        next_counts = [0] * 26
        for character in range(25):
            next_counts[character + 1] = counts[character]
        next_counts[0] = counts[25]
        next_counts[1] = (next_counts[1] + counts[25]) % modulus
        counts = next_counts

    return sum(counts) % modulus

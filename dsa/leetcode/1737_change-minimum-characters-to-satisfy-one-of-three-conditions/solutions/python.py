def solve(a: str, b: str) -> int:
    counts_a = [0] * 26
    counts_b = [0] * 26
    for character in a:
        counts_a[ord(character) - ord("a")] += 1
    for character in b:
        counts_b[ord(character) - ord("a")] += 1

    total = len(a) + len(b)
    answer = total - max(
        counts_a[index] + counts_b[index]
        for index in range(26)
    )

    prefix_a = 0
    prefix_b = 0
    for boundary in range(25):
        prefix_a += counts_a[boundary]
        prefix_b += counts_b[boundary]
        answer = min(
            answer,
            len(a) - prefix_a + prefix_b,
            len(b) - prefix_b + prefix_a,
        )

    return answer

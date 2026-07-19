def solve(s: str, queries: list[list[int]]) -> list[bool]:
    n = len(s)
    half = n // 2
    left = s[:half]
    right = s[half:][::-1]

    def prefix_counts(t: str) -> list[list[int]]:
        pref = [[0] * 26 for _ in range(len(t) + 1)]
        for i, char in enumerate(t):
            for j in range(26):
                pref[i + 1][j] = pref[i][j]
            pref[i + 1][ord(char) - ord("a")] += 1
        return pref

    left_pref = prefix_counts(left)
    right_pref = prefix_counts(right)
    mismatch_pref = [0] * (half + 1)
    for i in range(half):
        mismatch_pref[i + 1] = mismatch_pref[i] + (left[i] != right[i])

    def counts(pref: list[list[int]], l: int, r: int) -> list[int]:
        if l > r:
            return [0] * 26
        return [pref[r + 1][i] - pref[l][i] for i in range(26)]

    def subtract(a: list[int], b: list[int]) -> list[int]:
        return [a[i] - b[i] for i in range(26)]

    def interval_count(pref: list[list[int]], intervals: list[tuple[int, int]]) -> list[int]:
        total = [0] * 26
        for l, r in intervals:
            if l <= r:
                cur = counts(pref, l, r)
                for i in range(26):
                    total[i] += cur[i]
        return total

    def difference(base: tuple[int, int], remove: tuple[int, int]) -> list[tuple[int, int]]:
        l, r = base
        x, y = remove
        pieces = []
        if l <= min(r, x - 1):
            pieces.append((l, min(r, x - 1)))
        if max(l, y + 1) <= r:
            pieces.append((max(l, y + 1), r))
        return pieces

    def mismatches(l: int, r: int) -> int:
        if l > r:
            return 0
        return mismatch_pref[r + 1] - mismatch_pref[l]

    results = []
    for a, b, c, d in queries:
        # Map the selected range in the original right half to the reversed
        # right-half coordinate system used for palindrome comparison.
        c, d = n - 1 - d, n - 1 - c
        first = (a, b)
        second = (c, d)

        union_mismatches = mismatches(a, b) + mismatches(c, d) - mismatches(max(a, c), min(b, d))
        if mismatch_pref[half] != union_mismatches:
            results.append(False)
            continue

        left_available = counts(left_pref, a, b)
        right_available = counts(right_pref, c, d)
        left_fixed_need = interval_count(right_pref, difference(first, second))
        right_fixed_need = interval_count(left_pref, difference(second, first))

        left_remaining = subtract(left_available, left_fixed_need)
        right_remaining = subtract(right_available, right_fixed_need)
        results.append(
            all(value >= 0 for value in left_remaining)
            and all(value >= 0 for value in right_remaining)
            and left_remaining == right_remaining
        )

    return results

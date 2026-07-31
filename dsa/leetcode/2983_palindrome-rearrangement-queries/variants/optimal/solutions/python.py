def solve(s, queries):
    half = len(s) // 2
    left, right = s[:half], s[half:][::-1]

    def build_counts(text):
        prefix = [[0] * 26]
        for character in text:
            row = prefix[-1].copy()
            row[ord(character) - ord("a")] += 1
            prefix.append(row)
        return prefix

    left_counts, right_counts = build_counts(left), build_counts(right)
    mismatch = [0]
    for first, second in zip(left, right):
        mismatch.append(mismatch[-1] + (first != second))

    def counts(prefix, low, high):
        if low > high:
            return [0] * 26
        return [prefix[high + 1][i] - prefix[low][i] for i in range(26)]

    answer = []
    size = len(s)
    for first_low, first_high, second_low, second_high in queries:
        second_low, second_high = size - 1 - second_high, size - 1 - second_low
        overlap_low, overlap_high = max(first_low, second_low), min(first_high, second_high)
        covered = mismatch[first_high + 1] - mismatch[first_low] + mismatch[second_high + 1] - mismatch[second_low]
        if overlap_low <= overlap_high:
            covered -= mismatch[overlap_high + 1] - mismatch[overlap_low]
        if mismatch[half] != covered:
            answer.append(False)
            continue
        left_supply = counts(left_counts, first_low, first_high)
        right_supply = counts(right_counts, second_low, second_high)
        right_fixed = counts(right_counts, first_low, first_high)
        left_fixed = counts(left_counts, second_low, second_high)
        if overlap_low <= overlap_high:
            right_overlap = counts(right_counts, overlap_low, overlap_high)
            left_overlap = counts(left_counts, overlap_low, overlap_high)
            right_fixed = [a - b for a, b in zip(right_fixed, right_overlap)]
            left_fixed = [a - b for a, b in zip(left_fixed, left_overlap)]
        left_remaining = [a - b for a, b in zip(left_supply, right_fixed)]
        right_remaining = [a - b for a, b in zip(right_supply, left_fixed)]
        answer.append(min(left_remaining) >= 0 and min(right_remaining) >= 0 and left_remaining == right_remaining)
    return answer

def solve(word: str, k: int) -> int:
    modulus = 1_000_000_007
    short_run_lengths = []
    run_count = 0
    run_length = 1
    total = 1

    for index in range(1, len(word)):
        if word[index] == word[index - 1]:
            run_length += 1
        else:
            total = total * run_length % modulus
            run_count += 1
            if run_count < k:
                short_run_lengths.append(run_length)
            run_length = 1

    total = total * run_length % modulus
    run_count += 1
    if run_count < k:
        short_run_lengths.append(run_length)

    if run_count >= k:
        return total

    counts = [0] * k
    counts[0] = 1

    for length in short_run_lengths:
        next_counts = [0] * k
        window = 0
        for original_length in range(1, k):
            window += counts[original_length - 1]
            removed = original_length - length - 1
            if removed >= 0:
                window -= counts[removed]
            next_counts[original_length] = window % modulus
        counts = next_counts

    invalid = sum(counts) % modulus
    return (total - invalid) % modulus

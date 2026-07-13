def solve(tasks: list[str], n: int) -> int:
    counts = [0] * 26
    for task in tasks:
        counts[ord(task) - ord("A")] += 1

    maximum = max(counts)
    leaders = sum(frequency == maximum for frequency in counts)
    frame_bound = (maximum - 1) * (n + 1) + leaders
    return max(len(tasks), frame_bound)

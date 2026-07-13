from collections import Counter


def solve(nums: list[int], k: int, numOperations: int) -> int:
    counts = Counter(nums)
    events = []
    candidates = set()

    for value, frequency in counts.items():
        left = value - k
        right = value + k
        events.append((left, frequency))
        events.append((right + 1, -frequency))
        candidates.add(left)
        candidates.add(right)
        candidates.add(value)

    events.sort()
    event_index = 0
    reachable = 0
    best = 0

    for target in sorted(candidates):
        while event_index < len(events) and events[event_index][0] <= target:
            reachable += events[event_index][1]
            event_index += 1
        unchanged = counts.get(target, 0)
        best = max(best, unchanged + min(numOperations, reachable - unchanged))

    return best

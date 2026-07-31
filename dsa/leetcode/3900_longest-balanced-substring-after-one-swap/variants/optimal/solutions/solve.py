from collections import defaultdict, deque


def solve(s: str) -> int:
    zeros = s.count("0")
    ones = len(s) - zeros
    length_limit = 2 * min(zeros, ones)
    prefix_indices = defaultdict(deque)
    prefix_indices[0].append(0)
    balance = 0
    best = 0
    for right, character in enumerate(s, start=1):
        balance += 1 if character == "1" else -1
        minimum_left = right - length_limit
        for target in (balance - 2, balance, balance + 2):
            candidates = prefix_indices.get(target)
            if not candidates:
                continue
            while candidates and candidates[0] < minimum_left:
                candidates.popleft()
            if candidates:
                best = max(best, right - candidates[0])
        prefix_indices[balance].append(right)
    return best

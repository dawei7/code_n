from heapq import heapreplace, heappush


def solve(technique1: list[int], technique2: list[int], k: int) -> int:
    total = 0
    technique1_count = 0
    smallest_losses: list[int] = []

    for first, second in zip(technique1, technique2):
        if first >= second:
            total += first
            technique1_count += 1
            continue

        total += second
        loss = second - first
        if k == 0:
            continue
        if len(smallest_losses) < k:
            heappush(smallest_losses, -loss)
        elif loss < -smallest_losses[0]:
            heapreplace(smallest_losses, -loss)

    needed = max(0, k - technique1_count)
    if needed:
        losses = sorted(-stored for stored in smallest_losses)
        total -= sum(losses[:needed])
    return total

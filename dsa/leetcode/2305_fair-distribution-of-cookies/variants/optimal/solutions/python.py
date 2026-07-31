from typing import List


def solve(cookies: List[int], k: int) -> int:
    bags = sorted(cookies, reverse=True)
    loads = [0] * k
    best = sum(bags)

    def distribute(index: int, current_max: int) -> None:
        nonlocal best
        if current_max >= best:
            return
        if index == len(bags):
            best = current_max
            return

        seen_loads = set()
        bag = bags[index]
        for child in range(k):
            if loads[child] in seen_loads:
                continue
            seen_loads.add(loads[child])
            loads[child] += bag
            distribute(index + 1, max(current_max, loads[child]))
            loads[child] -= bag

    distribute(0, 0)
    return best

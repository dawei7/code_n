import sys
import heapq
from math import gcd


def digit_sum(x: int) -> int:
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total


def min_reachable_value(n: int, d: int) -> int:
    g = gcd(d, 9)
    rem = n % g
    for value in range(1, 10):
        if value % g == rem:
            return value
    return 9


def solve_case(n: int, d: int):
    target = min_reachable_value(n, d)
    limit = 220
    max_adds = 10000
    dist = {}
    heap = []

    def push(value: int, cost: int):
        if 1 <= value <= limit and cost < dist.get(value, 10**18):
            dist[value] = cost
            heapq.heappush(heap, (cost, value))

    for adds in range(max_adds + 1):
        value = n + adds * d
        if value <= limit:
            push(value, adds)
        push(digit_sum(value), adds + 1)

    while heap:
        cost, value = heapq.heappop(heap)
        if cost != dist[value]:
            continue
        if value == target:
            return target, cost
        push(digit_sum(value), cost + 1)
        for adds in range(1, max_adds + 1):
            y = value + adds * d
            if y <= limit:
                push(y, cost + adds)
            push(digit_sum(y), cost + adds + 1)

    return target, dist[target]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, d = data[idx:idx + 2]
        idx += 2
        best_value, best_ops = solve_case(n, d)
        out.append(f"{best_value} {best_ops}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

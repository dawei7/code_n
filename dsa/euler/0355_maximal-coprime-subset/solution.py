"""Project Euler Problem 355: Maximal Coprime Subset.

Find Co(200000), the maximal possible sum of a set of mutually coprime elements from {1, 2, ..., n}.
"""

import math


def solve(n: int = 200000) -> int:
    """Compute Co(n) via Min-Cost Max-Flow / Maximum Weight Bipartite Matching."""
    # Sieve primes up to n
    is_p = bytearray([1]) * (n + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_p[i]:
            is_p[i * i : n + 1 : i] = bytearray(len(range(i * i, n + 1, i)))

    primes = [p for p in range(2, n + 1) if is_p[p]]

    sqrt_n = math.isqrt(n)
    small_primes = [p for p in primes if p <= sqrt_n]
    large_primes = [p for p in primes if sqrt_n < p <= n // 2]
    fixed_primes = [p for p in primes if p > n // 2]

    # Baseline sum: 1 + fixed primes + large primes + pure powers of small primes
    base_sum = 1 + sum(fixed_primes) + sum(large_primes)
    pure_powers = {}
    for q in small_primes:
        pp = q
        while pp * q <= n:
            pp *= q
        pure_powers[q] = pp
        base_sum += pp

    n_left = len(small_primes)
    n_right = len(large_primes)

    q_to_idx = {q: i for i, q in enumerate(small_primes)}
    p_to_idx = {p: j for j, p in enumerate(large_primes)}

    # Positive gain edges between small primes and large primes
    edges = [[] for _ in range(n_left)]
    for q in small_primes:
        u = q_to_idx[q]
        for p in large_primes:
            v = p_to_idx[p]
            best_gain = 0
            qa = q
            while p * qa <= n:
                gain = p * qa - p - pure_powers[q]
                if gain > best_gain:
                    best_gain = gain
                qa *= q
            if best_gain > 0:
                edges[u].append((v, best_gain))

    # Min-Cost Max-Flow graph construction
    n_nodes = n_left + n_right + 2
    src = n_left + n_right
    sink = src + 1

    head = [-1] * n_nodes
    to = []
    cap = []
    cost = []
    nxt = []

    def add_edge(u_node: int, v_node: int, c: int, w: int) -> None:
        nxt.append(head[u_node])
        head[u_node] = len(to)
        to.append(v_node)
        cap.append(c)
        cost.append(w)

        nxt.append(head[v_node])
        head[v_node] = len(to)
        to.append(u_node)
        cap.append(0)
        cost.append(-w)

    for u in range(n_left):
        add_edge(src, u, 1, 0)
    for v in range(n_right):
        add_edge(n_left + v, sink, 1, 0)
    for u in range(n_left):
        for v, gain in edges[u]:
            add_edge(u, n_left + v, 1, -gain)

    # Successive Shortest Path (SPFA augmenting paths)
    min_cost = 0

    while True:
        dist = [float("inf")] * n_nodes
        parent_edge = [-1] * n_nodes
        in_queue = [False] * n_nodes

        dist[src] = 0
        queue = [src]
        in_queue[src] = True

        idx = 0
        while idx < len(queue):
            u_curr = queue[idx]
            idx += 1
            in_queue[u_curr] = False

            e = head[u_curr]
            while e != -1:
                v_curr = to[e]
                if cap[e] > 0 and dist[u_curr] + cost[e] < dist[v_curr]:
                    dist[v_curr] = dist[u_curr] + cost[e]
                    parent_edge[v_curr] = e
                    if not in_queue[v_curr]:
                        queue.append(v_curr)
                        in_queue[v_curr] = True
                e = nxt[e]

        # Stop when no augmenting path with negative cost (positive gain) exists
        if dist[sink] >= 0:
            break

        min_cost += dist[sink]
        curr = sink
        while curr != src:
            e = parent_edge[curr]
            cap[e] -= 1
            cap[e ^ 1] += 1
            curr = to[e ^ 1]

    return int(base_sum - min_cost)


if __name__ == "__main__":
    print(solve())

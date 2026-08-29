"""Project Euler Problem 838: Not Coprime.

Mathematical reduction:
We seek the smallest integer f(N) = prod_{p in S} p such that for every positive integer
n <= N with n = 3 (mod 10), gcd(f(N), n) > 1.
Equivalently, every such n must have at least one prime factor in S, minimizing
sum_{p in S} ln(p).

1. All primes p <= N ending in 3 have only one prime factor (themselves), so they MUST be in S.
2. Any composite n <= N ending in 3 that is already divisible by a prime ending in 3 is covered.
3. For remaining composite numbers, prime factors can only end in 1, 7, or 9.
   - Any clause of size 1 (e.g. p^3 <= N for p = 7 mod 10) forces p into S (unit propagation).
4. After unit propagation and clause subsumption, all remaining uncovered numbers
   have exactly two prime factors: one ending in 7, and one ending in 9.
5. The problem is thus strictly reduced to Bipartite Minimum Weight Vertex Cover:
   - Left side: primes p = 7 (mod 10) with weight ln(p).
   - Right side: primes q = 9 (mod 10) with weight ln(q).
   - Edges: pairs (p, q) forming an uncovered number n = p * q <= N.
6. By the Max-Flow Min-Cut theorem, the Minimum Weight Vertex Cover is solved exactly
   using Dinic's Maximum Flow algorithm.
"""

from __future__ import annotations

from collections import deque
import math


class Dinic:
    """Dinic's algorithm for computing maximum flow / minimum cut."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.graph: list[list[int]] = [[] for _ in range(n)]
        self.edges: list[list[float]] = []

    def add_edge(self, u: int, v: int, cap: float) -> None:
        self.graph[u].append(len(self.edges))
        self.edges.append([v, cap])
        self.graph[v].append(len(self.edges))
        self.edges.append([u, 0.0])

    def bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for edge_idx in self.graph[u]:
                v = int(self.edges[edge_idx][0])
                cap = self.edges[edge_idx][1]
                if cap > 1e-9 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u: int, t: int, flow: float, ptr: list[int]) -> float:
        if u == t or flow < 1e-9:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            edge_idx = self.graph[u][i]
            v = int(self.edges[edge_idx][0])
            cap = self.edges[edge_idx][1]
            if self.level[v] == self.level[u] + 1 and cap > 1e-9:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 1e-9:
                    self.edges[edge_idx][1] -= pushed
                    self.edges[edge_idx ^ 1][1] += pushed
                    return pushed
        return 0.0

    def max_flow(self, s: int, t: int) -> float:
        flow = 0.0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float("inf"), ptr)
                if pushed < 1e-9:
                    break
                flow += pushed
        return flow


def solve(n: int = 1000000) -> float:
    """Compute the natural logarithm of f(N) rounded to 6 decimal places."""
    # Sieve up to N
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    chosen_primes = {p for p in range(2, n + 1) if is_prime[p] and p % 10 == 3}
    clauses: list[set[int]] = []

    for val in range(3, n + 1, 10):
        temp = val
        factors = []
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                factors.append(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)

        if not any(p in chosen_primes for p in factors):
            clauses.append(set(factors))

    # Unit propagation
    changed = True
    while changed:
        changed = False
        forced = set()
        for c in clauses:
            if len(c) == 1:
                forced.add(next(iter(c)))
        if forced:
            changed = True
            chosen_primes.update(forced)
            clauses = [c for c in clauses if not any(p in forced for p in c)]

    # Subsumption filter
    clauses = sorted(clauses, key=len)
    filtered = []
    for c in clauses:
        if not any(f.issubset(c) for f in filtered):
            filtered.append(c)
    clauses = filtered

    # Bipartite Min-Cut construction
    primes_7 = set()
    primes_9 = set()
    for c in clauses:
        for p in c:
            if p % 10 == 7:
                primes_7.add(p)
            elif p % 10 == 9:
                primes_9.add(p)

    list_7 = sorted(primes_7)
    list_9 = sorted(primes_9)
    idx_7 = {p: i + 1 for i, p in enumerate(list_7)}
    idx_9 = {p: len(list_7) + 1 + i for i, p in enumerate(list_9)}

    num_nodes = len(list_7) + len(list_9) + 2
    s_node = 0
    t_node = num_nodes - 1

    dinic = Dinic(num_nodes)
    for p in list_7:
        dinic.add_edge(s_node, idx_7[p], math.log(p))
    for q in list_9:
        dinic.add_edge(idx_9[q], t_node, math.log(q))
    for c in clauses:
        p, q = sorted(c, key=lambda x: x % 10)
        dinic.add_edge(idx_7[p], idx_9[q], float("inf"))

    flow = dinic.max_flow(s_node, t_node)
    base_log = sum(math.log(p) for p in chosen_primes)

    return round(base_log + flow, 6)


if __name__ == "__main__":
    print(solve())

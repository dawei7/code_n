"""Project Euler Problem 703: Circular Logic II.

Find S(20) mod 1001001011, the number of independent sets in the functional graph
defined by the bit-shift feedback logic f(b1..bn).
"""

from array import array
from collections import deque
from typing import Tuple

_MOD = 1_001_001_011


def _build_successor_and_indegree(n: int) -> Tuple[array, array]:
    total_nodes = 1 << n
    succ = array("I", [0]) * total_nodes
    indeg = array("I", [0]) * total_nodes

    mask = (1 << (n - 1)) - 1
    shift = n - 3

    for s in range(total_nodes):
        t = s >> shift
        newbit = ((t >> 2) & 1) & (((t >> 1) & 1) ^ (t & 1))
        ns = ((s & mask) << 1) | newbit
        succ[s] = ns
        indeg[ns] += 1

    return succ, indeg


def solve(n: int = 20, mod: int = _MOD) -> int:
    """Count independent sets in the functional graph using Kahn topological pruning and cycle DP."""
    total_nodes = 1 << n
    succ, indeg = _build_successor_and_indegree(n)

    acc0 = array("I", [1]) * total_nodes
    acc1 = array("I", [1]) * total_nodes

    in_cycle = bytearray(b"\x01") * total_nodes
    q = deque(i for i in range(total_nodes) if indeg[i] == 0)

    while q:
        u = q.popleft()
        if in_cycle[u] == 0:
            continue
        in_cycle[u] = 0

        p = succ[u]
        dp0 = acc0[u]
        dp1 = acc1[u]

        acc0[p] = (acc0[p] * ((dp0 + dp1) % mod)) % mod
        acc1[p] = (acc1[p] * dp0) % mod

        indeg[p] -= 1
        if indeg[p] == 0:
            q.append(p)

    visited = bytearray(total_nodes)
    ans = 1

    for v in range(total_nodes):
        if in_cycle[v] and not visited[v]:
            cycle = []
            u = v
            while not visited[u]:
                visited[u] = 1
                cycle.append(u)
                u = succ[u]

            k = len(cycle)
            w0 = [int(acc0[x]) % mod for x in cycle]
            w1 = [int(acc1[x]) % mod for x in cycle]

            # Case 1: first node not selected
            prev0, prev1 = w0[0], 0
            for i in range(1, k):
                cur0 = ((prev0 + prev1) % mod) * w0[i] % mod
                cur1 = prev0 * w1[i] % mod
                prev0, prev1 = cur0, cur1
            case1 = (prev0 + prev1) % mod

            # Case 2: first node selected
            prev0, prev1 = 0, w1[0]
            for i in range(1, k):
                cur0 = ((prev0 + prev1) % mod) * w0[i] % mod
                cur1 = prev0 * w1[i] % mod
                prev0, prev1 = cur0, cur1
            case2 = prev0

            ans = (ans * ((case1 + case2) % mod)) % mod

    return ans


if __name__ == "__main__":
    print(solve())

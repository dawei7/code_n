"""Approximation algorithms.

Two classic problems from GFG's approximation-algorithms catalog:

  01 Vertex Cover (2-approx)  - greedy: pick max-degree vertex
    repeatedly; remove it and its neighbours; remaining is a
    vertex cover. The 2-approx result is at most 2x optimal.
  02 Set Cover (greedy)       - repeatedly pick the set
    covering the most uncovered elements; standard log(n)
    approximation.

The graph / universe is small (n <= 8) so brute-force
verification is fast.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === approx_01: Vertex Cover (2-approx) ===

APPROX_01_SOURCE = '''
def solve(n, edges):
    """Return a 2-approximate vertex cover.

    Greedy: while there are uncovered edges, pick a vertex
    of max degree, add it to the cover, and remove it and all
    its incident edges. The resulting cover is at most 2x
    the optimal.
    """
    if n == 0:
        return set()
    # Adjacency list.
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    cover = set()
    edges_left = set()
    for u, v in edges:
        edges_left.add((min(u, v), max(u, v)))
    while edges_left:
        # Pick the vertex with the most incident edges remaining.
        degrees = [0] * n
        for u, v in edges_left:
            degrees[u] += 1
            degrees[v] += 1
        v = max(range(n), key=lambda i: degrees[i])
        if degrees[v] == 0:
            break
        cover.add(v)
        # Remove all edges incident to v.
        edges_to_remove = [e for e in edges_left if v in e]
        for e in edges_to_remove:
            edges_left.discard(e)
    return sorted(cover)
'''


def _setup_vertex_cover(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = set()
    # Tree edges to ensure connectivity.
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.add((min(u, i), max(u, i)))
    # Extra edges.
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    challenge._n = n_nodes
    return {"n": n_nodes, "edges": sorted(edges)}


def _verify_vertex_cover(challenge, result):
    if not isinstance(result, list):
        return False
    cover = set(result)
    # The cover must touch every edge.
    for u, v in challenge._edges if hasattr(challenge, "_edges") else []:
        if u not in cover and v not in cover:
            return False
    # Brute force: find the minimum cover.
    n = challenge._n
    edges = challenge._edges
    if not edges:
        return True
    best = n
    for mask in range(1 << n):
        cov = {i for i in range(n) if mask & (1 << i)}
        if all(u in cov or v in cov for u, v in edges):
            size = len(cov)
            if size < best:
                best = size
    return len(cover) <= 2 * best


# Need to stash the edges on the challenge for the verify.
def _setup_vertex_cover_patched(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 6))
    edges = set()
    for i in range(1, n_nodes):
        u = rng.randint(0, i - 1)
        edges.add((min(u, i), max(u, i)))
    for _ in range(n_nodes):
        u = rng.randint(0, n_nodes - 1)
        v = rng.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    challenge._n = n_nodes
    challenge._edges = sorted(edges)
    return {"n": n_nodes, "edges": sorted(edges)}


# === approx_02: Set Cover (greedy) ===

APPROX_02_SOURCE = '''
def solve(universe, sets, m, k):
    """Greedy set cover: each step picks the set covering the
    most uncovered elements. O(m * k) per step.

    universe is a list of unique elements; sets[i] is a list
    of elements in set i. m = |sets|, k = |universe|.
    Return a sorted list of chosen set indices.
    """
    uncovered = set(universe)
    chosen = []
    while uncovered:
        # Pick the set covering the most uncovered elements.
        best_idx = -1
        best_count = 0
        for i, s in enumerate(sets):
            count = sum(1 for x in s if x in uncovered)
            if count > best_count:
                best_count = count
                best_idx = i
        if best_idx == -1 or best_count == 0:
            break
        chosen.append(best_idx)
        for x in sets[best_idx]:
            uncovered.discard(x)
    return sorted(chosen)
'''


def _setup_set_cover(challenge, n, seed):
    rng = random.Random(seed)
    universe_size = max(2, min(n, 6))
    universe = list(range(universe_size))
    n_sets = max(1, min(n, 4))
    sets = []
    for _ in range(n_sets):
        s = set()
        for u in universe:
            if rng.random() < 0.5:
                s.add(u)
        sets.append(sorted(s))
    challenge._universe = list(universe)
    challenge._sets = [list(s) for s in sets]
    return {"universe": list(universe), "sets": [list(s) for s in sets], "m": len(sets), "k": len(universe)}


def _verify_set_cover(challenge, result):
    if not isinstance(result, list):
        return False
    chosen = set(result)
    universe = set(challenge._universe)
    covered = set()
    for i in chosen:
        if 0 <= i < len(challenge._sets):
            covered.update(challenge._sets[i])
    return covered == universe


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="approx_01",
        name="Vertex Cover (2-Approx)",
        category="approximation",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find a 2-approximate vertex cover. Greedy: while\n"
            "edges remain, pick the vertex with the highest degree,\n"
            "add it to the cover, remove all incident edges. The\n"
            "result is at most 2x the optimal vertex cover. The\n"
            "verify accepts any 2-approx (i.e., len(cover) <= 2 * OPT).\n"
            "Source: https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/vertex-cover-problem-approximate-algorithm/",
        params=["n", "edges"],
        inputs={
            "n": "number of nodes.",
            "edges": "list of (u, v) tuples (undirected).",
        },
        returns="a sorted list of node indices covering every edge (and 2-approx).",
        source=APPROX_01_SOURCE,
        setup_fn=_setup_vertex_cover_patched,
        verify_fn=_verify_vertex_cover,
        samples=[
            Sample("n = 5, edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]", "[0, 2] (or other 2-approx)"),
        ],
        hint="Pick the max-degree vertex, add to cover, drop its edges. Repeat.",
        parents=["graph_12"],
        children=["approx_02"],
    ),
    AlgorithmSpec(
        id="approx_02",
        name="Set Cover (Greedy)",
        category="approximation",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find a set of indices that cover every element of\n"
            "``universe``. Greedy: each step picks the set covering\n"
            "the most uncovered elements. Standard O(log n) approx\n"
            "ratio for the classical Set Cover problem.\n"
            "Source: https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/",
        params=["universe", "sets", "m", "k"],
        inputs={
            "universe": "list of k unique element IDs (0..k-1).",
            "sets": "list of m sets, each a list of element IDs.",
            "m": "number of sets.",
            "k": "size of universe.",
        },
        returns="a sorted list of chosen set indices covering universe.",
        source=APPROX_02_SOURCE,
        setup_fn=_setup_set_cover,
        verify_fn=_verify_set_cover,
        samples=[
            Sample("universe = [0, 1, 2, 3, 4], sets = [[0, 1], [1, 2, 3], [2, 3, 4], [0, 4]], m = 4, k = 5", "[0, 1, 2] (or 1 + 2)"),
        ],
        hint="Each step: pick the set with the most uncovered elements. Repeat.",
        parents=["approx_01"],
        children=[],
    ),
]

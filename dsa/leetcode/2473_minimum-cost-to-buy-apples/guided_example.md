# Guided Example: Minimum Cost to Buy Apples

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "roads": [[1, 2, 5], [2, 3, 1], [3, 1, 2]], "appleCost": [2, 3, 1], "k": 3}`
- **Required output:** `[2, 3, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads`, where $\text{roads}[i] = [a_{i}, b_{i}, \text{cost}_{i}]$ indicates that there is a **bidirectional **road between cities $a_{i}$ and $b_{i}$ with a cost of traveling equal to $\text{cost}_{i}$.

The objective is to compute `[2, 3, 1]` from `{"n": 3, "roads": [[1, 2, 5], [2, 3, 1], [3, 1, 2]], "appleCost": [2, 3, 1], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Reduce a round trip to one weighted shortest distance

Suppose a traveler starts at city `i`, buys at city `u`, and the shortest distance between them is $d(i,u)$. Roads are bidirectional, so the cheapest outbound trip costs $d(i,u)$. On return, every road cost is multiplied by `k`, so following a shortest route back costs $k\cdot d(i,u)$.

The total for buying at `u` is therefore

$$
\texttt{appleCost}[u]+(k+1)d(i,u).
$$

For each starting city, the exact source runs Dijkstra to compute distances and minimizes this expression over reached cities.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "roads": [[1, 2, 5], [2, 3, 1], [3, 1, 2]], "appleCost": [2, 3, 1], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a zero-based undirected graph

Road city labels are one-based. The code subtracts one from both endpoints and stores `(neighbor,cost)` in both adjacency directions. Positive road costs satisfy Dijkstra's non-negative-edge requirement.

Buying in the starting city is always possible with distance zero, so an answer exists even if the road graph is disconnected. Only cities in the same connected component need be reached.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Road city labels are one-based.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One Dijkstra run for one start

`dijkstra(i)` initializes `dist[i]=0` and pushes `(0,i)`. Every heap pop gives a distance label `d` and city `u`.

The line

`ans = min(ans, appleCost[u] + d*(k+1))`

considers buying at that city with the popped route length.

For every road `u-v` of cost `w`, the relaxation compares `dist[v]` with `dist[u]+w`. If smaller, it updates and pushes the new pair.

Notice that relaxation uses current best `dist[u]` rather than popped `d`. This matters for stale heap entries.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "roads": [[1, 2, 5], [2, 3, 1], [3, 1, 2]], "appleCost": [2, 3, 1], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Multi-source Dijkstra:** Initialize each city :** - **Multi-source Dijkstra:** Initialize each city with its apple price and use edge weight multiplied by `k+1`. One reversed search yields all starts and matches the manifest.
- **Add a stale-entry guard:** Skip when popped distance differs from `dist[u]` to prevent redundant edge scans in the repeated-search implementation.
- **Floyd–Warshall:** All-pairs distances make each apple choice easy but cost $O(N^3)$ time.
- **Buy locally:** Distance zero guarantees answer is never more than local apple cost.
- **Disconnected graph:** A start can only buy in its component, but local purchase guarantees feasibility.
- **Return multiplier:** Outbound plus return is `1+k` times the same undirected shortest distance, not merely `k`.
- **Equal-cost routes:** Dijkstra needs only one shortest distance value; route identity is irrelevant.
- **Large totals:** Road paths and scaling require 64-bit arithmetic outside Python.
- **Input labels:** Subtracting one aligns one-based cities with zero-based arrays.
- **Metadata mismatch:** The exact source runs Dijkstra from every city instead of one multi-source search.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n + m) log n)$. Let $N$ be cities, $M$ roads, and $\Delta$ maximum degree. With a stale-entry guard, one run is $O((N+M)\log N)$ and all runs are $O(N(N+M)\log N)$.
- **Auxiliary Space Complexity:** $O(N+M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

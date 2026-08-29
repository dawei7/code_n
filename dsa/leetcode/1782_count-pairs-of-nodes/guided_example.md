# Guided Example: Count Pairs Of Nodes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], "queries": [2, 3]}`
- **Required output:** `[6, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an undirected graph defined by an integer `n`, the number of nodes, and a 2D integer array `edges`, the edges in the graph, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates that there is an **undirected** edge between $u_{i}$ and $v_{i}$. You are also given an integer array `queries`.

The objective is to compute `[6, 5]` from `{"n": 4, "edges": [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], "queries": [2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from node degrees, then correct shared edges

For nodes `a` and `b`, adding their degrees counts every edge incident to either node. However, an edge directly connecting `a` and `b` appears once in each degree, while `incident(a,b)` should count that edge only once.

If `shared(a,b)` is the number of parallel edges between the pair, then:

$$
\operatorname{incident}(a,b)
=
\deg(a)+\deg(b)-\operatorname{shared}(a,b).
$$

The exact solution first counts pairs using the easier raw degree sum, then subtracts pairs that were false positives because of shared-edge double counting.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], "queries": [2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build degrees and edge multiplicities

`cnt` stores each node's degree. Every input edge increments both endpoint degrees, including parallel edges.

Endpoints are converted to zero-based indices and normalized with smaller endpoint first. `g[(a,b)]` then records how many parallel edges connect that unordered pair.

Normalization ensures edges `(u,v)` and `(v,u)` would use the same key. Only connected pairs appear in `g`; unconnected pairs have shared multiplicity zero and never need correction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort degrees for query counting

`s = sorted(cnt)` loses node identity but preserves the multiset of degrees. For the initial raw condition, only the two degree values matter.

For query threshold `t` and a degree `x = s[j]`, the solution needs later indices whose degree is strictly greater than `t - x`.

`bisect_right(s, t - x, lo=j + 1)` returns the first later index `k` with value greater than `t - x`. All indices from `k` through `n - 1` form raw sums greater than `t`, so `n - k` is added.

Starting at `j + 1` enforces two distinct sorted positions and counts each unordered node pair exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], "queries": [2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers per query:** Count raw degree pairs in $O(n)$ after sorting, achieving the manifest's tighter query bound.
- **Check every node pair:** It costs $O(Qn^2)$ and is too slow.
- **Ignore shared edges:** It overcounts connected pairs because their mutual edges appear in both degrees.
- **Single edge between pair:** Subtract one from raw degree sum for true incident count.
- **Multiple parallel edges:** Subtract the full multiplicity, but adjust the answer count by one pair.
- **Unconnected pair:** Multiplicity is zero, so no correction entry is needed.
- **Strict threshold:** Sum equal to the query does not count; `bisect_right` handles this.
- **Normalized endpoints:** Smaller-first keys combine all parallel edges consistently.
- **Equal degree nodes:** Sorted positions remain distinct and are counted once through `j + 1`.
- **Several identical queries:** The exact source recomputes each independently.
- **Node identities after sorting:** They are unnecessary for raw count but retained in `cnt` for shared-edge corrections.
- **One false positive:** Each dictionary pair can cause at most one subtraction per query.
- **Zero threshold:** Every pair with at least one incident edge may qualify according to the same formula.
- **Input preservation:** Endpoints are normalized in local variables; `edges` is not changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E+n\log n+Q(n\log n+P)$. Let $E$ be the number of edges, $P$ the number of distinct connected node pairs, $Q$ the number of queries, and $n$ the node count.
- **Auxiliary Space Complexity:** $O(n+P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Detonate the Maximum Bombs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bombs": [[2, 1, 3], [6, 1, 4]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a list of bombs. The **range** of a bomb is defined as the area where its effect can be felt. This area is in the shape of a **circle** with the center as the location of the bomb.

The objective is to compute `2` from `{"bombs": [[2, 1, 3], [6, 1, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model detonation as directed reachability

Bomb `i` directly detonates bomb `j` when the center of `j` lies inside or on `i`'s circular range. This relationship is directional: a large-radius bomb may reach a small-radius bomb even when the reverse is false.

The source builds a directed graph `g`. An edge `i -> j` means detonating `i` directly triggers `j`.

For each unordered pair of bomb indices, it computes the center distance with `hypot(x1 - x2, y1 - y2)`. It then performs two independent radius tests:

- if `dist <= r1`, add edge `i -> j`;
- if `dist <= r2`, add edge `j -> i`.

Both may succeed, one may succeed, or neither may succeed. Using separate conditions rather than `else` preserves all four possibilities.

The inclusive `<=` is important because a bomb exactly on the circle boundary is within range.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bombs": [[2, 1, 3], [6, 1, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why graph paths represent chain reactions

If graph edge `i -> j` exists, detonating `i` triggers `j`. Once `j` detonates, every outgoing edge from `j` becomes active, and so on.

Thus every bomb reachable from a chosen start through a directed path will eventually detonate. Conversely, a bomb can detonate only through such a sequence of direct range relationships, so directed reachability exactly matches the chain reaction.

The task therefore becomes: compute the reachable-set size from every possible starting vertex and take the maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Traverse from each possible initial bomb

For start `k`, `vis = {k}` counts the manually detonated bomb itself, and `q = [k]` begins the traversal.

The source uses a Python list as a growing queue:

`for i in q`

iterates over existing entries and also reaches entries appended later. Whenever an unvisited neighbor `j` is found, it is added to `vis` and appended to `q`. This behaves like breadth-first traversal without an explicit deque index.

The visited set prevents cycles from adding a bomb repeatedly or causing an infinite traversal.

After traversal, `len(vis)` is the exact number detonated from `k`. If it equals `n`, no larger answer is possible, so the method returns `n` immediately. Otherwise it updates the best value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bombs": [[2, 1, 3], [6, 1, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Undirected connectivity:** Incorrect because one bomb's radius may reach another without reciprocal reach.
- **Floyd-Warshall transitive closure:** It also costs $O(n^3)$ time and $O(n^2)$ space, but repeated graph traversal is simpler.
- **Run DFS instead of the growing list:** DFS and BFS produce the same reachable set; traversal order does not affect the count.
- **Squared integer distance:** Avoids `hypot` and floating-point boundary comparisons while retaining $O(1)$ work per pair.
- **One bomb:** Its visited set contains itself, so the answer is one.
- **Bomb on the boundary:** `dist <= radius` includes it.
- **Same centers:** Positive radii make both bombs directly reach one another.
- **Cycles:** `vis` prevents repeated processing while still counting every bomb once.
- **Disconnected groups:** Each start reaches only its directed component; trying all starts finds the best group.
- **Early full reachability:** Returning `n` is safe because no answer can exceed the number of bombs.
- **Queue-list behavior:** Python's list iterator observes appended elements, which is why `for i in q` completes the traversal.
- **Input preservation:** The graph is separate; bomb coordinates and radii are not changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. Let $n$ be the number of bombs and $E$ the number of directed reachability edges.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Find the Number of Distinct Colors Among the Balls

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"limit": 4, "queries": [[1, 4], [2, 5], [1, 3], [3, 4]]}`
- **Required output:** `[1, 2, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `limit` and a 2D array `queries` of size `n x 2`.

The objective is to compute `[1, 2, 2, 3]` from `{"limit": 4, "queries": [[1, 4], [2, 5], [1, 3], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both directions of the assignment

After each query, we need the number of colors currently used by at least one ball. Recomputing all colored balls each time would be too slow.

The exact solution maintains:

- `g[x]`: the current color assigned to ball `x`;
- `cnt[y]`: the number of balls currently assigned color `y`.

The number of distinct active colors is exactly `len(cnt)`, provided zero-count entries are removed.

Only balls that have appeared in a query need entries in `g`. The parameter `limit` can be as large as $10^9$, so allocating an array for all labels would be wasteful. The dictionary makes storage depend on the number of queries instead.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"limit": 4, "queries": [[1, 4], [2, 5], [1, 3], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process one recoloring

For query `[x, y]`, the code first increments `cnt[y]` because ball `x` will have new color `y`.

If `x` already exists in `g`, the ball previously contributed one owner to old color `g[x]`. That old count is decremented. If it becomes zero, the key is popped so it no longer contributes to `len(cnt)`.

Then `g[x] = y` records the new assignment, and `len(cnt)` is appended to the answer.

Incrementing the new color before decrementing the old one is safe even when the colors are identical. Suppose ball `x` is recolored from $y$ to $y$. The count temporarily rises by one and then falls by one, returning to its original positive value. It is not mistakenly removed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For query `[x, y]`, the code first increments `cnt[y]` becau... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Invariant

After each completed query:

- `g` contains exactly one current color for every ball colored so far;
- for every key $c$ in `cnt`, `cnt[c]` equals the number of `g` values equal to $c$;
- `cnt` contains no zero-count key.

The invariant holds initially for two empty structures.

For an uncolored ball, incrementing the new count and adding `g[x]` introduces exactly one new assignment. For an already colored ball, decrementing the old count removes its former contribution, incrementing the new count adds its current contribution, and popping zero removes precisely a color with no owners. Thus the invariant is preserved.

Because the keys of `cnt` are exactly colors with at least one owner, `len(cnt)` is the requested distinct-color count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"limit": 4, "queries": [[1, 4], [2, 5], [1, 3], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recount colors after every query:** Scanning a:** - **Recount colors after every query:** Scanning all colored balls per query can take $O(q^2)$ time.
- **Color set only:** A set cannot tell whether removing one ball's old color should remove the color entirely when other balls still use it.
- **Array indexed by ball label:** It requires $O(limit)$ memory, impossible when `limit` is $10^9$.
- **Coordinate compression:** It can replace the ball dictionary after reading all queries, but adds preprocessing without improving asymptotic bounds.
- **First assignment to a ball:** There is no old count to decrement.
- **Recolor to the same color:** Increment-then-decrement leaves counts and the distinct answer unchanged.
- **Old color shared by others:** Its count stays positive and the key remains active.
- **Old color loses its last ball:** The zero count is popped, reducing `len(cnt)`.
- **New color already active:** Its owner count increases but distinct-color count does not.
- **New color unseen:** A new counter key raises the distinct count by one.
- **Uncolored balls:** They have no `g` entry and never contribute a color.
- **Unused limit:** It only validates legal labels; sparse dictionaries intentionally make it unnecessary to the computation.
- **One answer per query:** The append occurs after both the old-color removal and new assignment are complete, so the returned list has exactly one fully updated distinct-color count for every query.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let $q$ be the number of queries.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

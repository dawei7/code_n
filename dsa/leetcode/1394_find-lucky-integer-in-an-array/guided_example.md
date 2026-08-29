# Guided Example: Find Lucky Integer in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 2, 3, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, a **lucky integer** is an integer that has a frequency in the array equal to its value.

The objective is to compute `2` from `{"arr": [2, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count first, then test the definition

A value $x$ is lucky when it occurs exactly $x$ times. The array's order is irrelevant; only the frequency of each distinct value matters.

`Counter(arr)` builds a mapping `cnt` from each distinct array value to its occurrence count. For `[1,2,2,3,3,3]`, the mapping is equivalent to `{1: 1, 2: 2, 3: 3}`. Each key equals its mapped count, so all three values are lucky.

Counting in one pass avoids repeatedly scanning the whole array for every candidate. Each occurrence performs one expected constant-time hash-table update.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter exactly the lucky entries

`cnt.items()` produces pairs `(x, v)`, where `x` is the array value and `v` is its frequency. The generator expression

`(x for x, v in cnt.items() if x == v)`

yields a value only when it equals its count. It does not yield the count separately because the two numbers are identical for a lucky entry.

This distinction is important. A value 2 appearing three times has pair `(2,3)` and is rejected, even though both numbers are positive and small. A value 3 appearing twice is also rejected. Equality, not a greater-than or at-least relationship, defines luckiness.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select the largest and handle no candidate

There may be several lucky integers, so `max(...)` selects the largest yielded value. Dictionary iteration order is irrelevant because `max` examines all candidates.

If the generator yields nothing, ordinary `max` would raise an exception. Passing `default=-1` makes it return the required sentinel instead. Because valid array values are at least one, $-1$ cannot be confused with a real lucky integer.

For `[2,2,3,4]`, pairs include `(2,2)`, `(3,1)`, and `(4,1)`. Only 2 is yielded and returned. For `[2,2,2,3,3]`, the pairs are `(2,3)` and `(3,2)`; neither passes, so the default produces $-1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed frequency array:** Values lie between one and 500, so an array of 501 counts gives $O(n+500)$ time and constant domain-bounded space.
- **Sort and scan runs:** Sorting groups equal values, then run lengths can be compared with values. It costs $O(n\log n)$ time and may mutate the input.
- **Repeated `arr.count`:** Count every candidate by rescanning the array. It is simple but can cost $O(n^2)$.
- **Scan possible values downward:** With a frequency array, check 500 down to one and return the first equality. This makes largest selection explicit.
- **Several lucky integers:** `max` returns the largest, not the first counter entry.
- **No lucky integer:** `default=-1` avoids an exception and returns the required sentinel.
- **Value one:** It is lucky exactly when it occurs once.
- **Value larger than array length:** It cannot be lucky and is rejected automatically.
- **Duplicate occurrences:** They are summarized into one counter entry and do not cause duplicate candidates.
- **Positive-value constraint:** It ensures $-1$ is an unambiguous failure value and zero need not be considered.
- **Input order:** It has no effect on frequencies or the maximum.
- **Input mutation:** `Counter` only reads `arr`.
- **Required import:** `Counter` must be available, normally from `collections`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length and $u$ the number of distinct values. Building `Counter` takes expected $O(n)$ time. Scanning its $u$ entries takes $O(u)$, and $u\le n$, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

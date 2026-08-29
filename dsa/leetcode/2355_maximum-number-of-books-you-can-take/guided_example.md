# Guided Example: Maximum Number of Books You Can Take

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"books": [8, 5, 2, 7, 9]}`
- **Required output:** `19`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `books` of length `n` where $\text{books}[i]$ denotes the number of books on the $i^{\text{th}}$ shelf of a bookshelf.

The objective is to compute `19` from `{"books": [8, 5, 2, 7, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix the rightmost shelf and maximize everything to its left

Suppose a chosen section ends at shelf `i` and takes all `books[i] = v` books there. Moving one shelf left, strict increase permits at most `v - 1` books; another step left permits at most `v - 2`, and so on.

Within a suffix not limited by shelf capacities, the optimal taken amounts form a descending-by-one arithmetic progression when viewed right to left.

The dynamic state `dp[i]` is the maximum total for a valid contiguous section ending at `i` while taking exactly `books[i]` from that final shelf.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"books": [8, 5, 2, 7, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Transform capacity constraints with books[i] minus i

Extending the progression from `i` back to earlier index `j` would demand

`books[i] - (i-j)`

books at `j`. Shelf `j` can support this exactly when

`books[j] >= books[i] - (i-j)`,

equivalently

`books[j] - j >= books[i] - i`.

The list `nums[i] = books[i] - i` makes this comparison constant and exposes a previous-smaller-element problem.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the nearest boundary with a monotonic stack

`left[i]` is the nearest previous index `j` satisfying

`nums[j] < nums[i]`.

The stack keeps indices with strictly increasing `nums` values. Before pushing current `i`, it pops while the top value is greater than or equal to current. The remaining top, if any, is the nearest strictly smaller boundary.

Every index is pushed once and popped at most once, so all boundaries are found in linear time.

At this boundary, shelf `j` cannot simply continue the arithmetic ramp controlled by shelf `i`; it is better represented by its already optimized `dp[j]`. Shelves `j+1` through `i` form the new progression segment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `19` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"books": [8, 5, 2, 7, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `19` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Walk left from every endpoint:** Directly constructing the best progression costs `O(n^2)` in decreasing-capacity patterns.
- **Use only a greedy global segment:** Local capacity boundaries create restart points, so dynamic programming is needed to combine earlier optimal segments.
- **Previous smaller on raw books:** The relevant comparison is `books[i]-i`, which incorporates the one-per-position slope.
- **Pop only strictly greater stack values:** Equal transformed values must also pop because the boundary requires strictly smaller.
- **One shelf:** Its `dp` equals its available books and is the answer.
- **Zero-book shelf:** A segment taking positive amounts cannot pass through it; the formulas produce a zero-length contribution when it is the endpoint.
- **Increasing capacities:** Long sections may use most or all shelves.
- **Very small right endpoint value:** `cnt <= v` prevents zero or negative terms.
- **No previous boundary:** The progression begins at the later of index zero and the point where its leftmost term is one.
- **Boundary exists:** `dp[j]` joins a progression over `j+1..i` with strict inequality at the join.
- **Equal transformed values:** The earlier index is popped so it cannot be used as a strictly smaller boundary.
- **Maximum over endpoints:** The best section need not end at the last shelf.
- **Input preservation:** All transformed and DP state is separate from `books`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of shelves. Building transformed values is `O(n)`. Each index enters and leaves the monotonic stack at most once, and the DP loop is linear, so total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

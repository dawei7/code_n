# Guided Example: Find Maximal Uncovered Ranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10, "ranges": [[3, 5], [7, 8]]}`
- **Required output:** `[[0, 2], [6, 6], [9, 9]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` which is the length of a **0-indexed** array `nums`, and a **0-indexed** 2D-array `ranges`, which is a list of sub-ranges of `nums` (sub-ranges may **overlap**).

The objective is to compute `[[0, 2], [6, 6], [9, 9]]` from `{"n": 10, "ranges": [[3, 5], [7, 8]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Work with intervals rather than an array of size $n$

$n$ can be as large as $10^9$, so marking each covered index in a Boolean array is impossible.

Only the covered interval endpoints matter. By sorting covered ranges and sweeping their union, the solution identifies gaps without touching individual cells.

Variable `last` represents the greatest array index known to be covered by the union of all ranges processed so far.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10, "ranges": [[3, 5], [7, 8]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort by starting point

`ranges.sort()` orders pairs lexicographically:

- increasing left endpoint;
- increasing right endpoint when starts tie.

After sorting, when processing interval $[l,r]$, no future interval begins before $l$. Therefore, any gap between the previous covered union and $l$ is final and can be emitted immediately.

The sort mutates the input interval list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ranges.sort()` orders pairs lexicographically:

- increasin... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use `last = -1` as a virtual boundary

The real array begins at index zero. Initializing:

`last = -1`

pretends that coverage before the first interval ends immediately before the array.

Then the first possible uncovered index is always `last + 1`:

- initially zero;
- later, one position after the merged covered prefix.

This removes the need for a separate “gap before the first interval” branch.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 2], [6, 6], [9, 9]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10, "ranges": [[3, 5], [7, 8]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 2], [6, 6], [9, 9]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean coverage array:** Requires $O(n)$ time:** - **Boolean coverage array:** Requires $O(n)$ time and space and is impossible for $n$ up to $10^9$.
- **Explicitly merge ranges first:** Correct but unnecessary; the gap sweep merges coverage implicitly.
- **Difference map of endpoints:** Can avoid cell storage but still needs sorted events and more bookkeeping.
- **No covered ranges:** Return the single full interval `[0,n-1]`.
- **Whole array covered:** No leading, internal, or trailing gap is emitted.
- **Overlapping intervals:** `max(last,r)` merges them.
- **Nested interval:** It must not move `last` backward.
- **Adjacent covered intervals:** They leave no uncovered integer between them.
- **Single-cell gap:** Strict condition detects and emits equal endpoints.
- **Input mutation:** `ranges.sort()` changes the caller-visible order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m\log m)$. Let $m=\texttt{len(ranges)}$. Sorting costs $O(m\log m)$. The sweep visits every range once in $O(m)$ time, so total time is $O(m\log m)$.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Longest Arithmetic Sequence After Changing At Most One Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [9, 7, 5, 10, 1]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `5` from `{"nums": [9, 7, 5, 10, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent arithmetic structure through adjacent differences

A contiguous sequence is arithmetic when every adjacent difference is equal. The source builds

`d[i] = nums[i] - nums[i - 1]`

for `i\ge1`. Entry `d[0]` is unused and remains zero.

Changing one element can affect only the two adjacent differences touching that index. Every other difference stays fixed. This locality suggests precomputing unchanged arithmetic runs on both sides of every possible replacement position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [9, 7, 5, 10, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Longest unchanged run ending at each index

`f[i]` is the length, in elements, of the longest unchanged arithmetic subarray ending at index `i`.

The base values are `f[0]=1` and `f[i]=2` for `i\ge1`, because any two-element subarray is arithmetic: it has only one adjacent difference.

For `i\ge2`, if

`d[i] == d[i - 1]`,

then the difference from `i-1` to `i` continues the same arithmetic run ending at `i-1`. The source sets

`f[i] = f[i - 1] + 1`.

If the differences differ, the longest run ending at `i` resets to the final two elements, so the initialized value two remains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `f[i]` is the length, in elements, of the longest unchanged ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Longest unchanged run starting at each index

Symmetrically, `g[i]` is the longest unchanged arithmetic subarray starting at `i`. The last position has length one, and other positions begin at length two.

Scanning right to left, if `d[i+1] == d[i+2]`, the edge from `i` to `i+1` continues the run starting at `i+1`, so

`g[i] = g[i + 1] + 1`.

These arrays allow the main loop to know in constant time how far a fixed common difference already extends on either side.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [9, 7, 5, 10, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate replacement values:** The allowed re:** - **Enumerate replacement values:** The allowed replacement is any integer, an infinite set. Structural equations determine the only useful endpoint continuation or interior midpoint instead.
- **Check every subarray:** Testing arithmetic structure and one possible defect over `O(N^2)` intervals is too slow for `N=10^5`.
- **Change one adjacent difference independently:** Replacing an interior element changes two differences together; they cannot be optimized separately. The midpoint equation couples them.
- **No replacement:** Already arithmetic runs must remain candidates because the operation is “at most” one, not exactly one.
- **Change at a selected endpoint:** Only one neighboring difference must match, so an arbitrary integer extension is always possible.
- **Interior odd neighbor difference:** No integer can be exactly halfway between the fixed neighbors, so a two-sided bridge is impossible. One-sided candidates may still work.
- **Negative difference:** Arithmetic sequences may decrease. Equality tests and evenness work identically for negative values.
- **Zero difference:** Constant runs are arithmetic, and an interior replacement can bridge equal neighbors with the same value.
- **Array already arithmetic:** An unchanged run reaches length `N`, and no candidate can exceed it.
- **Minimum allowed length:** With `N=4`, initialization to three is valid and all boundary checks avoid out-of-range access.
- **Difference-array indexing:** `d[i]` describes the edge from `i-1` to `i`. Left extension compares `d[i-1]`; right extension compares `d[i+2]`.
- **Avoid double-counting neighbors:** The central bridge starts with three elements, so extensions add run length minus one on each side.
- **Space reduction:** One could precompute only one directional array and maintain the other direction with a more involved scan, but the three linear arrays keep the exact logic clear and meet the required bounds.
- **Import dependency:** The annotation uses `List`, which must be available in environments that evaluate annotations.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Constructing `d`, `f`, and `g` requires three linear passes. The final loop performs constant work per index. Total time is `O(N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

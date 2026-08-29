# Guided Example: Mark Elements on Array by Performing Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 1, 2, 3, 1], "queries": [[1, 2], [3, 3], [4, 2]]}`
- **Required output:** `[8, 3, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of size `n` consisting of positive integers.

The objective is to compute `[8, 3, 0]` from `{"nums": [1, 2, 2, 1, 2, 3, 1], "queries": [[1, 2], [3, 3], [4, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Maintain the sum rather than recomputing it.** `s = sum(nums)` begins as the sum of all unmarked elements. Whenever an element is marked for the first time, subtract its value. Then `s` is always the answer after the current query.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 1, 2, 3, 1], "queries": [[1, 2], [3, 3], [4, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Boolean list `mark` records whether each index has already been removed from that sum, preventing double subtraction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Pre-sort the global marking priority.** `arr` contains pairs `(value,index)` sorted by Python tuple order. Values come first, and equal values are ordered by smaller index. This exactly matches the rule for choosing smallest unmarked elements with index tie-breaking.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[8, 3, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 1, 2, 3, 1], "queries": [[1, 2], [3, 3], [4, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[8, 3, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Min-heap:** Store all value-index pairs and pop until finding unmarked entries. It also works in $O((N+M)\log N)$ but pays logarithmic cost per automatic marking.
- **Re-sort remaining elements per query:** It can become quadratic or worse and repeats a fixed global ordering.
- **Recompute unmarked sum:** Scanning `nums` after every query costs $O(MN)$.
- **Explicit index already marked:** It is skipped without subtracting twice.
- **Explicit index is next smallest:** Marking it first makes the cursor skip it, so $k$ additional elements are still chosen.
- **Equal values:** Tuple sorting chooses smaller original index.
- **$k=0$:** Only the explicit index action occurs.
- **Too few unmarked elements:** All remaining ones are marked and the sum becomes zero.
- **All elements marked early:** Later queries append zero with no further cursor work.
- **Persistent cursor:** Its monotonicity is the key to the linear post-sort processing bound.
- **Why explicit marking does not move `j` immediately:** That index may lie later in sorted order. Leaving the cursor unchanged is safe because its mark flag will cause a skip when reached.
- **Sum invariant starts correctly:** Before any marks, every index is unmarked, so `sum(nums)` exactly matches the invariant's definition.
- **Query order matters:** Mark flags persist across queries, and answers are appended after each query. Reordering queries could change which elements remain for later automatic choices.
- **Local `k` mutation:** Unpacking each query creates a new integer reference. Decrementing it does not alter the nested list in `queries`.
- **Positive values:** Subtracting newly marked values makes `s` monotonically nonincreasing and never negative under correct one-time marking.
- **Output size:** One sum is appended per query, so `len(ans)==len(queries)` even after all elements are marked.
- **Why cursor order remains valid after explicit marks:** Removing arbitrary elements from a fixed total order leaves the relative priority of every surviving element unchanged.
- **Index tie-break is encoded once:** Sorting tuples eliminates the need to compare indices inside every query loop.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N+M)$. Sorting $N$ pairs costs $O(N\log N)$. Initial sum and pair construction cost $O(N)$. Query headers cost $O(M)$, while all cursor-loop iterations together cost $O(N)$. Total time is $O(N\log N+M)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

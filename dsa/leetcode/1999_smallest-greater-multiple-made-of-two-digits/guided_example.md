# Guided Example: Smallest Greater Multiple Made of Two Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"k": 2, "digit1": 0, "digit2": 2}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given three integers, `k`, `digit1`, and `digit2`, you want to find the **smallest** integer that is:

The objective is to compute `20` from `{"k": 2, "digit1": 0, "digit2": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate allowed numbers as a digit tree

Starting from zero, appending digit `d` creates `x * 10 + d`. The source performs breadth-first search over this construction tree, using a deque initialized with zero.

Each popped number is tested before its children are appended. A qualifying value must be strictly greater than `k`, divisible by `k`, and within the signed 32-bit limit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"k": 2, "digit1": 0, "digit2": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Put the smaller digit branch first

If `digit1 > digit2`, the method recursively calls itself with the digits swapped. After that normalization, children are enqueued in ascending digit order.

Breadth-first traversal processes shorter digit sequences before longer ones, and ascending child order gives lexicographic order within a fixed length. For canonical positive decimal strings, shorter length means smaller value and lexicographic order matches numeric order. Therefore the first qualifying canonical value is the smallest.

If the digits are equal, only one child is enqueued, avoiding two identical branches.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How a zero digit affects the queue

The search begins at numeric zero so it can build every allowed digit sequence uniformly. If the smaller digit is zero, appending it to zero produces zero again. More generally, leading-zero sequences generate duplicate numeric values.

These duplicates delay the search but do not invalidate the first-answer guarantee. The first canonical representation of every positive number appears at its natural length in ordinary breadth-first and lexicographic order. A later leading-zero representation only repeats a value whose canonical representation was already processed; it cannot introduce a new smaller answer after a larger canonical answer.

A visited set or special handling of leading zero could eliminate duplication, but the exact source uses neither.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"k": 2, "digit1": 0, "digit2": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS over remainders modulo `k`:** Tracks at most $k$ states and can reconstruct the smallest digit string, avoiding duplicate full-number generation; the strict-greater and 32-bit conditions need careful handling.
- **Enumerate multiples of `k`:** Test $2k,3k,\ldots$ until the limit, which can require roughly $2^{31}/k$ checks.
- **Depth-first generation:** Does not naturally visit values in numeric order and may find a larger answer first.
- **Both digits zero:** Immediate -1 because only zero can be formed.
- **Equal nonzero digits:** Only one branch is needed at each depth.
- **One digit zero:** Leading-zero paths create duplicates but not new numerical values.
- **Digits supplied in reverse order:** The recursive swap normalizes their generation order.
- **Candidate equals `k`:** Rejected by the strict `x > k` test.
- **No in-range solution:** The first unseen canonical value beyond the limit proves -1.
- **Boundary value $2^{31}-1$:** Allowed because rejection uses strictly greater than the limit.
- **Duplicate queue values:** They affect efficiency, not correctness.
- **Imported deque:** The exact source assumes `deque` is available in the execution environment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^D)$. Let $D$ be the number of digit positions explored before a solution or the 32-bit cutoff. With two distinct digits, the source can generate $O(2^D)$ queue nodes and takes $O(2^D)$ time and space. With identical digits, branching drops to one per level.
- **Auxiliary Space Complexity:** $O(2^D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

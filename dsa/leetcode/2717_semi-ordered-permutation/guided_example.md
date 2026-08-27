# Guided Example: Semi-Ordered Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 4, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** permutation of `n` integers `nums`.

The objective is to compute `2` from `{"nums": [2, 1, 4, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the locations of 1 and n matter

A semi-ordered permutation imposes exactly two requirements: value `1` must occupy index zero, and value `n` must occupy index $n-1$. Every other value may appear in any order. Therefore an optimal solution should not spend effort arranging the middle values; they merely move aside as `1` and `n` pass them through adjacent swaps.

Let `i = nums.index(1)` and `j = nums.index(n)`. Because `nums` is a permutation, both values occur exactly once, so these positions are unambiguous.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 4, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cost of moving 1 to the front

Value `1` starts at index `i`. One adjacent swap with the element immediately to its left decreases its index by one. No adjacent swap can decrease its index by more than one. Reaching index zero therefore requires at least `i` swaps, and swapping `1` left exactly `i` times achieves that cost.

Thus `i` is both a lower bound and the exact isolated cost for the first requirement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Value `1` starts at index `i`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cost of moving n to the back

Value `n` starts at index `j`. It is $n-1-j$ positions away from the last index. Moving it right across each intervening element takes exactly one adjacent swap, so its isolated cost is:

$$
n-1-j.
$$

Again, this is unavoidable because a swap moves `n` at most one position right, and it is attainable by repeatedly swapping it with its right neighbor.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 4, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate adjacent swaps:** Produces the final :** - **Simulate adjacent swaps:** Produces the final permutation but does unnecessary mutations when only the minimum count is requested.
- **One combined scan:** The positions of `1` and `n` can be recorded in one traversal; it keeps the same $O(n)$ time and $O(1)$ space.
- **Breadth-first search over permutations:** Finds a shortest sequence for tiny $n$ but has factorial state growth and ignores the endpoint structure.
- **Already semi-ordered:** When `i=0` and `j=n-1`, the formula returns zero.
- **Reversed special values:** When `n` precedes `1`, subtract exactly one because their crossing swap advances both.
- **Length two:** The only permutations are already ordered with cost zero or reversed with cost one; the formula handles both.
- **Adjacent 1 and n in correct order:** They do not cross, so no discount applies.
- **Adjacent n and 1 in reversed order:** Their one mutual swap is the shared operation counted by the subtraction.
- **Distinctness guarantee:** The permutation property ensures `index` finds one unique position for each special value.
- **Unrestricted middle:** No sorting of values `2` through `n-1` is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the permutation length. Python's `nums.index(1)` scans until it finds `1`, and `nums.index(n)` independently scans until it finds `n`. Each scan is $O(n)$ in the worst case, so total time is $O(n)$; two linear scans remain linear.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Next Greater Element I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}`
- **Required output:** `[-1, 3, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

The objective is to compute `[-1, 3, -1]` from `{"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

For each queried value, the answer is not merely any larger value to its right. It must be the first larger value encountered when moving rightward through `nums2`. Searching separately for every value in `nums1` repeats the same suffix scans. The solution preprocesses all useful answers in one right-to-left pass with a monotonic stack, then answers each query by dictionary lookup.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Scanning from right to left has a natural advantage: when processing value `x`, every possible answer to its right has already been seen. The stack keeps only right-side values that are still capable of being the next greater element for some value farther left.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Scanning from right to left has a natural advantage: when pr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**What the stack represents.** From bottom to top, `stk` is strictly decreasing under the distinct-value constraint. Equivalently, values become larger as one moves from the top downward. The top is the nearest surviving candidate in the compressed suffix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, 3, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, 3, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan rightward for every query:** Locate each :** - **Scan rightward for every query:** Locate each `nums1` value and search its suffix. This can cost $O(mn)$ time.
- **Left-to-right monotonic stack:** Keep unresolved values; when a larger value arrives, pop them and map each popped value to the current one. It has the same $O(n+m)$ bounds and is the editorial's common direction.
- **Precompute indices only:** A value-to-index map avoids locating queries but still leaves a linear suffix scan per query, so worst-case time remains quadratic.
- **No greater element:** The reverse scan stores no mapping, and `get(x, -1)` supplies the required sentinel.
- **Strictly increasing `nums2`:** Every value except the last maps to its immediate right neighbor.
- **Strictly decreasing `nums2`:** Every reverse-processed value pops the smaller suffix candidates, and no queried value has a greater element to its right.
- **Distinctness:** Dictionary keys are values because each value occurs once. Duplicate arrays would require index-aware handling.
- **Strict comparison:** Equal values would not qualify as greater. The source's `<` pop is sufficient because equality is impossible here.
- **Query order:** Preprocessing order does not affect output order; the final comprehension follows `nums1` exactly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $n$ be `len(nums2)` and $m$ be `len(nums1)`. Every value of `nums2` is pushed once and can be popped at most once. Although one loop iteration may pop many values, the total number of pops across the entire scan is at most $n$. Preprocessing is therefore $O(n)$, and the $m$ expected constant-time dictionary lookups add $O(m)$, for $O(n+m)$ total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

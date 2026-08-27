# Guided Example: Neither Minimum nor Maximum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 1, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` containing **distinct** **positive** integers, find and return **any** number from the array that is neither the **minimum** nor the **maximum** value in the array, or **`-1`** if there is no such number.

The objective is to compute `2` from `{"nums": [3, 2, 1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify the two forbidden values

The answer may be any array value except the global minimum and global maximum. Because all values are distinct, there is exactly one occurrence of each forbidden extreme.

The exact implementation first computes:

`mi, mx = min(nums), max(nums)`.

Once those two values are known, every other element automatically satisfies the requirement. There is no need to determine which interior element is second-smallest, a median, or in any particular rank.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan until the first allowed value

The generator expression:

`(x for x in nums if x != mi and x != mx)`

visits values in original array order and yields only values different from both extremes. `next(..., -1)` returns the first yielded value. If the generator is exhausted without yielding, `next` returns its default `-1`.

The contract accepts any valid interior value, so stopping at the first one is optimal. The solution does not sort or modify `nums`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The generator expression:

`(x for x in nums if x != mi and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a different value from both extremes is sufficient

Every element of a finite set lies between its minimum and maximum. With distinct values, an element that equals neither extreme must satisfy:

$$
\texttt{mi}<x<\texttt{mx}.
$$

It is therefore neither the minimum nor maximum. Conversely, any valid requested value must be unequal to both `mi` and `mx`, so the filter captures exactly the allowed elements.

Positivity is not needed for this reasoning, but it makes `-1` a safe failure sentinel because `-1` cannot be a legal array value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Median of the first three distinct values:** T:** - **Median of the first three distinct values:** The median of any three distinct array values cannot be a global minimum or maximum, giving an $O(1)$ solution when $n\ge3$.
- **Sort the array:** Any interior sorted element works, but sorting costs $O(n\log n)$ and may mutate the input.
- **Track min, max, and candidate in one pass:** Can reduce the number of traversals while preserving $O(n)$ time.
- **Length one:** Its sole value is both extremes, so return `-1`.
- **Length two:** The two distinct values are exactly the minimum and maximum, so return `-1`.
- **Length at least three:** Distinctness guarantees at least one interior value.
- **First element valid:** The generator stops immediately after the two extreme scans.
- **Example permits several answers:** Returning three instead of the sample's two is still correct.
- **Positive values:** Ensure the failure sentinel `-1` cannot collide with a valid returned number.
- **Input preservation:** Neither `min`, `max`, nor the generator changes `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `nums.length`. The `min` scan takes $O(n)$ time, the `max` scan takes $O(n)$ time, and the generator takes up to $O(n)$ time. The total is $O(n)$, not $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

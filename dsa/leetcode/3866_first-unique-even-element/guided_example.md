# Guided Example: First Unique Even Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 2, 5, 4, 6]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [3, 4, 2, 5, 4, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two different kinds of information are required

The answer combines a global condition and an ordering condition:

- a value is eligible only if its total frequency in the entire array is exactly one; and
- among eligible even values, the one with the earliest original index wins.

The first condition cannot generally be decided when a value is first encountered. An even number seen near the beginning may occur again near the end and lose uniqueness. The source therefore uses two passes: count all values first, then scan the original order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 2, 5, 4, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build complete frequencies

`cnt = Counter(nums)` creates a mapping from each distinct array value `x` to its total number of occurrences. After this statement,

$$
\texttt{cnt}[x]
=\left|\{i:\texttt{nums}[i]=x\}\right|.
$$

Because the counter is built from the full array before any candidate is selected, `cnt[x] == 1` exactly captures global uniqueness. It does not merely mean “not seen before.”

For the first example `[3,4,2,5,4,6]`, the counter records frequency two for value four and frequency one for two and six. Value four is even but ineligible; two and six are both eligible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan in original order for the priority rule

The second loop reads `nums` from left to right. For each value `x`, it checks

`x % 2 == 0`

and

`cnt[x] == 1`.

The remainder condition is the exact divisibility-by-two definition of evenness. Both conditions must hold.

As soon as they do, the method returns `x`. Since every earlier array position has already been examined and rejected, this occurrence has the smallest index among all globally unique even values. No later value can have higher priority.

If the loop ends, every element failed parity, uniqueness, or both. The method returns minus one, the required no-answer sentinel.

Notice that the function returns the even value, not its index. The scan order is used only to choose which value to return.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 2, 5, 4, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed array of 101 counts:** Count by value directly, then perform the same original-order scan. This gives deterministic `O(N+100)` time and explicit `O(1)` bounded-domain space.
- **One pass with first positions and counts:** Record each value's count and earliest index, then scan the at-most-100 value domain for the eligible even value with minimum first index. This is correct but stores more state than the simple second pass.
- **Return the first even value immediately:** Incorrect because a later duplicate may make it non-unique.
- **Use a set of seen values only:** A set distinguishes seen from unseen but not frequency one from frequency two or more. Exact counts are necessary.
- **Sort unique even candidates by value:** The priority is array index, not numerical value. Sorting values can choose the wrong answer.
- **Return an index:** The contract asks for the element value. The scan order determines priority, but the returned object is `x`.
- **First element later duplicated:** Its counter value exceeds one, so it is skipped even though it is the earliest even occurrence.
- **Multiple unique evens:** The left-to-right early return selects the earliest index, not the smallest even number.
- **Repeated even values:** Every occurrence is rejected because its full frequency is greater than one.
- **Unique odd value:** It remains in the counter but fails the parity condition.
- **No valid value:** Minus one is safe as a sentinel because all input values are positive.
- **Value zero:** It is excluded by the stated range, though it is mathematically even and the source would treat it as such if supplied.
- **Generalized value domain:** Without the one-to-one-hundred bound, describe counter memory as `O(U)` rather than constant.
- **Hash-table qualification:** Counter operations are expected constant time. A fixed array removes hashing if worst-case deterministic behavior matters under this bounded domain.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the array length and `U` its number of distinct values. Building the counter takes expected `O(N)` time. The selection pass visits at most `N` elements, with expected constant-time hash lookup per element. Total expected time is `O(N)`, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

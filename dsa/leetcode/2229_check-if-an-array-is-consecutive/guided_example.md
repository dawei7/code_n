# Guided Example: Check if an Array Is Consecutive

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 4, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return `true` *if *`nums`* is **consecutive**, otherwise return *`false`*.*

The objective is to compute `true` from `{"nums": [1, 3, 4, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A consecutive array must satisfy two independent facts

Let `n = len(nums)`, `mi = min(nums)`, and `mx = max(nums)`. If the array contains every integer from `mi` through `mi + n - 1` exactly once, then:

- it has `n` distinct values; and
- its numeric span contains exactly `n` integers, so `mx - mi + 1 = n`.

Both facts matter. A correct span without distinctness can hide a missing number behind a duplicate. Distinctness without the correct span can leave a gap between values.

The exact solution obtains the bounds with

`mi, mx = min(nums), max(nums)`

and checks both requirements in one chained comparison:

`len(set(nums)) == mx - mi + 1 == len(nums)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 4, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand Python's chained equality

Python interprets `a == b == c` as “`a == b` and `b == c`,” not as comparing a Boolean result with `c`. Here the three quantities are:

- the number of distinct values;
- the number of integer positions in the inclusive minimum-to-maximum interval;
- the number of array entries.

Returning true means all three are equal.

Since a set removes duplicates, `len(set(nums)) == len(nums)` proves every input element is unique. The equality `mx - mi + 1 == len(nums)` proves that the inclusive span has exactly as many integer positions as the array has elements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Python interprets `a == b == c` as “`a == b` and `b == c`,” ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why these conditions are sufficient

Every array value lies between `mi` and `mx` by definition. The interval contains exactly `n` possible integers when `mx - mi + 1 = n`. The array also supplies exactly `n` distinct values.

It is impossible to choose `n` distinct integers from an `n`-integer interval while omitting one of the interval's values: omitting one would leave only `n - 1` possible selected values. Therefore, the set of array values must be the entire interval `[mi, mx]`, which equals `[mi, mi + n - 1]`. The array is consecutive.

Order is irrelevant. The definition says the array contains the range; it does not require the elements to appear in increasing order. The set and extrema deliberately ignore arrangement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 4, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort and compare neighbors:** Sort the values :** - **Sort and compare neighbors:** Sort the values and require each next value to equal the previous plus one. This is correct but costs `O(n \log n)` time and may mutate the input unless a copy is made.
- **Boolean presence array:** The bounded value range permits marking seen values by index. It can run in linear time but allocates according to the value universe rather than the actual input size.
- **Check only `mx - mi + 1 == n`:** Duplicates can replace missing interior values while preserving the span, so distinctness is essential.
- **Check only set size `n`:** Unique values can still contain gaps and have a span wider than `n`.
- **One element:** It is consecutive by definition, and all three compared quantities equal one.
- **Unsorted consecutive values:** Ordering does not matter; set membership and extrema still recognize the complete range.
- **Duplicate at an endpoint:** The set count falls below list length and the method returns false.
- **Missing interior value:** Either a duplicate reduces distinctness or another value widens the span; the chained test catches both.
- **Zero as the minimum:** No offset or special handling is required.
- **Large gaps:** They increase `mx - mi + 1` beyond `n` and fail immediately in the final Boolean expression.
- **Input preservation:** Unlike in-place sorting, this method leaves `nums` unchanged.
- **Chained-comparison semantics:** Rewriting it in a language without Python-style chaining requires two explicit conjunctions; evaluating equality left to right as ordinary binary operations could be wrong.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(nums)`. `min(nums)` and `max(nums)` each scan the array in `O(n)` time. Constructing `set(nums)` performs `n` expected constant-time hash insertions, also `O(n)` expected time. Sequential linear passes remain `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Partition Array Into Three Parts With Equal Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, return `true` if we can partition the array into three **non-empty** parts with equal sums.

The objective is to compute `true` from `{"arr": [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Derive the only possible part sum

If three parts have equal sum `s`, the complete array sum must be `3s`. Therefore, the total must be divisible by three, and the target for every part is forced.

The line

`s, mod = divmod(sum(arr), 3)`

computes both quotient and remainder. If `mod` is nonzero, no integer target sum can satisfy the requirement, so the method returns false immediately.

Python's `divmod` also works for negative totals. When the total is exactly divisible by three, the remainder is zero and `s` is the exact signed target.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Greedily cut whenever the running segment reaches the target

Variable `t` is the sum of elements since the most recent greedy cut. For each value:

`t += x`.

Whenever `t == s`, the algorithm has found one nonempty consecutive segment of target sum. It increments `cnt` and resets `t = 0` so the next element begins a new candidate segment.

Resetting is essential. Without it, later comparisons would use a prefix sum from the start of the whole array rather than the sum of the current part.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Variable `t` is the sum of elements since the most recent gr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why each counted segment is nonempty

The target check happens only after one array element has been added. After a cut, `t` is reset, but `cnt` cannot increase again until a later loop iteration consumes at least one new element.

This remains true when `s = 0` and the next element is zero. A one-element zero part is nonempty and valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix-sum boundary search:** Find one prefix :** - **Prefix-sum boundary search:** Find one prefix equal to `s` and a later prefix equal to `2s` while leaving an element for the suffix. It is also linear but needs careful boundary handling when `s = 0`.
- **Store all prefix sums:** It can search possible cuts but uses `O(N)` space unnecessarily.
- **Try every pair of cuts:** Direct enumeration costs `O(N^2)` or worse.
- **Total not divisible by three:** Impossible immediately, regardless of element arrangement.
- **Target zero:** At least three nonempty zero-sum greedy segments are required; repeated zero values are handled naturally.
- **Negative values:** The method does not assume running sums are monotone.
- **More than three target hits:** Still valid; use the first two cuts and the complete remaining suffix.
- **Exactly three elements:** Each element must equal the forced target, which the scan recognizes.
- **Nonempty requirement:** Counting a segment only after consuming an element and demanding a third hit ensures the suffix after the second cut is nonempty.
- **Input preservation:** The array is read twice but never modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

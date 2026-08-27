# Guided Example: Largest Number After Digit Swaps by Parity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 1234}`
- **Required output:** `3412`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `num`. You may swap any two digits of `num` that have the same **parity** (i.e. both odd digits or both even digits).

The objective is to compute `3412` from `{"num": 1234}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parity fixes which digits may occupy each position

An odd digit may swap only with another odd digit, and an even digit only with another even digit. Therefore, a position that originally contains an odd digit can ultimately contain any of the number's odd digits, but never an even digit. The same holds for even positions of the parity pattern.

Because arbitrary pairs of equal-parity digits may be swapped any number of times, every permutation within the odd group and every permutation within the even group is reachable. The task is to assign those digits to their allowed positions to make the decimal number largest.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 1234}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maximize from the most significant position

Two positive integers with the same number of digits are compared at their first differing digit. The larger digit at the earliest position always wins, regardless of later digits.

Thus, at each original position, the optimal choice is the largest unused digit having the required parity. Choosing a smaller available digit there cannot be compensated by placing a larger same-parity digit later. Swapping those two assignments would increase the earlier digit and produce a larger number.

Applying this argument from left to right proves the greedy placement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Two positive integers with the same number of digits are com... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count available digits instead of sorting

The solution converts `num` to its decimal digits:

`nums = [int(c) for c in str(num)]`.

`Counter(nums)` stores how many copies of each digit remain. Since digits belong to the fixed range zero through nine, counts are a compact alternative to sorting separate odd and even lists.

The array `idx = [8, 9]` stores the current largest candidate for each parity. Index zero begins at largest even digit eight; index one begins at largest odd digit nine.

For an original digit `x`, `x & 1` is zero when `x` is even and one when it is odd. The solution uses that parity as an index into `idx`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3412` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 1234}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3412` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort odd and even lists descending:** Then con:** - **Sort odd and even lists descending:** Then consume the next digit from the appropriate list at each position. This is simpler conceptually but costs `O(d \log d)` sorting time; with at most ten digits the practical difference is tiny.
- **Try all same-parity swaps:** Exploring reachable permutations is factorial in the number of digits and repeats equivalent arrangements when digits duplicate.
- **Globally sort every digit:** This may place an odd digit into an originally even position or vice versa, violating the swap invariant.
- **One digit:** Its parity pool contains only itself, so the number is unchanged.
- **All digits one parity:** The method arranges all digits in descending order because every position draws from the same pool.
- **Already maximal arrangement:** Each position receives the same value and the result is unchanged.
- **Repeated digits:** `Counter` preserves multiplicity, and each placement decrements exactly one copy.
- **Zeros:** Zero participates in the even pool and is used only after larger remaining evens.
- **First digit parity:** The parity pattern of positions is fixed by the original digits; only values within each parity group move.
- **Duplicate maximum digit:** The pointer remains at that value until its count reaches zero.
- **Pointer exhaustion:** It cannot fall below zero or one while a position of that parity remains, because the remaining counts and remaining parity positions are equal.
- **Input preservation:** `num` is immutable; the method builds a new numeric result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `d` be the number of decimal digits. Converting to digits, building the counter, and constructing the answer each take `O(d)` time. The parity pointers descend across only five possible digits per parity in total, so all while-loop decrements together are `O(1)` for decimal digits.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

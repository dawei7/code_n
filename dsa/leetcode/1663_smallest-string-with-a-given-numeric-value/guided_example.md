# Guided Example: Smallest String With A Given Numeric Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "k": 27}`
- **Required output:** `"aay"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **numeric value** of a **lowercase character** is defined as its position `(1-indexed)` in the alphabet, so the numeric value of `a` is `1`, the numeric value of `b` is `2`, the numeric value of `c` is `3`, and so on.

The objective is to compute `"aay"` from `{"n": 3, "k": 27}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from the cheapest possible length-`n` string

Every position must contain a lowercase letter, and the smallest letter `a` has numeric value one. Therefore any valid string of length `n` spends at least `n` total value. The source begins with exactly that baseline:

`ans = ['a'] * n`.

At this point, the string has numeric value `n`. The variable `d = k - n` is the additional value that still must be distributed. The constraints `n <= k <= 26n` guarantee

$$
0 \le d \le 25n.
$$

Each position currently holds `a` and can be increased by at most `25` before reaching `z`. Thus there is always exactly enough total capacity to place the remaining `d`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "k": 27}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why extra value belongs as far right as possible

Lexicographic order is determined by the first position at which two strings differ. Keeping an earlier character smaller is more important than making any later character smaller. Therefore the additional numeric value should be pushed toward the right end, allowing the longest possible prefix to remain `a`.

Suppose a candidate has some extra value at an earlier position while a later position is not yet `z`. Moving one unit of value from the earlier character to that later character keeps the total numeric value unchanged. At the first affected position, the new string has a smaller character, so it is lexicographically smaller. Repeating this exchange shows that in an optimal string, later positions must be filled to `z` before an earlier position receives extra value.

This yields a simple shape: zero or more leading `a` characters, possibly one partially increased character, and then zero or more trailing `z` characters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Fill complete `z` characters from the end

`i` starts at `n - 1`, the last index. While `d > 25`, more extra value remains than one position can hold. The method sets `ans[i] = 'z'`, which adds exactly `25` beyond that position’s baseline `a`. It subtracts `25` from `d` and moves `i` one step left.

The loop condition is strictly greater than `25`, not greater than or equal to it. Once `d` is at most `25`, the current one position can absorb all remaining value. Stopping there leaves every earlier position untouched at `a`, which is lexicographically best.

At the maximum input `k = 26n`, the initial extra value is `25n`. The loop fills the last `n - 1` positions with `z`, leaving `d = 25` and `i = 0`. The final step turns the first position into `z` as well. Thus the index never needs to move below zero for a valid input.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aay"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "k": 27}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aay"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy construction from the left:** At each position, choose the smallest character that leaves at most `26` value for every remaining position and at least one for each. This is also $O(n)$ and correct, but its feasibility formula is slightly less intuitive than filling extra value from the right.
- **Fill all `a` characters and scan every position backward:** Add `min(d, 25)` at each index until `d` becomes zero. This is nearly identical; the exact source accelerates full increments with a loop and performs one residual assignment afterward.
- **Enumerate strings or use dynamic programming:** Both are unnecessary because lexicographic order and uniform per-position bounds give a direct greedy exchange argument. Enumeration is exponential.
- **Minimum value `k == n`:** Then `d == 0`, the loop is skipped, the last `a` remains unchanged, and the answer is all `a` characters.
- **Maximum value `k == 26n`:** Every position becomes `z`, including the first position in the residual step.
- **Residual exactly `25`:** The strict loop condition stops and the final assignment turns the current position into `z`. This avoids an extra iteration but produces the same correct suffix.
- **Residual zero after baseline:** `chr(ord('a') + 0)` safely writes `a` again.
- **Single-character string:** `d` is between zero and `25`, so the loop never moves left and the final assignment directly selects the letter of value `k`.
- **Large `n`:** Work and storage grow linearly up to the $10^5$ constraint; there is no recursion-depth or combinatorial issue.
- **Why not fill from the left:** Spending extra value early makes the first differing character larger even when later positions still have capacity, so it cannot produce the lexicographically smallest result.
- **Input feasibility:** The bounds on `k` are necessary. Below `n` no length-`n` lowercase string has small enough value, and above `26n` the positions lack sufficient capacity; the source relies on the guarantee rather than checking these cases.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Allocating `ans` with `n` copies of `'a'` takes $O(n)$ time. The loop moves `i` left at most `n - 1` times, and the residual assignment is constant time. Joining the `n` characters into the return string takes another $O(n)$ time. Total running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

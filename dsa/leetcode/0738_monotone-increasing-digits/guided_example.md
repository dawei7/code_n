# Guided Example: Monotone Increasing Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1234}`
- **Required output:** `1234`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer has **monotone increasing digits** if and only if each pair of adjacent digits `x` and `y` satisfy $x \le y$.

The objective is to compute `1234` from `{"n": 1234}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep the number unchanged if its digits already qualify

Digits are monotone increasing when every adjacent pair satisfies left digit less than or equal to right digit. The exact solution converts `n` to a mutable list of digit characters and scans from left to right while this condition holds.

The index `i` begins at one. After the first loop, either:

- `i == len(s)`, meaning no descent exists and `n` itself is the largest valid number no greater than `n`.
- `s[i - 1] > s[i]`, meaning `i` is the first position where monotonicity fails.

If the number already qualifies, the method performs no edits and returns it after joining the digits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1234}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first descent forces a decrease somewhere to its left

At a descent such as the `3, 2` boundary in `332`, leaving the prefix unchanged cannot produce a monotone number no greater than the input. Raising the later digit enough to reach 3 would make the candidate larger than `n` at the first differing position.

Therefore some digit at or before the left side of the descent must be decreased. To maximize the result, the solution starts by decreasing the digit immediately before the descent by exactly one.

After lowering that digit, every later position should eventually be made as large as possible, namely nine, because the prefix has already made the candidate strictly smaller than `n`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a decrement may propagate left

Lowering `s[i - 1]` can create a new descent with its own left neighbor. In `332`, lowering the second 3 to 2 gives the prefix `32`, which is still decreasing. The first 3 must also be lowered.

The loop

`while i and s[i - 1] > s[i]`

decrements `s[i - 1]` and moves `i` one position left. It repeats until the digit before the changed boundary is no greater than the digit after it, or until it has moved past the leading position.

Every decremented digit was at least one: it was strictly greater than a decimal digit to its right. Subtracting one therefore never creates a negative digit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1234` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1234}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1234` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every smaller number:** Decrement `n` until finding a monotone candidate. This can inspect an enormous number of integers and is far slower than repairing digits directly.
- **Construct the answer with digit dynamic programming:** A tight-prefix DP can maximize a monotone sequence under the upper bound. It is general but significantly more complex for a property solved by one greedy repair.
- **Decrement only the first offending digit once:** This fails when the decrement creates a new descent to its left, as in `332`. The repair must propagate.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let `d` be the number of decimal digits. The first scan advances at most `d` positions. The repair loop moves only left, at most `d` positions, and the suffix-fill loop moves only right across at most `d` positions.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

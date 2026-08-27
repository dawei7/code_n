# Guided Example: 24 Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cards": [4, 1, 8, 7]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `cards` of length `4`. You have four cards, each containing a number in the range `[1, 9]`. You should arrange the numbers on these cards in a mathematical expression using the operators `['+', '-', '*', '/']` and the parentheses `'('` and `')'` to get the value 24.

The objective is to compute `true` from `{"cards": [4, 1, 8, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce two current values into one

Any legal expression using binary operators can be evaluated by repeatedly choosing two available subexpression values, combining them with one operator, and replacing them with the result.

Starting with four card values:

- the first operation leaves three values;
- the second leaves two;
- the third leaves one.

The recursive search enumerates every such reduction order and operation choice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cards": [4, 1, 8, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recursive state

`dfs(nums)` receives the current multiset of floating-point values produced by card values or earlier subexpressions.

When only one value remains, no more binary operation can be applied. The branch succeeds when:

`abs(nums[0] - 24) < 1e-6`.

The tolerance is necessary because real division can produce repeating binary floating-point approximations. A mathematically exact result such as 24 may be represented as `23.999999999...`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dfs(nums)` receives the current multiset of floating-point ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose two distinct current entries

The nested loops select ordered indices `i` and `j` with `i != j`.

`nxt` contains every current number except those two. Each list position represents a distinct available card or derived subexpression, so equal numeric values at different positions can still be selected separately.

The selected pair is combined, and its result is appended to `nxt` for the recursive call.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cards": [4, 1, 8, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Exact rational arithmetic:** Use fractions rep:** - **Exact rational arithmetic:** Use fractions represented by numerator and denominator. This avoids floating-point tolerance and division-rounding concerns, at the cost of larger integer arithmetic.
- **- **Subset dynamic programming:** For every subset:** - **Subset dynamic programming:** For every subset of cards, store every reachable value by splitting the subset into two parts. It systematically removes duplicate recomputation but is more machinery for four cards.
- **- **Enumerate permutations, operators, and parenth:** - **Enumerate permutations, operators, and parenthesis shapes:** This is finite and workable for four cards but easier to omit a shape or mishandle noncommutative operations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The contract fixes the input at exactly four cards. Therefore, the recursion tree has a fixed finite maximum size, independent of any growing input parameter. Under the problem's formal constraints, time and auxiliary space are both `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

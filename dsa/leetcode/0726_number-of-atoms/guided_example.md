# Guided Example: Number of Atoms

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"formula": "H2O"}`
- **Required output:** `"H2O"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `formula` representing a chemical formula, return *the count of each atom*.

The objective is to compute `"H2O"` from `{"formula": "H2O"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why scanning from right to left simplifies multipliers

In a chemical formula, a number appears after the thing it multiplies. It may be the count of one atom, as in `H2`, or the multiplier for a parenthesized group, as in `(OH)2`. A right-to-left scan encounters that number before it encounters the atom or closing parenthesis to which the number belongs.

The exact solution uses this direction so a parsed number can be held in one variable, `pending`, and applied to the next meaningful token on its left. If no written number exists, the implicit multiplier is one.

Nested groups add another requirement: an atom must receive the product of every enclosing group multiplier. The stack `multipliers` stores cumulative products. It begins with `[1]`, representing no enclosing multiplication.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"formula": "H2O"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse a multi-digit number in reverse

When the current character is a digit, the scanner consumes the entire consecutive digit run from right to left. Because the least significant digit is encountered first, it builds the value using `place`:

- Start with `factor = 0` and `place = 1`.
- Add `digit * place`.
- Multiply `place` by ten before reading the next digit to the left.

For the text `123`, the scan sees `3`, then `2`, then `1` and accumulates `3 + 20 + 100 = 123`. It stores that result in `pending` and uses `continue` because the index already points to the character immediately before the number.

Under a valid formula, this pending number belongs either to the atom immediately on its left or to a group whose closing parenthesis is immediately on its left.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Entering a group while scanning backward

When the scanner encounters `)`, it is moving backward into the parenthesized group. Every atom encountered until the matching `(` must be multiplied by the number that followed this closing parenthesis.

The solution appends

`multipliers[-1] * pending`

to the stack. This is a cumulative multiplier: it combines the new group’s factor with all outer groups already active. `pending` is then reset to one.

For example, while scanning `(ON(SO3)2)2` backward, the outer `)2` makes the current cumulative multiplier two. Reaching the inner `)2` pushes four, so atoms inside that nested group receive both factors.

When the scan later reaches `(`, it has moved out of the current group. Popping the stack restores the cumulative multiplier of the surrounding context.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"H2O"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"formula": "H2O"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"H2O"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive descent from left to right:** Parse one group into a local count map, recursively parse nested groups, and multiply a completed child map after its closing parenthesis. This closely follows the grammar but uses recursion depth `O(d)` and merges maps.
- **Stack of count maps:** Push an empty map at `(`, then pop, multiply, and merge at `)`. It is iterative and intuitive, but multiple maps may store repeated atom names. The exact reverse scan keeps one global count map and a multiplier stack.
- **Regular-expression tokenization:** A regex can extract atoms, numbers, and parentheses before a reverse pass. It shortens token recognition but introduces a separate token collection and makes the grammar less explicit.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + A \log A)$. Let `n` be the formula length, `A` the number of distinct atom names, and `d` the maximum nesting depth.
- **Auxiliary Space Complexity:** $O(A + d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

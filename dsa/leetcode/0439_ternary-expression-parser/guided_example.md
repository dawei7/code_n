# Guided Example: Ternary Expression Parser

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "T?2:3"}`
- **Required output:** `"2"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `expression` representing arbitrarily nested ternary expressions, evaluate the expression, and return *the result of it*.

The objective is to compute `"2"` from `{"expression": "T?2:3"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Right associativity suggests scanning from right to left

An expression `condition ? trueValue : falseValue` cannot be resolved until both branch expressions have been resolved. Nested ternaries associate from right to left, so scanning the input backward encounters branch results before the condition that selects between them.

The solution uses `expression[::-1]` to traverse characters in reverse and a stack `stk` to store already resolved operands/subexpressions. Colons carry no information once scan direction and stack positions are understood, so they are skipped.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "T?2:3"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ordinary value characters become stack operands

Digits, `T`, and `F` may all be terminal results. When `cond` is false, any character other than `':'` or `'?'` is appended to the stack.

Scanning `T?2:3` backward, the algorithm first pushes `3`, then pushes `2`. The false branch was encountered first, and the true branch is now on top of it. This ordering is exactly what reduction needs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A question mark announces a pending reduction

When the reverse scan reaches `'?'`, both branch expressions to its right have already been reduced to stack values. The code sets `cond = true` rather than reducing immediately because the condition character lies one position farther left and has not yet been processed.

The next non-separator character is guaranteed by valid syntax to be the condition `T` or `F`. Because `cond` is true, it is interpreted as an operator condition rather than pushed as an ordinary terminal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"2"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "T?2:3"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"2"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Forward recursive descent:** Parse one condition and recursively parse its true/false expressions while tracking matching separators. It can be linear with a shared index but may use $O(n)$ recursion depth.
- **Repeatedly replace the rightmost atomic expression:** Easy to visualize, but immutable string rebuilding can make it $O(n^2)$.
- **Build an explicit expression tree:** Correct but allocates nodes unnecessary when only the final selected terminal is required.
- **Constant-space focused scan:** Follow only the selected branch from left to right while counting nested `?`/`:` pairs to skip an unselected branch. It can achieve $O(n)$ time and $O(1)$ extra space but is more subtle.
- **Ignore right associativity:** Evaluating leftmost ternaries first changes expressions such as `F?1:T?4:5` and is incorrect.
- **Condition `T`:** Preserve the stack's top true result and discard the false result below it.
- **Condition `F`:** Discard the top true result, naturally exposing the false result.
- **Boolean terminal result:** A `T` or `F` not acting as the character before a pending `?` is pushed like a digit.
- **Colons:** They are skipped because branch ordering is already encoded by reverse traversal and the stack.
- **Valid-expression guarantee:** It ensures no stack underflow, unmatched delimiter, or unfinished `cond` state must be handled.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the expression length. The reversed slice `expression[::-1]` takes $O(n)$ time and allocates an $O(n)$ string. The loop processes each character once, and every stack item is pushed/popped a constant number of times, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

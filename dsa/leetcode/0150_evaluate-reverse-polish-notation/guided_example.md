# Guided Example: Evaluate Reverse Polish Notation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tokens": ["2", "1", "+", "3", "*"]}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `tokens` that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.

The objective is to compute `9` from `{"tokens": ["2", "1", "+", "3", "*"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use a stack for unfinished expression values

In Reverse Polish Notation, an operator appears after its two operands. Scanning left to right therefore gives a simple rule:

- a number becomes a value available to a later operator;
- an operator consumes the two most recent available values;
- the computed result becomes one new available value.

The list `s` is used as that stack. Parentheses and precedence rules are unnecessary because token order already says exactly when each operation is ready.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tokens": ["2", "1", "+", "3", "*"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The stack’s meaning after every token

After processing any prefix of `tokens`, `s` contains the values of all complete subexpressions in that prefix that have not yet been consumed by a later operator. Their order matches their left-to-right order in the expression.

For a number token, `int(token)` converts the complete signed string, such as `"-11"`, and appends it. A minus sign inside a numeric token is not confused with the operator token `"-"` because dictionary membership checks the entire string.

For an operator token, validity of the RPN input guarantees at least two available values. The operation consumes those two values and pushes their combined result, preserving the invariant.

At the end, a valid complete expression leaves exactly one value. The source returns `s[0]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the unusual two-pop expression

Suppose the top of the stack ends with left operand `x` followed by right operand `y`:

`[..., x, y]`

Python evaluates function arguments from left to right. First, `s.pop(-2)` removes `x`, the second-last item. The stack becomes `[..., y]`. Then `s.pop(-1)` removes `y`.

The operator is therefore called as `operator(x, y)`, which is the required order.

This is especially important for subtraction and division:

$$
x-y\ne y-x
$$

and generally:

$$
x/y\ne y/x.
$$

A more conventional implementation would pop `y` first and then `x`. This source achieves the same operand ordering through indexed pops.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tokens": ["2", "1", "+", "3", "*"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit conditionals:** Pop right then left and use `if` branches for each operator. It is longer but makes operand order highly visible.
- **Integer-only truncating division:** Compute `abs(x) // abs(y)` and apply the sign. It avoids floating-point conversion and generalizes beyond 32-bit values.
- **Reduce tokens in place:** Replace each operator and its preceding operands inside the input list. Repeated middle deletions make it $O(n^2)$ time.
- **Recursive parser from the end:** Read tokens backward, recursively evaluate the left and right operands in the correct reversed order. It uses $O(n)$ call-stack space.
- **One numeral:** It is pushed and returned with no operation.
- **Negative numeral token:** The full token is not an operator key and `int` parses its sign.
- **Subtraction/division order:** Swapping the operands yields wrong answers; the indexed pops intentionally preserve `x op y`.
- **Division by zero:** The Reference guarantees it never occurs, so no check is needed.
- **Malformed RPN:** Too few operands would raise on `pop`, and surplus operands would violate the final-one-value assumption; the source trusts validity.
- **Runtime dependency:** The source uses `List` without importing it. Standalone Python needs `from typing import List`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of tokens.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

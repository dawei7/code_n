# Guided Example: Evaluate Valid Expressions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "add(2,3)"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `expression` that represents a nested mathematical expression in a simplified form.

The objective is to compute `5` from `{"expression": "add(2,3)"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parse one complete expression and return where it ends

`parse(i)` returns a pair:

- The integer value of the valid expression beginning at index `i`.
- The index immediately after that expression.

Returning the ending position lets a parent parse its first operand, skip the comma, then parse the second without searching for matching parentheses globally.

The grammar guarantees every call begins at either an integer literal or an operator name.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "add(2,3)"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse positive and negative literals

If `expression[i]` is a digit or minus sign, the expression is a literal. A pointer `j` skips an optional minus sign and then advances through every digit. `int(expression[i:j])` converts the exact literal, and `j` already points to its following comma, closing parenthesis, or end of input.

The minus sign cannot be confused with subtraction because the operator is spelled `"sub"` and valid grammar places `'-'` only at a literal start.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `expression[i]` is a digit or minus sign, the expression ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Parse an operation recursively

Otherwise, the source scans from `i` until `'('`. The substring before it is one of `add`, `sub`, `mul`, or `div`.

After the opening parenthesis:

1. Parse the first operand, receiving `val1` and the comma position.
2. Increment `j` once to skip the comma.
3. Parse the second operand, receiving `val2` and the closing-parenthesis position.
4. Increment `j` once to move past the closing parenthesis.
5. Apply the named operation and return its result with `j`.

Nested structure is handled naturally because each operand call consumes its entire subtree before returning.

For `div(mul(4,sub(9,5)),add(1,1))`, the innermost literal calls return first, `sub` becomes four, `mul` becomes sixteen, `add` becomes two, and the root divides to eight.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "add(2,3)"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit value/operator stacks:** A left-to-ri:** - **Explicit value/operator stacks:** A left-to-right iterative parser avoids Python recursion limits and matches the manifest summary, but it is not the shown source.
- **Evaluate with Python `eval`:** The grammar uses custom function names and untrusted-text evaluation would be inappropriate and harder to constrain safely.
- **Repeatedly find innermost parentheses:** This can rescan the string and become quadratic. Returned end indices avoid that.
- **Single literal:** The first parse branch returns it directly, including negative values.
- **Deep nesting:** The algorithmic recurrence is valid, but Python's runtime recursion limit can reject an otherwise allowed expression.
- **Negative exact division:** Floor division equals the exact quotient because the dividend is guaranteed divisible by the divisor.
- **Subtraction yielding negative values:** Results remain integers and feed parent operations normally.
- **Multi-digit literals:** The digit loop consumes the entire token.
- **No whitespace:** The parser does not skip spaces because the contract says none exist.
- **Valid grammar guarantee:** There is no error handling for unknown operators, missing delimiters, or division by zero.
- **Index after root:** The caller ignores it because validity guarantees the root consumes the complete string.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the expression length. Each character participates in constant parsing work, so time complexity is $O(n)$. Integer arithmetic is treated as constant under the signed-long guarantee.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

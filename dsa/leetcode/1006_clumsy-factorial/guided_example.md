# Guided Example: Clumsy Factorial

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **factorial** of a positive integer `n` is the product of all positive integers less than or equal to `n`.

The objective is to compute `7` from `{"n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate the expression while respecting precedence

The operands are `n, n - 1, ..., 1`, and the operations repeat in the order multiplication, division, addition, subtraction.

Ordinary precedence means multiplication and division must be completed before addition and subtraction. A stack of signed additive terms provides a convenient representation:

- multiplication or division immediately changes the most recent term;
- addition appends a new positive term;
- subtraction appends a new negative term;
- summing all final terms evaluates the complete expression.

This avoids constructing or parsing an expression string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start with the first operand

The stack begins as `[n]`. Variable `k = 0` means the next operation is multiplication.

The loop visits every lower integer `x` from `n - 1` down through one. After using one operation, `k = (k + 1) % 4` rotates to the next operation and wraps back to multiplication after subtraction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The stack begins as `[n]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply multiplication to the latest term

When `k == 0`, the code removes the top term, multiplies it by `x`, and pushes the result:

`stk.append(stk.pop() * x)`.

Combining immediately enforces multiplication before any eventual sum. The top term may be positive in the first group or negative after a subtraction; preserving its sign correctly represents subtraction of a later product.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Closed-form pattern:** For sufficiently large :** - **Closed-form pattern:** For sufficiently large `n`, results follow a period based on `n mod 4`. This achieves constant time but is harder to derive and explain safely.
- **One running total plus current term:** Keep the unresolved multiplicative term separately and commit it on addition/subtraction. It can reduce stack storage to constant space while retaining linear time.
- **Build tokens and use a general calculator:** Correct precedence is possible, but the machinery is excessive for a fixed four-operation cycle.
- **Use Python `//` for negative terms:** This floors rather than truncates toward zero and can produce an incorrect extra negative unit.
- **`n = 1`:** The initial stack is returned unchanged.
- **`n = 2`:** Only multiplication occurs, producing two.
- **Cycle ends after any operator:** The loop simply stops when operand one is consumed; no placeholder operation is applied.
- **Negative stack terms:** They arise from subtraction and must remain signed through later multiplication and division.
- **Division by zero:** Impossible because loop operands decrease only through positive integers.
- **Input upper bound:** Direct simulation of at most ten thousand operands is easily manageable.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the input integer. The loop processes each operand from `N - 1` through one exactly once, with constant work per operand. Time complexity is `O(N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

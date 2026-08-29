# Guided Example: Add Two Integers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num1": 12, "num2": 5}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `num1` and `num2`, return *the **sum** of the two integers*.

The objective is to compute `17` from `{"num1": 12, "num2": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The requested operation is exactly integer addition

The function receives two integers and must return their arithmetic sum. Python already defines `+` for integers with precisely these semantics, so the exact solution is

`return num1 + num2`.

There is no transformation, search, iteration, or data structure required. Adding extra machinery would not reveal a hidden constraint because the problem explicitly permits ordinary integer addition and asks for the direct result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num1": 12, "num2": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the expression returns the required value

Integer addition combines signed quantities. For positive inputs, it moves upward by both magnitudes. For two negative inputs, it combines their negative magnitudes. For opposite signs, it subtracts the smaller absolute magnitude from the larger and keeps the sign of the larger magnitude.

Python evaluates `num1 + num2` first and returns that resulting integer. The method has no later statement that could alter it.

For `num1 = 12` and `num2 = 5`, the expression evaluates to seventeen. For `num1 = -10` and `num2 = 4`, adding four moves four units toward zero from negative ten, producing negative six.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Negative signs belong to the values

A negative input is still one integer, not a special string or separate operation. Python's addition operator handles its sign automatically. No manual branching is necessary for combinations such as positive plus negative or negative plus negative.

For example:

- `7 + (-3) = 4`;
- `-7 + 3 = -4`;
- `-7 + (-3) = -10`.

These all follow the same single expression.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num1": 12, "num2": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated increment or decrement:** Move from `num1` one unit at a time according to `num2`. This is slower, more error-prone for negative values, and unnecessary when addition is permitted.
- **Bitwise carry simulation:** XOR and shifted AND can implement addition without `+`, but the problem does not prohibit `+`. Such code obscures the simple contract, especially for Python's signed integers.
- **Convert to strings:** Decimal digit addition would require sign and carry handling and extra memory while producing the same value.
- **One operand zero:** The other operand is returned mathematically through the same expression.
- **Both operands zero:** The result is zero.
- **Two positive operands:** Their magnitudes combine and the result is positive.
- **Two negative operands:** Their absolute magnitudes combine and the result remains negative.
- **Opposite signs with equal magnitude:** They cancel to zero.
- **Opposite signs with unequal magnitude:** The result has the sign of the larger absolute value.
- **Boundary values:** `100 + 100 = 200` and `-100 + -100 = -200` are both safely represented.
- **Parameter order:** Commutativity means exchanging `num1` and `num2` changes nothing.
- **Return type:** Integer operands remain in integer arithmetic, so the method never produces a string or floating-point approximation.
- **Exactness:** Every value in the constraint range is represented exactly; no rounding or precision loss occurs.
- **No input mutation:** Python integers are immutable, and the function has no side effects.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(b)$. Under the problem's fixed bounded integers, one addition takes `O(1)` time. Returning the result also takes `O(1)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

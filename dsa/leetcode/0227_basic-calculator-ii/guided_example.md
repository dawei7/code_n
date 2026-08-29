# Guided Example: Basic Calculator II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "3+2*2"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` which represents an expression, *evaluate this expression and return its value*.

The objective is to compute `7` from `{"s": "3+2*2"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the stack to separate low-precedence terms

Addition and subtraction divide the expression into terms. Multiplication and
division belong inside the current term because they have higher precedence.
The exact solution stores each completed additive term in `stk`:

- a term preceded by `+` is stored as a positive value;
- a term preceded by `-` is stored as a negative value;
- `*` and `/` immediately combine the next number with the most recent stack
  term instead of creating another term.

After every multiplication and division chain has been collapsed, summing the
stack is equivalent to evaluating all remaining additions. This avoids a full
operator-precedence parser because the grammar has only two precedence levels
and no parentheses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "3+2*2"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: `sign` describes the operator before the number being built

The parser starts with `sign = '+'`. This imaginary leading plus makes the
first number follow the same processing rule as later positive terms.
Variable `v` accumulates the current number. For every digit `c`, the update
`v = v * 10 + int(c)` shifts existing decimal digits left and appends the new
digit. Thus `"205"` builds 2, then 20, then 205.

When the scan reaches an operator, that operator comes after the number in
`v`. The number must be processed using the previous `sign`, not using the
newly encountered operator. Only afterward does `sign = c` save the current
operator for the number to its right.

For `3+2*2`, the first `+` causes 3 to be processed under the initial plus and
placed on the stack. That encountered plus becomes the pending sign. At `*`,
the value 2 is appended under plus; then `*` becomes pending. At the final 2,
the pending multiplication pops the previous 2, multiplies it by the current
2, and pushes 4. The final stack is `[3, 4]`, whose sum is 7.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process a number when an operator or the physical end is reached

The condition `i == n - 1 or c in '+-*/'` is the parser's token boundary. An
operator always ends the preceding number. The last character must also force
the final number to be applied because no later operator exists to trigger it.

This handles both a final digit and trailing spaces. If the last character is
a digit, the first `if` adds it to `v` before the boundary condition processes
the full number. If the expression ends in spaces, intermediate spaces leave
`v` untouched and the final space triggers processing of the number already
built. Ordinary spaces elsewhere match neither branch and are simply ignored.

After processing a boundary, the method assigns `v = 0` so digits of the next
number start fresh. It also assigns `sign = c`. At a true operator boundary,
that saves a valid operator. At the final digit or space, the stored value is
not an operator, but the loop ends immediately, so that last assignment is
never observed and is harmless under valid input.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "3+2*2"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Finalized sum plus current term:** Add the previous term to a running result only when a new `+` or `-` starts, while folding `*` and `/` into one `last` value. It achieves the same $O(n)$ time with $O(1)$ space and matches the manifest summary.
- **Two-stack precedence parser:** Maintain separate number and operator stacks and reduce according to precedence. It generalizes more easily to parentheses and more operators but adds unnecessary machinery here.
- **Recursive descent:** Parse additive and multiplicative grammar levels with functions. It is clear and extensible, but this no-parentheses grammar can be handled more compactly by one pass.
- **Trailing spaces:** Only the final physical character triggers completion. The accumulated `v` survives all preceding spaces, so the last number is still applied exactly once.
- **Leading spaces:** They perform no action; the initial plus remains pending for the first number.
- **Multi-digit zero-containing numbers:** Decimal accumulation correctly distinguishes values such as 0, 10, and 105.
- **Division truncation for a negative term:** `int(stk.pop() / v)` truncates toward zero, unlike floor division. This matters because subtraction can make the stored term negative even though lexical numbers are nonnegative.
- **Division by zero:** A valid expression under the intended arithmetic contract does not require evaluating division by zero; the source has no special guard.
- **Long multiplication/division chain:** Each operator immediately replaces the last term, preserving left-to-right evaluation without growing the stack for every factor.
- **Only one number:** The end condition appends it under the imaginary leading plus, and `sum` returns it.
- **No parentheses:** Parentheses are outside this problem's input alphabet. Supporting them would require saved contexts or a fuller parser.
- **Intermediate range:** The reference guarantees signed 32-bit intermediate results, which also keeps the source's float-assisted division exact for these values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters in `s`. The `for` loop visits each
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

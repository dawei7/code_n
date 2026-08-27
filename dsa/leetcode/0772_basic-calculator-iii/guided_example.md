# Guided Example: Basic Calculator III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1+1"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement a basic calculator to evaluate a simple expression string.

The objective is to compute `2` from `{"s": "1+1"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Evaluate one parenthesized level at a time

The exact solution converts the input string into a deque of characters and calls recursive `dfs`. One call evaluates until it consumes the deque or encounters the closing parenthesis belonging to that level.

Each call maintains:

- `num`: the integer literal or nested-expression value currently being built.
- `sign`: the operator that must be applied to `num`.
- `stk`: signed terms whose sum is the value of this level.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1+1"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build multi-digit integers

When a digit is read, `num = num * 10 + digit`. Consecutive digits therefore form one decimal value.

The number is not committed immediately because later digits may belong to it. It is committed when an operator, closing parenthesis, or end of input is reached.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When a digit is read, `num = num * 10 + digit`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Evaluate parentheses recursively

When `(` appears, the method recursively evaluates the following characters. The nested call stops after processing its matching `)` and returns the parenthesized integer.

That value replaces `num`, so the outer level treats the entire parenthesized expression as one operand. This automatically gives parentheses highest precedence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1+1"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Shunting-yard algorithm:** Convert to postfix :** - **Shunting-yard algorithm:** Convert to postfix using operator stacks, then evaluate. It is iterative but requires more explicit machinery.
- **- **Recursive-descent parser by grammar levels:** :** - **Recursive-descent parser by grammar levels:** Separate expression, term, and factor functions. This is very clear and avoids the signed-term trick.
- **- **Use `//` for division:** It is wrong for negat:** - **Use `//` for division:** It is wrong for negative quotients because it floors instead of truncating toward zero.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the expression length. Every character is removed from the deque once and processed by one recursive level. Stack operations are constant time, so total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Basic Calculator IV

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "e + 8 - a + 5", "evalvars": ["e"], "evalints": [1]}`
- **Required output:** `["-1*a", "14"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an expression such as $expression = "e + 8 - a + 5"$ and an evaluation map such as `{"e": 1}` (given in terms of $evalvars = ["e"]$ and $evalints = [1]$), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

The objective is to compute `["-1*a", "14"]` from `{"expression": "e + 8 - a + 5", "evalvars": ["e"], "evalints": [1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a polynomial canonically

The evaluator must combine like terms, substitute selected variables, respect precedence, and format remaining variables in a fixed order.

The exact solution represents a polynomial as a dictionary:

- A key is a tuple of free-variable names forming one monomial.
- The tuple is sorted lexicographically and preserves repetition.
- The value is the integer coefficient.

For example, `3*a*a*b` is stored as key `("a", "a", "b")` with coefficient three. A constant uses the empty tuple `()`.

This canonical key makes algebraically identical products combine even if their variables appeared in different input orders.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "e + 8 - a + 5", "evalvars": ["e"], "evalints": [1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Tokenize before parsing

The regular expression extracts variable names, nonnegative integer literals, parentheses, and operators while ignoring spaces. Multi-letter variables and multi-digit numbers each become one token.

`position` is a shared index into this token list. Recursive parsing consumes tokens exactly once in grammatical order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use three parser levels for precedence

`parse_expression` handles addition and subtraction. It first parses one term, then repeatedly consumes `+` or `-` followed by another term.

`parse_term` handles multiplication. It parses one factor, then repeatedly multiplies by following factors separated by `*`.

`parse_factor` handles the indivisible units: parenthesized expressions, integer literals, substituted variables, and free variables.

Because an expression asks for complete terms before adding them, multiplication binds more tightly. Recursive factor parsing makes parentheses bind most tightly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["-1*a", "14"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "e + 8 - a + 5", "evalvars": ["e"], "evalints": [1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["-1*a", "14"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use Python `eval`:** Forbidden and would not produce canonical symbolic polynomial terms.
- **Build an abstract syntax tree first:** It separates parsing and evaluation but adds a full tree allocation.
- **Keep variables in encounter order:** Products such as `a*b` and `b*a` would fail to combine. Sort every monomial key.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p \log p)$. Polynomial size can expand through multiplication. Let `P` be the total number of term-pair products performed across all multiplications and `U` the number of final nonzero monomials. Parsing and combination take `O(P)` dictionary work plus the cost of sorting variable tuples in produced monomials.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

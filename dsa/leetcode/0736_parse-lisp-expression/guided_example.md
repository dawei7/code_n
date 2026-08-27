# Guided Example: Parse Lisp Expression

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "(let x 2 (mult x (let x 3 y 4 (add x y))))"}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string expression representing a Lisp-like expression to return the integer value of.

The objective is to compute `14` from `{"expression": "(let x 2 (mult x (let x 3 y 4 (add x y))))"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parse and evaluate at the same time

The expression grammar is recursive: an expression may be an integer, a variable, or a parenthesized `let`, `add`, or `mult` expression containing other expressions. The exact solution uses a recursive evaluator with one shared character index `i`.

Rather than building a separate syntax tree, each call reads the expression beginning at `i`, computes its integer value, and leaves `i` at the delimiter immediately after that expression. This avoids a second traversal and keeps parsing aligned with evaluation.

Variable scope is represented by `scope`, a map from each variable name to a stack of currently active values. The last value in the list is the innermost binding.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "(let x 2 (mult x (let x 3 y 4 (add x y))))"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse atomic tokens

`parseVar` records the current index, advances until a space or closing parenthesis, and returns that substring. Variable names may contain lowercase letters and digits after their first letter, so delimiter-based scanning is simpler than checking every permitted character class.

`parseInt` handles an optional leading minus sign, then accumulates decimal digits with

`v = v * 10 + digit`.

It returns the signed integer and leaves `i` at the next delimiter.

When `eval` sees that the current character is not `(`, it distinguishes a variable from an integer by the first character. A lowercase letter begins a variable and the value is `scope[name][-1]`. A digit or minus sign begins an integer.

The input is guaranteed legal, so every evaluated variable has an active binding.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `parseVar` records the current index, advances until a space... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize a parenthesized operator

When an expression begins with `(`, `eval` advances past it. The first operator character then identifies the form:

- `l` begins `let`.
- `a` begins `add`.
- Otherwise the legal remaining operator is `mult`.

The pointer increments skip the operator word and following space: four characters for `"add "` or `"let "`, and five for `"mult "`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "(let x 2 (mult x (let x 3 y 4 (add x y))))"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Tokenize first, then recursively evaluate toke:** - **Tokenize first, then recursively evaluate tokens:** This separates lexical analysis from grammar handling and can be easier to debug, but stores `O(n)` tokens in addition to scope and recursion state.
- **- **Build an abstract syntax tree:** A tree is use:** - **Build an abstract syntax tree:** A tree is useful if the expression must be inspected or evaluated repeatedly. For one evaluation it adds objects and a second traversal without improving asymptotic time.
- **- **Copy the complete environment for nested calls:** - **Copy the complete environment for nested calls:** This makes lexical scoping conceptually simple but can copy many bindings repeatedly and lead to quadratic work. Per-variable stacks update and restore only changed names.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the expression length. The shared index moves forward across tokens and delimiters. Each character participates in only a constant amount of parsing work, so total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

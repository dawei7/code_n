# Guided Example: Parsing A Boolean Expression

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "&(|(f))"}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **boolean expression** is an expression that evaluates to either `true` or `false`. It can be in one of the following shapes:

The objective is to compute `false` from `{"expression": "&(|(f))"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce completed subexpressions with a stack

The expression is nested. A closing parenthesis marks the moment when every operand of one operator has been seen, so the solution scans left to right and postpones evaluation until that closing marker.

The stack stores only meaningful tokens: literal results `t` and `f` plus operators `!`, `&`, and `|`. Opening parentheses and commas are structural separators, so the loop deliberately ignores them.

Nested subexpressions do not remain as raw text. When one closes, it is evaluated immediately and its single literal result is pushed. Its parent then sees that result exactly like an original `t` or `f` operand.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "&(|(f))"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collect the operands at a closing parenthesis

When `c == ')'`, the top of the stack contains the completed operator’s operand results. The loop pops consecutive `t` and `f` tokens, counting true results in `t` and false results in `f`.

After those literals are removed, the next stack item is the operator that opened this subexpression. Valid syntax guarantees this arrangement and guarantees at least one operand.

Only counts are needed. AND cares whether any false value exists, OR cares whether any true value exists, and NOT has exactly one operand. Their original ordering does not affect the Boolean result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `c == ')'`, the top of the stack contains the completed... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the operator

For `!`, the code produces true when `f` is nonzero and false otherwise. Since NOT has exactly one operand, this changes false to true and true to false.

For `&`, any false operand makes the result false. If `f` is zero, every operand was true, so the result is true.

For `|`, any true operand makes the result true. If `t` is zero, every operand was false.

The resulting character is pushed onto the stack, replacing the whole parenthesized expression with one value. This is the key invariant: after processing any prefix, the stack represents operators still waiting for closure and literal results of all completed children.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "&(|(f))"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive descent:** Parse one expression at a:** - **Recursive descent:** Parse one expression at a time and return its Boolean value plus the next index. This follows the grammar directly but can reach deep recursion.
- **Replace innermost text repeatedly:** Search for closing parentheses and rewrite strings. Immutable string construction and repeated scans can lead to quadratic time.
- **Store every punctuation token:** A conventional stack parser can push parentheses and commas too, but they carry no information needed by this reduction.
- **Single literal `t`:** It remains the only stack value and returns true.
- **Single literal `f`:** It remains the only stack value and returns false.
- **NOT:** Valid syntax supplies exactly one operand, making the “any false” check equivalent to negation.
- **One-operand AND or OR:** Both return that operand, and the count tests handle them naturally.
- **Many operands:** Only two counters are needed regardless of count because AND and OR short semantic summaries are sufficient.
- **Nested operators:** Each child is reduced before its parent closes, so the parent receives literals rather than unresolved syntax.
- **Commas:** They merely separate operands and are safely ignored.
- **Valid-input guarantee:** The code does not defend against an empty stack, missing operator, or malformed arity; those cases are outside the contract.
- **Python pattern matching:** Every popped operator is one of the three handled cases, so `c` is always assigned a result before being pushed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the expression length. Every relevant token is pushed once and popped at most once. Although a closing parenthesis may pop many operands, those tokens never reappear, so the total stack work across the full scan is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

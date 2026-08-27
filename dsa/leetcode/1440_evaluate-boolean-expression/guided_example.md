# Guided Example: Evaluate Boolean Expression

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Variables": [{"name": "x", "value": 66}, {"name": "y", "value": 77}], "Expressions": [{"left_operand": "x", "operator": ">", "right_operand": "y"}, {"left_operand": "x", "operator": "<", "right_operand": "y"}, {"left_operand": "x", "operator": "=", "right_operand": "y"}, {"left_operand": "y", "operator": ">", "right_operand": "x"}, {"left_operand": "y", "operator": "<", "right_operand": "x"}, {"left_operand": "x", "operator": "=", "right_operand": "x"}]}}`
- **Required output:** `{"columns": ["left_operand", "operator", "right_operand", "value"], "rows": [["x", ">", "y", "false"], ["x", "<", "y", "true"], ["x", "=", "y", "false"], ["y", ">", "x", "true"], ["y", "<", "x", "false"], ["x", "=", "x", "true"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table `Variables`:

The objective is to compute `{"columns": ["left_operand", "operator", "right_operand", "value"], "rows": [["x", ">", "y", "false"], ["x", "<", "y", "true"], ["x", "=", "y", "false"], ["y", ">", "x", "true"], ["y", "<", "x", "false"], ["x", "=", "x", "true"]]}` from `{"tables": {"Variables": [{"name": "x", "value": 66}, {"name": "y", "value": 77}], "Expressions": [{"left_operand": "x", "operator": ">", "right_operand": "y"}, {"left_operand": "x", "operator": "<", "right_operand": "y"}, {"left_operand": "x", "operator": "=", "right_operand": "y"}, {"left_operand": "y", "operator": ">", "right_operand": "x"}, {"left_operand": "y", "operator": "<", "right_operand": "x"}, {"left_operand": "x", "operator": "=", "right_operand": "x"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Turn names into values before evaluating anything.** Each row of `Expressions` contains two variable names and one operator, not the numbers that should actually be compared. For example, a row might say that the left operand is `x`, the operator is `>`, and the right operand is `y`. The numerical values of `x` and `y` live in `Variables`. The query therefore has two logically separate jobs: look up both operand values, and then apply the row's operator to those values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Variables": [{"name": "x", "value": 66}, {"name": "y", "value": 77}], "Expressions": [{"left_operand": "x", "operator": ">", "right_operand": "y"}, {"left_operand": "x", "operator": "<", "right_operand": "y"}, {"left_operand": "x", "operator": "=", "right_operand": "y"}, {"left_operand": "y", "operator": ">", "right_operand": "x"}, {"left_operand": "y", "operator": "<", "right_operand": "x"}, {"left_operand": "x", "operator": "=", "right_operand": "x"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The same `Variables` table must participate twice because one expression refers to it twice. The query gives those two roles different aliases:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The same `Variables` table must participate twice because on... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `v1` represents the variable named by `left_operand`.
- `v2` represents the variable named by `right_operand`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["left_operand", "operator", "right_operand", "value"], "rows": [["x", ">", "y", "false"], ["x", "<", "y", "true"], ["x", "=", "y", "false"], ["y", ">", "x", "true"], ["y", "<", "x", "false"], ["x", "=", "x", "true"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Variables": [{"name": "x", "value": 66}, {"name": "y", "value": 77}], "Expressions": [{"left_operand": "x", "operator": ">", "right_operand": "y"}, {"left_operand": "x", "operator": "<", "right_operand": "y"}, {"left_operand": "x", "operator": "=", "right_operand": "y"}, {"left_operand": "y", "operator": ">", "right_operand": "x"}, {"left_operand": "y", "operator": "<", "right_operand": "x"}, {"left_operand": "x", "operator": "=", "right_operand": "x"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["left_operand", "operator", "right_operand", "value"], "rows": [["x", ">", "y", "false"], ["x", "<", "y", "true"], ["x", "=", "y", "false"], ["y", ">", "x", "true"], ["y", "<", "x", "false"], ["x", "=", "x", "true"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two correlated scalar subqueries:** The query :** - **Two correlated scalar subqueries:** The query could look up the left and right values with separate subqueries in the `SELECT` list. That can express the same logic, but the two explicit joins make the two operand roles clearer and usually give the optimizer a more direct relational plan.
- **A single occurrence of Variables:** One alias cannot independently match two possibly different operand names. Requiring one joined row to have both names would fail whenever `left_operand` and `right_operand` differ, so two aliases are the natural representation.
- **Nested CASE branches:** A first `CASE` could choose the operator and a nested expression could perform its comparison. It is valid, but the guarded `OR` terms keep all three legal cases visible in one condition.
- **MySQL IF expressions:** Chained `IF` calls can produce the required strings, but they are more vendor-specific and tend to obscure the exhaustive three-operator decision.
- **Equal operand names:** An expression such as `x = x` is handled normally. Both aliases resolve to the same unique row, and equality is true; `x < x` and `x > x` are false.
- **Equal values under different names:** Two names may map to the same integer. The query compares values rather than names, so `a = b` can correctly be true even when `a` and `b` are distinct identifiers.
- **Negative and zero values:** Standard integer comparisons already order negative numbers, zero, and positive numbers correctly. No absolute value or special sign handling is needed.
- **Missing operands outside the contract:** If an operand name were absent, the inner join would remove that expression. A more defensive, different specification could use `LEFT JOIN` and define how `NULL` should be reported, but this problem guarantees the lookup exists.
- **Unexpected operators outside the contract:** Any unrecognized operator would reach `ELSE` and be labeled `false`. That behavior is not relied on because the input restricts the operator to `<`, `>`, or `=`.
- **SQL NULL values outside the contract:** If operand values could be `NULL`, comparisons would evaluate to unknown rather than true, and `CASE` would return `false`. The stated integer schema does not require a separate null policy.
- **Output order:** The result may be returned in any order. Tests should compare the required rows according to that contract instead of assuming insertion order.
- **Exact text casing:** The required results are lowercase `true` and `false`. Returning Boolean values, uppercase words, or numeric `1` and `0` would not faithfully produce the requested output representation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$. Let `V` be the number of rows in `Variables` and `E` the number of rows in `Expressions`. Under the usual hash-join execution model, the database can scan `Variables` to build a name-to-value lookup and scan the expressions while probing that lookup for both operands. Building and probing are linear in the rows involved, so the expected running time is `O(V + E)`. Evaluating the fixed three-way `CASE` costs constant time per expression.
- **Auxiliary Space Complexity:** $O(V+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

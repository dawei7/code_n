# Guided Example: The Number of Seniors and Juniors to Join the Company

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Candidates": [{"employee_id": 1, "experience": "Junior", "salary": 10000}, {"employee_id": 9, "experience": "Junior", "salary": 10000}, {"employee_id": 2, "experience": "Senior", "salary": 20000}, {"employee_id": 11, "experience": "Senior", "salary": 20000}, {"employee_id": 13, "experience": "Senior", "salary": 50000}, {"employee_id": 4, "experience": "Junior", "salary": 40000}]}}`
- **Required output:** `{"columns": ["experience", "accepted_candidates"], "rows": [["Senior", 2], ["Junior", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Candidates`

The objective is to compute `{"columns": ["experience", "accepted_candidates"], "rows": [["Senior", 2], ["Junior", 2]]}` from `{"tables": {"Candidates": [{"employee_id": 1, "experience": "Junior", "salary": 10000}, {"employee_id": 9, "experience": "Junior", "salary": 10000}, {"employee_id": 2, "experience": "Senior", "salary": 20000}, {"employee_id": 11, "experience": "Senior", "salary": 20000}, {"employee_id": 13, "experience": "Senior", "salary": 50000}, {"employee_id": 4, "experience": "Junior", "salary": 40000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Hire the cheapest seniors first

To maximize the number of candidates from one experience group under a fixed budget, choose salaries in ascending order. If a chosen set contains a more expensive candidate while a cheaper unchosen candidate exists, swapping them cannot increase cost and preserves the number hired. Repeating yields an optimal cheapest-prefix selection.

CTE `s` filters senior candidates and computes a cumulative salary `cur` using `SUM(salary) OVER (ORDER BY salary)`. Intended row by intended row, `cur` is the cost of hiring the cheapest seniors through that candidate.

The final senior count includes rows with `cur <= 70000`, representing the largest affordable senior prefix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Candidates": [{"employee_id": 1, "experience": "Junior", "salary": 10000}, {"employee_id": 9, "experience": "Junior", "salary": 10000}, {"employee_id": 2, "experience": "Senior", "salary": 20000}, {"employee_id": 11, "experience": "Senior", "salary": 20000}, {"employee_id": 13, "experience": "Senior", "salary": 50000}, {"employee_id": 4, "experience": "Junior", "salary": 40000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reserve the amount spent on seniors

Before considering juniors, the company must keep the optimal senior decision fixed. The scalar calculation inside CTE `j` intends to obtain `MAX(cur)` among affordable senior prefix totals. If no senior prefix fits, `COALESCE(..., 0)` intends to make senior spending zero.

Each junior running salary is then added to that senior cost. A junior row whose combined `cur` is at most 70000 belongs to the cheapest affordable junior prefix.

This expresses the priority correctly: senior count is maximized first; juniors receive only the remaining budget.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Before considering juniors, the company must keep the optima... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Return both categories even when a count is zero

The first aggregate selects the constant label Senior and counts affordable rows from `s`. The second does the same for Junior from `j`.

`COUNT(employee_id)` over an empty filtered result returns zero, so both branches still produce one aggregate row. `UNION ALL` combines the two required categories without duplicate-removal work.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["experience", "accepted_candidates"], "rows": [["Senior", 2], ["Junior", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Candidates": [{"employee_id": 1, "experience": "Junior", "salary": 10000}, {"employee_id": 9, "experience": "Junior", "salary": 10000}, {"employee_id": 2, "experience": "Senior", "salary": 20000}, {"employee_id": 11, "experience": "Senior", "salary": 20000}, {"employee_id": 13, "experience": "Senior", "salary": 50000}, {"employee_id": 4, "experience": "Junior", "salary": 40000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["experience", "accepted_candidates"], "rows": [["Senior", 2], ["Junior", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Corrected window query:** Parenthesize the sca:** - **Corrected window query:** Parenthesize the scalar subquery and use `ROWS UNBOUNDED PRECEDING` with `employee_id` as a deterministic salary tie-breaker.
- **Ranked candidates plus recursive budget:** More verbose, but can state one-candidate-at-a-time selection explicitly.
- **Procedural sort and scan:** Sort seniors, consume budget, then sort juniors and consume the remainder; directly mirrors the greedy proof.
- **No affordable senior:** Senior count is zero and juniors receive all 70000.
- **No affordable junior:** Junior count is zero after senior spending.
- **No candidates in a category:** Aggregate count should still return that category with zero.
- **Salary exactly equals remaining budget:** The candidate is affordable because the comparison is `<=`.
- **Equal salaries:** Require row-based framing; the exact default frame can undercount a partially affordable tie.
- **Senior priority:** A cheaper junior never displaces a senior if doing so would reduce maximum senior count.
- **Scalar-subquery syntax:** The exact source is invalid without an inner pair of parentheses.
- **`UNION ALL`:** Appropriate because the two literal experience labels are distinct.
- **Any result order:** No final `ORDER BY` is necessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of candidates. Filtering is linear. The senior and junior window functions order rows by salary, typically costing $O(N\log N)$ total time. Aggregation and filtering add $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

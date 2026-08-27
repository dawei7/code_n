# Guided Example: Sort the Olympic Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Olympic": [{"country": "China", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "South Sudan", "gold_medals": 0, "silver_medals": 0, "bronze_medals": 1}, {"country": "USA", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "Israel", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 3}, {"country": "Egypt", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 2}]}}`
- **Required output:** `{"columns": ["country", "gold_medals", "silver_medals", "bronze_medals"], "rows": [["China", 10, 10, 20], ["USA", 10, 10, 20], ["Israel", 2, 2, 3], ["Egypt", 2, 2, 2], ["South Sudan", 0, 0, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Olympic`

The objective is to compute `{"columns": ["country", "gold_medals", "silver_medals", "bronze_medals"], "rows": [["China", 10, 10, 20], ["USA", 10, 10, 20], ["Israel", 2, 2, 3], ["Egypt", 2, 2, 2], ["South Sudan", 0, 0, 1]]}` from `{"tables": {"Olympic": [{"country": "China", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "South Sudan", "gold_medals": 0, "silver_medals": 0, "bronze_medals": 1}, {"country": "USA", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "Israel", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 3}, {"country": "Egypt", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the ranking rules directly into sort keys

Every row must remain intact; the task changes only row order. The ranking is hierarchical:

1. more gold medals ranks first;
2. when gold ties, more silver ranks first;
3. when both tie, more bronze ranks first;
4. when all medals tie, lexicographically smaller country ranks first.

SQL's `ORDER BY` accepts multiple keys and compares them from left to right. A later key is consulted only when every earlier key ties, exactly matching this hierarchy.

The query returns every column with `SELECT *` and orders by:



These numbers are positional references to expressions in the selected row, not literal constants.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Olympic": [{"country": "China", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "South Sudan", "gold_medals": 0, "silver_medals": 0, "bronze_medals": 1}, {"country": "USA", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "Israel", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 3}, {"country": "Egypt", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Decode every positional reference

The table's selected column order is:



Therefore, `2 DESC` means greatest gold count first. `3 DESC` means greatest silver count first among rows tied on gold. `4 DESC` performs the bronze tie-break.

The final `1` means `country`. SQL ordering is ascending when no direction is written, so it puts country names in ascending lexicographic order for a complete medal tie. Writing `1 ASC` would be equivalent.

Changing the order of these clauses would change the ranking policy. For example, bronze before silver would allow a higher bronze count to override a silver advantage, contrary to the statement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The table's selected column order is:



Therefore, `2 DESC`... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How lexicographic multi-key comparison works

Imagine assigning each row the conceptual ordering tuple:

$$
(-g,-s,-b,c),
$$

where $g$, $s$, and $b$ are medal counts and $c$ is the country name. Ascending tuple order would rank larger counts first because of the negative signs and names normally. SQL expresses the same idea with three `DESC` directions followed by ascending country.

The database does not add medal counts together. Ten gold and zero silver always outranks nine gold and a huge silver count because gold is the first key. The next medal category is used only under an exact tie in all earlier categories.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["country", "gold_medals", "silver_medals", "bronze_medals"], "rows": [["China", 10, 10, 20], ["USA", 10, 10, 20], ["Israel", 2, 2, 3], ["Egypt", 2, 2, 2], ["South Sudan", 0, 0, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Olympic": [{"country": "China", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "South Sudan", "gold_medals": 0, "silver_medals": 0, "bronze_medals": 1}, {"country": "USA", "gold_medals": 10, "silver_medals": 10, "bronze_medals": 20}, {"country": "Israel", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 3}, {"country": "Egypt", "gold_medals": 2, "silver_medals": 2, "bronze_medals": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["country", "gold_medals", "silver_medals", "bronze_medals"], "rows": [["China", 10, 10, 20], ["USA", 10, 10, 20], ["Israel", 2, 2, 3], ["Egypt", 2, 2, 2], ["South Sudan", 0, 0, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit column names:** `ORDER BY gold_medals:** - **Explicit column names:** `ORDER BY gold_medals DESC, silver_medals DESC, bronze_medals DESC, country ASC` is equivalent and more robust if select-column order changes.
- **Combined medal total:** Sorting by total medals is wrong because the ranking is lexicographic by medal type, not by sum.
- **Omit the country key:** Complete medal ties would have unspecified row order and fail the explicit name tie-break.
- **Country ordered descending:** This reverses the final rule and would put USA before China in the example.
- **Gold tie only:** Silver decides before bronze or country is considered.
- **Gold and silver tie:** Bronze decides.
- **All medal counts tie:** Ascending country name is the sole deciding key.
- **Zero medals:** Zero values sort normally; they do not require null handling.
- **One row:** It is returned unchanged because no comparison is necessary.
- **Positional-key fragility:** `2`, `3`, `4`, and `1` rely on the `SELECT *` column order shown by the schema.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of country rows. A comparison sort needs $O(R\log R)$ comparisons in the general case. Each comparison examines at most four fixed fields, so the overall time is $O(R\log R)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

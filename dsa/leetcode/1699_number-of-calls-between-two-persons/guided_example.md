# Guided Example: Number of Calls Between Two Persons

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Calls": [{"from_id": 1, "to_id": 2, "duration": 59}, {"from_id": 2, "to_id": 1, "duration": 11}, {"from_id": 1, "to_id": 3, "duration": 20}, {"from_id": 3, "to_id": 4, "duration": 100}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 4, "to_id": 3, "duration": 499}]}}`
- **Required output:** `{"columns": ["person1", "person2", "call_count", "total_duration"], "rows": [[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Calls`

The objective is to compute `{"columns": ["person1", "person2", "call_count", "total_duration"], "rows": [[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]]}` from `{"tables": {"Calls": [{"from_id": 1, "to_id": 2, "duration": 59}, {"from_id": 2, "to_id": 1, "duration": 11}, {"from_id": 1, "to_id": 3, "duration": 20}, {"from_id": 3, "to_id": 4, "duration": 100}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 4, "to_id": 3, "duration": 499}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat a conversation pair as unordered

Each source row records a directional call from `from_id` to `to_id`, but the requested result combines calls in both directions. The calls `1 -> 2` and `2 -> 1` must therefore share one grouping key.

The query creates a canonical ordered representation of an unordered pair. For every row, the smaller user ID becomes `person1` and the larger becomes `person2`:

`IF(from_id < to_id, from_id, to_id) AS person1`

and

`IF(from_id < to_id, to_id, from_id) AS person2`.

The contract guarantees `from_id != to_id`, so exactly one of the two IDs is smaller. The two expressions neither lose nor duplicate an endpoint. They merely normalize direction. Whether the original caller was the smaller or larger person, the resulting pair is always `(min(from_id, to_id), max(from_id, to_id))`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Calls": [{"from_id": 1, "to_id": 2, "duration": 59}, {"from_id": 2, "to_id": 1, "duration": 11}, {"from_id": 1, "to_id": 3, "duration": 20}, {"from_id": 3, "to_id": 4, "duration": 100}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 4, "to_id": 3, "duration": 499}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why canonicalization is necessary before grouping

SQL grouping compares the values of its grouping expressions. Without normalization, `(1, 2)` and `(2, 1)` are different ordered pairs and would produce separate output rows. Canonicalization maps both to `(1, 2)`, giving the database one stable key for the relationship.

This is a general technique for symmetric relationships: define a canonical orientation first, then aggregate. It avoids joining the table to a reversed copy and avoids a later step that would have to merge two directional summaries.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | SQL grouping compares the values of its grouping expressions... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group by the two projected person columns

`GROUP BY 1, 2` means group by the first and second expressions in the select list. In this query those expressions are the two `IF` calculations that produce `person1` and `person2`. It is equivalent in intent to grouping by the canonical pair expressions explicitly.

Every input row enters exactly one group because its two endpoint IDs have one unique smaller-larger ordering. All calls between the same two persons enter that same group, regardless of direction. Calls involving a different person differ in at least one canonical key and remain separate.

Ordinal grouping is concise, but the numbers refer to select-list positions rather than literal values. Reordering the projected columns without updating `GROUP BY 1, 2` could change the query's meaning, which is an implementation-maintenance concern rather than an issue for the current fixed statement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["person1", "person2", "call_count", "total_duration"], "rows": [[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Calls": [{"from_id": 1, "to_id": 2, "duration": 59}, {"from_id": 2, "to_id": 1, "duration": 11}, {"from_id": 1, "to_id": 3, "duration": 20}, {"from_id": 3, "to_id": 4, "duration": 100}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 3, "to_id": 4, "duration": 200}, {"from_id": 4, "to_id": 3, "duration": 499}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["person1", "person2", "call_count", "total_duration"], "rows": [[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LEAST` and `GREATEST`:** `LEAST(from_id, to_i:** - **`LEAST` and `GREATEST`:** `LEAST(from_id, to_id)` and `GREATEST(from_id, to_id)` express the same canonical pair more directly in MySQL. The exact source uses two `IF` expressions instead.
- **Union both directions:** Creating a reversed copy with `UNION ALL` is unnecessary and risks counting every call twice unless followed by careful filtering.
- **Aggregate direction first:** One could summarize ordered pairs and then combine reverse summaries, but canonicalizing each row before one aggregation is simpler.
- **Distinct counting:** `COUNT(DISTINCT duration)` or deduplicating rows would lose legitimate repeated call records and is not equivalent to counting calls.
- **Duplicate rows:** Every duplicate contributes one call and its full duration because the table models events and has no uniqueness guarantee.
- **Only one direction present:** All rows still normalize to the required smaller-larger pair; a reverse-direction row is not required.
- **Calls in both directions:** They merge into one group because direction is deliberately discarded from the key.
- **One call for a pair:** Its output count is one and its total duration is that row's duration.
- **Several different pairs sharing a person:** For example, `(1,2)` and `(1,3)` remain different because the second canonical key differs.
- **Self-calls:** The stated contract excludes them. If generalized data allowed `from_id = to_id`, both expressions would yield the same person and violate the requested distinct-person condition unless filtered.
- **Null endpoints outside the contract:** MySQL comparisons with null do not evaluate as true, so generalized nullable data would require explicit handling.
- **Large totals:** The database's `SUM` return type must accommodate the accumulated duration; MySQL promotes integer sums appropriately under its aggregate rules.
- **Any-order output:** Consumers must not rely on the incidental order produced by grouping; add `ORDER BY person1, person2` only if a separate caller requires it.
- **Ordinal grouping:** `GROUP BY 1, 2` is valid here but tied to projection order; spelling out the canonical expressions can be safer during later query maintenance.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of rows in `Calls` and $P$ the number of distinct unordered person pairs represented. In an expected hash-aggregation execution, the database scans each row once, evaluates two constant-time comparisons and conditional selections, and updates one group's count and sum. This gives expected $O(R)$ time.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

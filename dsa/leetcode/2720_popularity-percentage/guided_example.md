# Guided Example: Popularity Percentage

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friends": [{"user1": 2, "user2": 1}, {"user1": 1, "user2": 3}, {"user1": 4, "user2": 1}, {"user1": 1, "user2": 5}, {"user1": 1, "user2": 6}, {"user1": 2, "user2": 6}, {"user1": 7, "user2": 2}, {"user1": 8, "user2": 3}, {"user1": 3, "user2": 9}]}}`
- **Required output:** `{"columns": ["user1", "percentage_popularity"], "rows": [[1, 55.56], [2, 33.33], [3, 33.33], [4, 11.11], [5, 11.11], [6, 22.22], [7, 11.11], [8, 11.11], [9, 11.11]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friends`

The objective is to compute `{"columns": ["user1", "percentage_popularity"], "rows": [[1, 55.56], [2, 33.33], [3, 33.33], [4, 11.11], [5, 11.11], [6, 22.22], [7, 11.11], [8, 11.11], [9, 11.11]]}` from `{"tables": {"Friends": [{"user1": 2, "user2": 1}, {"user1": 1, "user2": 3}, {"user1": 4, "user2": 1}, {"user1": 1, "user2": 5}, {"user1": 1, "user2": 6}, {"user1": 2, "user2": 6}, {"user1": 7, "user2": 2}, {"user1": 8, "user2": 3}, {"user1": 3, "user2": 9}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent an undirected friendship in both directions

Each row of `Friends` stores two participants, but friendship is mutual. If a source row is `(2, 1)`, user two has friend one and user one has friend two. Grouping only by the original `user1` column would omit every friendship from the perspective of a participant appearing in `user2`.

The common table expression `F` fixes this by combining:

- `SELECT * FROM Friends`, which emits `(user1, user2)`;
- `SELECT user2, user1 FROM Friends`, which emits the reversed direction.

After this normalization, every row of `F` means “the user in the first column has the user in the second column as a friend.”

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friends": [{"user1": 2, "user2": 1}, {"user1": 1, "user2": 3}, {"user1": 4, "user2": 1}, {"user1": 1, "user2": 5}, {"user1": 1, "user2": 6}, {"user1": 2, "user2": 6}, {"user1": 7, "user2": 2}, {"user1": 8, "user2": 3}, {"user1": 3, "user2": 9}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `UNION` is meaningful

The query uses `UNION` rather than `UNION ALL`. `UNION` removes duplicate directed pairs. The table's primary key prevents two identical source rows, but it does not necessarily forbid both `(a,b)` and `(b,a)` from appearing as separate source rows. Reversing both would otherwise duplicate the same relationship in `F`.

Deduplication ensures each directed friendship is counted once. This aligns the numerator with the number of friends rather than the number of redundant records.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query uses `UNION` rather than `UNION ALL`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count the platform's users from the normalized relation

The second common table expression `T` computes:

`COUNT(DISTINCT user1) AS cnt FROM F`.

Because every participant from the original table appears as the first column in one of the two directions, distinct `F.user1` values are exactly all users represented on the platform by this dataset. A user originally appearing only in `user2` is no longer missed.

The scalar subquery `(SELECT cnt FROM T)` supplies this common denominator to every result row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user1", "percentage_popularity"], "rows": [[1, 55.56], [2, 33.33], [3, 33.33], [4, 11.11], [5, 11.11], [6, 22.22], [7, 11.11], [8, 11.11], [9, 11.11]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friends": [{"user1": 2, "user2": 1}, {"user1": 1, "user2": 3}, {"user1": 4, "user2": 1}, {"user1": 1, "user2": 5}, {"user1": 1, "user2": 6}, {"user1": 2, "user2": 6}, {"user1": 7, "user2": 2}, {"user1": 8, "user2": 3}, {"user1": 3, "user2": 9}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user1", "percentage_popularity"], "rows": [[1, 55.56], [2, 33.33], [3, 33.33], [4, 11.11], [5, 11.11], [6, 22.22], [7, 11.11], [8, 11.11], [9, 11.11]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`UNION ALL` plus `COUNT(DISTINCT user2)`:** Al:** - **`UNION ALL` plus `COUNT(DISTINCT user2)`:** Also handles duplicate directions, but the total-user computation and numerator must both preserve distinct semantics explicitly.
- **Group by normalized user:** `GROUP BY user1` with a friend count can replace the window plus outer `DISTINCT` and may express the one-row-per-user intent more directly.
- **Count only original `user1` values:** Incorrect because users appearing solely in `user2` would disappear from both results and denominator.
- **Treat friendships as directed:** Incorrect for the stated mutual relationship; both endpoints must receive credit.
- **Both orientations stored:** `UNION` prevents `(a,b)` and `(b,a)` source rows from doubling the normalized friendship.
- **Single friendship:** Two users each have one friend, so each popularity is $50.00$ percent because the denominator includes both users.
- **Isolated users:** They cannot appear because the input has no user roster beyond `Friends`.
- **Rounding:** `ROUND(..., 2)` is necessary; returning the unrounded repeating decimal would violate the contract.
- **Output order:** `ORDER BY 1` means ascending `user1` because it is the first selected column.
- **Window duplication:** `SELECT DISTINCT` is essential in this exact formulation because the window count is repeated once per friendship row.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of input friendship rows and $U$ the number of represented users. Expanding creates at most $2R$ candidate rows. A typical MySQL execution of `UNION` performs duplicate elimination using sorting or hashing. The window partitioning, `DISTINCT`, and final ordering also require grouping, sorting, or hash structures.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Total Traveled Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 17, "name": "Addison"}, {"user_id": 14, "name": "Ethan"}, {"user_id": 4, "name": "Michael"}, {"user_id": 2, "name": "Avery"}, {"user_id": 10, "name": "Eleanor"}], "Rides": [{"ride_id": 72, "user_id": 17, "distance": 160}, {"ride_id": 42, "user_id": 14, "distance": 161}, {"ride_id": 45, "user_id": 4, "distance": 59}, {"ride_id": 32, "user_id": 2, "distance": 197}, {"ride_id": 15, "user_id": 4, "distance": 357}, {"ride_id": 56, "user_id": 2, "distance": 196}, {"ride_id": 10, "user_id": 14, "distance": 25}]}}`
- **Required output:** `{"columns": ["user_id", "name", "traveled distance"], "rows": [[2, "Avery", 393], [4, "Michael", 416], [10, "Eleanor", 0], [14, "Ethan", 186], [17, "Addison", 160]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id", "name", "traveled distance"], "rows": [[2, "Avery", 393], [4, "Michael", 416], [10, "Eleanor", 0], [14, "Ethan", 186], [17, "Addison", 160]]}` from `{"tables": {"Users": [{"user_id": 17, "name": "Addison"}, {"user_id": 14, "name": "Ethan"}, {"user_id": 4, "name": "Michael"}, {"user_id": 2, "name": "Avery"}, {"user_id": 10, "name": "Eleanor"}], "Rides": [{"ride_id": 72, "user_id": 17, "distance": 160}, {"ride_id": 42, "user_id": 14, "distance": 161}, {"ride_id": 45, "user_id": 4, "distance": 59}, {"ride_id": 32, "user_id": 2, "distance": 197}, {"ride_id": 15, "user_id": 4, "distance": 357}, {"ride_id": 56, "user_id": 2, "distance": 196}, {"ride_id": 10, "user_id": 14, "distance": 25}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Begin from every user, not every ride.** The result must include users who have never completed a ride. Therefore, `Users` must be the preserved side of the join. The query writes

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 17, "name": "Addison"}, {"user_id": 14, "name": "Ethan"}, {"user_id": 4, "name": "Michael"}, {"user_id": 2, "name": "Avery"}, {"user_id": 10, "name": "Eleanor"}], "Rides": [{"ride_id": 72, "user_id": 17, "distance": 160}, {"ride_id": 42, "user_id": 14, "distance": 161}, {"ride_id": 45, "user_id": 4, "distance": 59}, {"ride_id": 32, "user_id": 2, "distance": 197}, {"ride_id": 15, "user_id": 4, "distance": 357}, {"ride_id": 56, "user_id": 2, "distance": 196}, {"ride_id": 10, "user_id": 14, "distance": 25}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

A left join emits every row from `Users`. When matching ride rows exist, it emits one joined row per ride. When none exist, it still emits one user row whose ride columns, including `distance`, are null.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

An inner join would lose users without rides and could never later recover their required zero totals.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "name", "traveled distance"], "rows": [[2, "Avery", 393], [4, "Michael", 416], [10, "Eleanor", 0], [14, "Ethan", 186], [17, "Addison", 160]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 17, "name": "Addison"}, {"user_id": 14, "name": "Ethan"}, {"user_id": 4, "name": "Michael"}, {"user_id": 2, "name": "Avery"}, {"user_id": 10, "name": "Eleanor"}], "Rides": [{"ride_id": 72, "user_id": 17, "distance": 160}, {"ride_id": 42, "user_id": 14, "distance": 161}, {"ride_id": 45, "user_id": 4, "distance": 59}, {"ride_id": 32, "user_id": 2, "distance": 197}, {"ride_id": 15, "user_id": 4, "distance": 357}, {"ride_id": 56, "user_id": 2, "distance": 196}, {"ride_id": 10, "user_id": 14, "distance": 25}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "name", "traveled distance"], "rows": [[2, "Avery", 393], [4, "Michael", 416], [10, "Eleanor", 0], [14, "Ethan", 186], [17, "Addison", 160]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Pre-aggregate rides before joining:** Group `Rides` by user first, then left-join the smaller totals table to `Users`. This can reduce join volume when users have many rides and still requires null replacement.
- **Correlated scalar subquery:** Compute one sum for each user. It is concise but may be slower without optimizer decorrelation or an index.
- **Inner join:** It is incorrect because users without rides disappear.
- **No rides for a user:** `SUM` is null over the null-extended group, and `COALESCE` changes it to zero.
- **One ride:** Its distance passes through as the total.
- **Many rides:** Every matching row contributes once to `SUM`.
- **Zero distance:** If allowed, it is a real numeric input and remains zero; it is distinct from null, though both display zero after aggregation.
- **Grouping by ordinal:** `GROUP BY 1` means `user_id` here, but explicit column names are often clearer and safer during query maintenance.
- **Functional dependency of name:** The unique user ID determines one name. Explicitly grouping both columns improves portability.
- **Alias with spaces:** MySQL accepts the quoted alias; other SQL dialects may prefer double quotes.
- **Required ordering:** Without `ORDER BY`, relational result order is unspecified even if an execution plan happens to emit sorted rows.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((U + R) log (U + R))$. Let $U$ be the number of user rows and $R$ the number of ride rows. Physical complexity depends on indexes and the MySQL execution plan.
- **Auxiliary Space Complexity:** $O(U + R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

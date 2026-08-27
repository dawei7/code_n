# Guided Example: Second Degree Follower

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Follow": [{"followee": "Alice", "follower": "Bob"}, {"followee": "Bob", "follower": "Cena"}, {"followee": "Bob", "follower": "Donald"}, {"followee": "Donald", "follower": "Edward"}]}}`
- **Required output:** `{"columns": ["follower", "num"], "rows": [["Bob", 2], ["Donald", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Follow`

The objective is to compute `{"columns": ["follower", "num"], "rows": [["Bob", 2], ["Donald", 1]]}` from `{"tables": {"Follow": [{"followee": "Alice", "follower": "Bob"}, {"followee": "Bob", "follower": "Cena"}, {"followee": "Bob", "follower": "Donald"}, {"followee": "Donald", "follower": "Edward"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Read each relationship in the correct direction.** A row `(followee, follower)` means that the user in `follower` follows the user in `followee`. A second-degree user must play both roles somewhere in the table: the user follows at least one other person, and at least one person follows that user. The query finds such users by joining two copies of `Follow`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Follow": [{"followee": "Alice", "follower": "Bob"}, {"followee": "Bob", "follower": "Cena"}, {"followee": "Bob", "follower": "Donald"}, {"followee": "Donald", "follower": "Edward"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Call the two aliases `f1` and `f2`. In an `f1` row, `f1.follower` is a person who follows somebody. In an `f2` row, `f2.followee` is a person who is followed by somebody. The condition

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Call the two aliases `f1` and `f2`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

therefore matches exactly when the same user satisfies both halves of the definition. The shared value is the second-degree user.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["follower", "num"], "rows": [["Bob", 2], ["Donald", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Follow": [{"followee": "Alice", "follower": "Bob"}, {"followee": "Bob", "follower": "Cena"}, {"followee": "Bob", "follower": "Donald"}, {"followee": "Donald", "follower": "Edward"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["follower", "num"], "rows": [["Bob", 2], ["Donald", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count incoming relationships, then filter with:** - **Count incoming relationships, then filter with `EXISTS`:** Group rows by `followee` to count each user's followers, and retain a group only when an `EXISTS` subquery finds that user in the `follower` column. This directly separates counting from eligibility and avoids multiplying incoming and outgoing degrees.
- **Intersection of role sets:** Build the set of users appearing as `follower`, intersect it with users appearing as `followee`, and join that set to incoming counts. This mirrors the definition very clearly but may require more CTEs.
- **`COUNT(*)` instead of `COUNT(DISTINCT ...)`:** It is unsafe with the current two-way join because every outgoing relationship repeats all incoming relationships. It becomes safe only after the eligibility check is restructured so each incoming row appears once.
- **User follows many accounts:** The distinct count prevents those outgoing rows from inflating the number of people who follow the user.
- **User is followed by many accounts:** Every distinct incoming follower is preserved and counted exactly once.
- **User only follows others:** Such a user has no matching `f2.followee` row and is excluded.
- **User is only followed by others:** Such a user has no matching `f1.follower` row and is excluded.
- **Self-follow relationships:** The schema promises that none exist. If they did, one self-edge alone would satisfy both roles, which may or may not match the intended social definition.
- **Duplicate relationships:** The composite primary key excludes them. `DISTINCT` nevertheless protects the count from duplicates created by the join's multiple outgoing matches.
- **Alias naming:** The CTE column named `followee` actually stores a direct follower. Reading it by its source expression, `f2.follower`, prevents a direction mistake during review.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `Follow`. The two aliases each refer to the same $R$-row relation. With an index, hash table, or sort on the join key, finding matching users is commonly bounded by $O(R\log R)$ for a sort-based plan or expected $O(R)$ for a hash-based plan. Grouping, distinct counting, and the final ordering can each require sorting or hashing. The manifest therefore gives the conservative time bound $O(R\log R)$ and auxiliary space bound $O(R)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

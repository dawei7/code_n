# Guided Example: Friend Requests II: Who Has the Most Friends

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016-06-03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016-06-09"}]}}`
- **Required output:** `{"columns": ["id", "num"], "rows": [[3, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `RequestAccepted`

The objective is to compute `{"columns": ["id", "num"], "rows": [[3, 3]]}` from `{"tables": {"RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016-06-03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016-06-09"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Symmetrizing each friendship

The common table expression `T` contains:



For original friendship $(u,v)$, the first branch emits row $(u,v)$ and the second emits $(v,u)$. In both branches, the first column now means “the person whose friend count receives one.” The second column records the friend but is not needed for the final count.

For sample row $(1,2)$, user 1 gains one occurrence from the first branch and user 2 gains one from the swapped branch. Repeating this for every accepted request makes each person appear once per incident friendship.

`UNION ALL` is essential. Plain `UNION` removes duplicate rows across branches. Although the composite primary key prevents duplicate directed acceptance pairs, distinct friendships involving the same person must all remain as separate occurrences for counting. Deduplication is not part of this transformation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016-06-03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016-06-09"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grouping endpoint occurrences

The outer query groups by the first column:



Ordinal 1 refers to `requester_id AS id`. `COUNT(1)` counts endpoint rows in each person’s group, which equals that person’s number of friends under the one-row-per-friendship schema.

In the sample:

- user 1 appears for friendships with 2 and 3, count two;
- user 2 appears for friendships with 1 and 3, count two;
- user 3 appears for friendships with 1, 2, and 4, count three;
- user 4 appears once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer query groups by the first column:



Ordinal 1 ref... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selecting the unique maximum

`ORDER BY 2 DESC` refers to the second selected expression, `COUNT(1) AS num`. It ranks people from most friends to fewest. `LIMIT 1` keeps the first group.

The contract guarantees exactly one person has the maximum friend count, so no tie-breaking key is required. The follow-up removes that guarantee and would need a rank or comparison against the maximum rather than arbitrary top-one selection.

The final aliases `id` and `num` provide the requested schema.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "num"], "rows": [[3, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016-06-03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016-06-08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016-06-09"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "num"], "rows": [[3, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Aggregate each role separately, then combine c:** - **Aggregate each role separately, then combine counts:** Count requester and accepter occurrences per ID and outer-join/sum the two results. Correct but more complicated than symmetric expansion.
- **Use `UNION` instead of `UNION ALL`:** Risks discarding occurrences and undercounting; every friendship endpoint contribution must remain.
- **Window `RANK`:** Group counts, rank descending, and keep rank one. This naturally returns all tied leaders for the follow-up.
- **Maximum-count subquery:** Compare each grouped count with the maximum grouped count to return every leader.
- **Count only requester IDs:** Misses friendships where a person was the accepter.
- **Count only accepter IDs:** Has the symmetric omission.
- **Unique maximum:** Justifies `LIMIT 1` without a secondary ordering rule.
- **Tie in generalized data:** Exact query returns only one arbitrary leader; use `RANK` for all.
- **One friendship:** Both endpoints have count one, creating a tie and therefore contradicting the unique-winner test guarantee.
- **Accept date:** Irrelevant to total friend degree and deliberately omitted.
- **Composite primary key:** Prevents duplicate directed friendship rows, so each accepted pair contributes once.
- **Self-friend row:** Would be emitted twice for one ID; intended friendship data should exclude it or define special handling.
- **Ordinal references:** `GROUP BY 1` and `ORDER BY 2` are concise but explicit aliases are easier to maintain.
- **Empty table:** No groups exist and no row is returned; intended tests supply a unique maximum.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $n$ be the number of accepted-request rows and $u$ the number of distinct people. The CTE produces $2n$ rows, which is still $O(n)$. Hash grouping takes expected $O(n)$ time and $O(u)$ group state.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Friend Requests I: Overall Acceptance Rate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"FriendRequest": [{"sender_id": 1, "send_to_id": 2, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 3, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 4, "request_date": "2016/06/01"}, {"sender_id": 2, "send_to_id": 3, "request_date": "2016/06/02"}, {"sender_id": 3, "send_to_id": 4, "request_date": "2016/06/09"}], "RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016/06/03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/09"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/10"}]}}`
- **Required output:** `{"columns": ["accept_rate"], "rows": [[0.8]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `FriendRequest`

The objective is to compute `{"columns": ["accept_rate"], "rows": [[0.8]]}` from `{"tables": {"FriendRequest": [{"sender_id": 1, "send_to_id": 2, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 3, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 4, "request_date": "2016/06/01"}, {"sender_id": 2, "send_to_id": 3, "request_date": "2016/06/02"}, {"sender_id": 3, "send_to_id": 4, "request_date": "2016/06/09"}], "RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016/06/03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/09"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/10"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting distinct pairs rather than distinct columns

MySQL supports multi-expression distinct counting:



This counts distinct *combinations*. Pairs `(1,2)` and `(1,3)` are different even though they share the first component. Counting distinct requester IDs and distinct accepter IDs separately would lose pair relationships and could not reconstruct the correct number.

The acceptance date is intentionally absent. If pair `(3,4)` appears with two accept dates, both event rows collapse to one logical accepted request. The denominator similarly ignores `request_date` and collapses repeated `(sender_id, send_to_id)` pairs.

Direction matters. Pair `(1,2)` is different from `(2,1)` because sender/requester and receiver/accepter roles are ordered columns. The query preserves that order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"FriendRequest": [{"sender_id": 1, "send_to_id": 2, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 3, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 4, "request_date": "2016/06/01"}, {"sender_id": 2, "send_to_id": 3, "request_date": "2016/06/02"}, {"sender_id": 3, "send_to_id": 4, "request_date": "2016/06/09"}], "RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016/06/03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/09"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/10"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why numerator and denominator are independent

The numerator subquery reads only `RequestAccepted`, while the denominator reads only `FriendRequest`. There is no join requiring an accepted pair to appear among recorded requests.

That separation implements the note that accepted requests count even when absent from `FriendRequest`. It also means the numeric rate can exceed one if the accepted table contains more distinct pairs than the request table. Although unusual in a real workflow, this is consistent with the explicit contract; the query must not cap the value at 1.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The numerator subquery reads only `RequestAccepted`, while t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Division and the empty-request case

The two scalar subqueries each return one integer. MySQL’s division produces a fractional numeric result when the denominator is positive.

If there are no distinct request pairs, the denominator is zero. Division by zero yields `NULL` in this context. The surrounding:



replaces that missing ratio with zero. `COALESCE` returns its first non-`NULL` argument, so ordinary nonempty ratios pass through unchanged.

If there are requests but no accepted pairs, the numerator is zero and the calculation is the genuine numeric value zero; `COALESCE` still leaves it as zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["accept_rate"], "rows": [[0.8]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"FriendRequest": [{"sender_id": 1, "send_to_id": 2, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 3, "request_date": "2016/06/01"}, {"sender_id": 1, "send_to_id": 4, "request_date": "2016/06/01"}, {"sender_id": 2, "send_to_id": 3, "request_date": "2016/06/02"}, {"sender_id": 3, "send_to_id": 4, "request_date": "2016/06/09"}], "RequestAccepted": [{"requester_id": 1, "accepter_id": 2, "accept_date": "2016/06/03"}, {"requester_id": 1, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 2, "accepter_id": 3, "accept_date": "2016/06/08"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/09"}, {"requester_id": 3, "accepter_id": 4, "accept_date": "2016/06/10"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["accept_rate"], "rows": [[0.8]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Distinct subqueries then `COUNT(*)`:** Select :** - **Distinct subqueries then `COUNT(*)`:** Select distinct pairs in derived tables and count their rows. More verbose but portable to systems without multi-column `COUNT(DISTINCT ...)` syntax.
- **Concatenating IDs:** Avoid `COUNT(DISTINCT CONCAT(...))` because ambiguous formatting can merge different pairs unless carefully encoded.
- **Joining acceptances to requests:** Incorrect under this contract because accepted pairs not present in `FriendRequest` must still count.
- **Counting raw rows:** Incorrect because repeated request or acceptance events count only once per pair.
- **Counting dates:** Dates do not distinguish the logical directed pairs and must be ignored.
- **No requests:** Denominator zero produces `NULL` on division; `COALESCE` returns zero.
- **No acceptances but some requests:** Numerator zero gives rate zero normally.
- **Accepted pair absent from requests:** It still contributes to the numerator.
- **Rate above one:** Possible under the independent-table rule and must not be clamped.
- **Reverse-direction pairs:** `(1,2)` and `(2,1)` are distinct.
- **Rounding order:** Divide exact counts first, then round the ratio once.
- **Potential null IDs:** MySQL’s multi-column distinct count ignores combinations containing `NULL`. The intended event model uses user IDs; if nullable IDs were valid data, their counting policy would need explicit handling.
- **One-row guarantee:** Scalar subqueries let the outer query return an `accept_rate` row even for empty inputs.
- **Monthly/daily follow-ups:** They require grouping by time periods and possibly running aggregates; this whole-table scalar query intentionally answers only the overall rate.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A+R)$. Let $A$ and $R$ be the row counts of `RequestAccepted` and `FriendRequest`. Computing distinct pairs can use hashing in expected $O(A+R)$ time and $O(A+R)$ worst-case space for stored unique pairs.
- **Auxiliary Space Complexity:** $O(R+A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

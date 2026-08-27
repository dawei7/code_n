# Guided Example: Find Longest Calls

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Contacts": [{"id": 1, "first_name": "John", "last_name": "Doe"}, {"id": 2, "first_name": "Jane", "last_name": "Smith"}, {"id": 3, "first_name": "Alice", "last_name": "Johnson"}, {"id": 4, "first_name": "Michael", "last_name": "Brown"}, {"id": 5, "first_name": "Emily", "last_name": "Davis"}], "Calls": [{"contact_id": 1, "type": "incoming", "duration": 120}, {"contact_id": 1, "type": "outgoing", "duration": 180}, {"contact_id": 2, "type": "incoming", "duration": 300}, {"contact_id": 2, "type": "outgoing", "duration": 240}, {"contact_id": 3, "type": "incoming", "duration": 150}, {"contact_id": 3, "type": "outgoing", "duration": 360}, {"contact_id": 4, "type": "incoming", "duration": 420}, {"contact_id": 4, "type": "outgoing", "duration": 200}, {"contact_id": 5, "type": "incoming", "duration": 180}, {"contact_id": 5, "type": "outgoing", "duration": 280}]}}`
- **Required output:** `{"columns": ["first_name", "type", "duration_formatted"], "rows": [["Alice", "outgoing", "00:06:00"], ["Emily", "outgoing", "00:04:40"], ["Jane", "outgoing", "00:04:00"], ["Michael", "incoming", "00:07:00"], ["Jane", "incoming", "00:05:00"], ["Emily", "incoming", "00:03:00"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Contacts`

The objective is to compute `{"columns": ["first_name", "type", "duration_formatted"], "rows": [["Alice", "outgoing", "00:06:00"], ["Emily", "outgoing", "00:04:40"], ["Jane", "outgoing", "00:04:00"], ["Michael", "incoming", "00:07:00"], ["Jane", "incoming", "00:05:00"], ["Emily", "incoming", "00:03:00"]]}` from `{"tables": {"Contacts": [{"id": 1, "first_name": "John", "last_name": "Doe"}, {"id": 2, "first_name": "Jane", "last_name": "Smith"}, {"id": 3, "first_name": "Alice", "last_name": "Johnson"}, {"id": 4, "first_name": "Michael", "last_name": "Brown"}, {"id": 5, "first_name": "Emily", "last_name": "Davis"}], "Calls": [{"contact_id": 1, "type": "incoming", "duration": 120}, {"contact_id": 1, "type": "outgoing", "duration": 180}, {"contact_id": 2, "type": "incoming", "duration": 300}, {"contact_id": 2, "type": "outgoing", "duration": 240}, {"contact_id": 3, "type": "incoming", "duration": 150}, {"contact_id": 3, "type": "outgoing", "duration": 360}, {"contact_id": 4, "type": "incoming", "duration": 420}, {"contact_id": 4, "type": "outgoing", "duration": 200}, {"contact_id": 5, "type": "incoming", "duration": 180}, {"contact_id": 5, "type": "outgoing", "duration": 280}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The query first enriches each call with a contact name.** `Calls` contains `contact_id`, call direction, and duration, while the required output needs `first_name`. The CTE joins `Calls AS c1` to `Contacts AS c2` on `c1.contact_id = c2.id`. Each call row can then be ranked and displayed with its contact.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Contacts": [{"id": 1, "first_name": "John", "last_name": "Doe"}, {"id": 2, "first_name": "Jane", "last_name": "Smith"}, {"id": 3, "first_name": "Alice", "last_name": "Johnson"}, {"id": 4, "first_name": "Michael", "last_name": "Brown"}, {"id": 5, "first_name": "Emily", "last_name": "Davis"}], "Calls": [{"contact_id": 1, "type": "incoming", "duration": 120}, {"contact_id": 1, "type": "outgoing", "duration": 180}, {"contact_id": 2, "type": "incoming", "duration": 300}, {"contact_id": 2, "type": "outgoing", "duration": 240}, {"contact_id": 3, "type": "incoming", "duration": 150}, {"contact_id": 3, "type": "outgoing", "duration": 360}, {"contact_id": 4, "type": "incoming", "duration": 420}, {"contact_id": 4, "type": "outgoing", "duration": 200}, {"contact_id": 5, "type": "incoming", "duration": 180}, {"contact_id": 5, "type": "outgoing", "duration": 280}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Rank incoming and outgoing calls independently.** The window expression:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Rank incoming and outgoing calls independently.** The wind... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`RANK() OVER (PARTITION BY type ORDER BY duration DESC)`

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["first_name", "type", "duration_formatted"], "rows": [["Alice", "outgoing", "00:06:00"], ["Emily", "outgoing", "00:04:40"], ["Jane", "outgoing", "00:04:00"], ["Michael", "incoming", "00:07:00"], ["Jane", "incoming", "00:05:00"], ["Emily", "incoming", "00:03:00"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Contacts": [{"id": 1, "first_name": "John", "last_name": "Doe"}, {"id": 2, "first_name": "Jane", "last_name": "Smith"}, {"id": 3, "first_name": "Alice", "last_name": "Johnson"}, {"id": 4, "first_name": "Michael", "last_name": "Brown"}, {"id": 5, "first_name": "Emily", "last_name": "Davis"}], "Calls": [{"contact_id": 1, "type": "incoming", "duration": 120}, {"contact_id": 1, "type": "outgoing", "duration": 180}, {"contact_id": 2, "type": "incoming", "duration": 300}, {"contact_id": 2, "type": "outgoing", "duration": 240}, {"contact_id": 3, "type": "incoming", "duration": 150}, {"contact_id": 3, "type": "outgoing", "duration": 360}, {"contact_id": 4, "type": "incoming", "duration": 420}, {"contact_id": 4, "type": "outgoing", "duration": 200}, {"contact_id": 5, "type": "incoming", "duration": 180}, {"contact_id": 5, "type": "outgoing", "duration": 280}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["first_name", "type", "duration_formatted"], "rows": [["Alice", "outgoing", "00:06:00"], ["Emily", "outgoing", "00:04:40"], ["Jane", "outgoing", "00:04:00"], ["Michael", "incoming", "00:07:00"], ["Jane", "incoming", "00:05:00"], ["Emily", "incoming", "00:03:00"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`ROW_NUMBER` with full ordering:** Enforces ex:** - **`ROW_NUMBER` with full ordering:** Enforces exactly three rows per type and resolves duration ties deterministically.
- **Correlated top-three subqueries:** Possible but usually less clear and potentially less efficient than a window function.
- **Fewer than three calls of a type:** Every available row should be returned.
- **Equal durations:** Exact `RANK` may return more than three rows, a correctness defect for a strict row count.
- **Tie at rank three:** Every tied row survives, again exceeding three.
- **Type ordering:** Source uses ascending but the contract requires descending.
- **Duration ordering:** Ranking uses the original integer, which is correct.
- **Formatted ordering:** Fixed-width `HH:MM:SS` strings preserve order only within the formatter's supported hour representation.
- **Same first name:** Final ordering may still tie because no unique final key is supplied.
- **Contact join:** An inner join assumes every call's contact ID has a matching contact, as implied by the relationship.
- **Incoming and outgoing partitions:** Each receives an independent rank sequence.
- **Duration zero:** Formats as `00:00:00` and can still rank if few calls exist.
- **Projection:** Numeric duration and rank are intentionally hidden from the result.
- **Primary key:** It does not prevent different contacts from sharing a duration.
- **Source defects:** Use of `RANK` and ascending `type` prevent a general correctness guarantee.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c log c)$. Let $c$ be the number of calls. Joining contacts is expected $O(c)$ with an index on `Contacts.id`. The window operation must order calls within type by duration, generally costing $O(c\log c)$. The final selected result is small under intended top-three semantics, though the `RANK` defect can enlarge it under ties.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Find Invalid IP Addresses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"logs": [{"log_id": 1, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 2, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 3, "ip": "192.168.001.1", "status_code": 200}, {"log_id": 4, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 5, "ip": "192.168.1", "status_code": 500}, {"log_id": 6, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 7, "ip": "192.168.001.1", "status_code": 200}]}}`
- **Required output:** `{"columns": ["ip", "invalid_count"], "rows": [["256.1.2.3", 2], ["192.168.001.1", 2], ["192.168.1", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: ` logs`

The objective is to compute `{"columns": ["ip", "invalid_count"], "rows": [["256.1.2.3", 2], ["192.168.001.1", 2], ["192.168.1", 1]]}` from `{"tables": {"logs": [{"log_id": 1, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 2, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 3, "ip": "192.168.001.1", "status_code": 200}, {"log_id": 4, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 5, "ip": "192.168.1", "status_code": 500}, {"log_id": 6, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 7, "ip": "192.168.001.1", "status_code": 200}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Filter rows that satisfy any listed invalidity condition.** The SQL treats an address as invalid when it has the wrong number of dot separators, a leading zero in one of four extracted octets, or an octet numerically greater than $255$. The `WHERE` clauses are connected by `OR`, so one failing property is sufficient.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"logs": [{"log_id": 1, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 2, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 3, "ip": "192.168.001.1", "status_code": 200}, {"log_id": 4, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 5, "ip": "192.168.1", "status_code": 500}, {"log_id": 6, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 7, "ip": "192.168.001.1", "status_code": 200}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Count dots to test the octet count.** Replacing every dot with an empty string shortens the address by exactly the number of dots:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Count dots to test the octet count.** Replacing every dot ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`LENGTH(ip) - LENGTH(REPLACE(ip, '.', ''))`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["ip", "invalid_count"], "rows": [["256.1.2.3", 2], ["192.168.001.1", 2], ["192.168.1", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"logs": [{"log_id": 1, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 2, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 3, "ip": "192.168.001.1", "status_code": 200}, {"log_id": 4, "ip": "192.168.1.1", "status_code": 200}, {"log_id": 5, "ip": "192.168.1", "status_code": 500}, {"log_id": 6, "ip": "256.1.2.3", "status_code": 404}, {"log_id": 7, "ip": "192.168.001.1", "status_code": 200}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["ip", "invalid_count"], "rows": [["256.1.2.3", 2], ["192.168.001.1", 2], ["192.168.1", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Parsing CTE:** Extract four octets once, then :** - **Parsing CTE:** Extract four octets once, then reference named columns for all tests. This is clearer and avoids repeated expressions, but the protected query does not do it.
- **Full anchored IPv4 regex:** It can enforce digit syntax, count, leading-zero, and range rules, but the range portion becomes difficult to read.
- **Only count dots:** Three dots do not by themselves guarantee valid numeric octets.
- **Octet equal to 255:** The condition is strictly greater than $255$, so $255$ remains allowed.
- **Single zero octet:** `"0"` does not match the two-character leading-zero pattern and is valid.
- **Multiple invalid reasons:** OR filtering selects the row once; `COUNT(*)` counts log rows, not reasons.
- **Repeated address:** Grouping produces one result row with its occurrence count.
- **Status code:** It is irrelevant to IP validity and is intentionally unused.
- **Descending tie-break:** Equal counts are ordered by IP text descending, not numerically by octets.
- **Malformed nonnumeric text:** The exact source lacks a digits-only predicate, so it should not be described as a stricter validator than it is.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+q)$. Let $S$ be the total character volume of scanned IP strings and $q$ the number of distinct invalid IP values. String replacement, extraction, and short regex checks require work proportional to input text, summarized as $O(S)$. Grouping uses hash or sort work depending on the plan, and final ordering costs up to $O(q\log q)$.
- **Auxiliary Space Complexity:** $O(S + k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

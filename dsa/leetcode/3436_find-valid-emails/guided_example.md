# Guided Example: Find Valid Emails

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 1, "email": "alice@example.com"}, {"user_id": 2, "email": "bob_at_example.com"}, {"user_id": 3, "email": "charlie@example.net"}, {"user_id": 4, "email": "david@domain.com"}, {"user_id": 5, "email": "eve@invalid"}]}}`
- **Required output:** `{"columns": ["user_id", "email"], "rows": [[1, "alice@example.com"], [4, "david@domain.com"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id", "email"], "rows": [[1, "alice@example.com"], [4, "david@domain.com"]]}` from `{"tables": {"Users": [{"user_id": 1, "email": "alice@example.com"}, {"user_id": 2, "email": "bob_at_example.com"}, {"user_id": 3, "email": "charlie@example.net"}, {"user_id": 4, "email": "david@domain.com"}, {"user_id": 5, "email": "eve@invalid"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Validate the entire email with one anchored pattern.** The query selects `user_id` and `email` only when `email REGEXP ...` succeeds:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 1, "email": "alice@example.com"}, {"user_id": 2, "email": "bob_at_example.com"}, {"user_id": 3, "email": "charlie@example.net"}, {"user_id": 4, "email": "david@domain.com"}, {"user_id": 5, "email": "eve@invalid"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\.com$`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\.com$`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The anchors `^` and `$` require the match to cover the complete email string. Without them, a malformed address could contain a valid-looking substring and still pass.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "email"], "rows": [[1, "alice@example.com"], [4, "david@domain.com"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 1, "email": "alice@example.com"}, {"user_id": 2, "email": "bob_at_example.com"}, {"user_id": 3, "email": "charlie@example.net"}, {"user_id": 4, "email": "david@domain.com"}, {"user_id": 5, "email": "eve@invalid"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "email"], "rows": [[1, "alice@example.com"], [4, "david@domain.com"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Unanchored regex:** It could accept a valid fr:** - **Unanchored regex:** It could accept a valid fragment inside an otherwise invalid email. Both `^` and `$` are essential.
- **Unescaped dot:** Regex `.` matches any character, so `exampleXcom` could pass. The suffix dot must be literal.
- **Empty local part:** The `+` quantifier rejects `@domain.com`.
- **Empty domain:** The mandatory first letter rejects `user@.com`.
- **Multiple at signs:** Character classes on both sides exclude `@`, so exactly one literal separator is possible.
- **Local underscore:** It is explicitly allowed before `@`.
- **Domain underscore:** It is not in either domain class and is rejected.
- **Domain beginning with a digit:** The first-domain-letter class rejects it even though later digits are accepted.
- **Digits later in domain:** The exact query accepts them; this differs from the reference's “only letters” wording and should not be hidden.
- **Ordering syntax:** `ORDER BY user_id ASC` would be clearer than positional `ORDER BY 1` but is equivalent here.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $S$ be the total number of characters across scanned email strings and $r$ the number of matching rows. A fixed anchored regular expression can be tested in $O(S)$ total scanning time. Ordering qualifying rows may require $O(r\log r)$ time and $O(r)$ sort space. The overall direct-plan bound is $O(S+r\log r)$ time and $O(r)$ auxiliary space.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Bitwise User Permissions Analysis

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"user_permissions": [{"user_id": 1, "permissions": 5}, {"user_id": 2, "permissions": 12}, {"user_id": 3, "permissions": 7}, {"user_id": 4, "permissions": 3}]}}`
- **Required output:** `{"columns": ["common_perms", "any_perms"], "rows": [[0, 15]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{user}_{permissions}$

The objective is to compute `{"columns": ["common_perms", "any_perms"], "rows": [[0, 15]]}` from `{"tables": {"user_permissions": [{"user_id": 1, "permissions": 5}, {"user_id": 2, "permissions": 12}, {"user_id": 3, "permissions": 7}, {"user_id": 4, "permissions": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Treat each bit as an independent permission.** An integer permission mask is a compact set. If bit $b$ is one, the user has permission $b$; if it is zero, the user lacks it. The query asks for two reductions over every row:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"user_permissions": [{"user_id": 1, "permissions": 5}, {"user_id": 2, "permissions": 12}, {"user_id": 3, "permissions": 7}, {"user_id": 4, "permissions": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `common_perms` should contain bit $b$ only when every user's mask contains that bit;
- `any_perms` should contain bit $b$ when at least one user's mask contains that bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Bitwise AND and OR implement these definitions position by position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["common_perms", "any_perms"], "rows": [[0, 15]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"user_permissions": [{"user_id": 1, "permissions": 5}, {"user_id": 2, "permissions": 12}, {"user_id": 3, "permissions": 7}, {"user_id": 4, "permissions": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["common_perms", "any_perms"], "rows": [[0, 15]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Application-side fold:** Fetch masks and reduce them with language-level AND and OR. It computes the same values but transfers all rows and moves simple aggregation out of the database.
- **Recursive SQL fold:** A dialect without `BIT_AND` or `BIT_OR` aggregates can number rows and combine masks recursively. It is longer and dialect-specific but preserves the linear reduction.
- **Per-bit conditional aggregation:** Test each known permission bit with Boolean counts. This becomes verbose, requires a predetermined bit width, and reconstructs operations the native aggregates already provide.
- **Use `MIN` and `MAX`:** Incorrect because numeric order is not set intersection or union.
- **One user:** Both aggregates equal that user's mask; a singleton set's intersection and union are identical.
- **All users identical:** Both outputs equal their shared mask.
- **No common permission:** AND becomes zero even if every user has several different permissions.
- **Every possible permission appears somewhere:** OR sets every corresponding bit, even if no one user has them all.
- **Permission mask zero:** One zero row forces `common_perms` to zero; it contributes no set bits to `any_perms`.
- **Duplicate masks:** They do not change either result because AND and OR are idempotent.
- **Row order:** Associativity and commutativity make physical scan order irrelevant.
- **Null permissions:** SQL bitwise aggregates may ignore nulls or have dialect-specific behavior. The intended schema treats the permission mask as a supplied value; nullable extensions need an explicit policy.
- **Empty table:** Ungrouped aggregates still return one row, commonly with null aggregate values because no identity seed is specified by SQL. The exact source adds no fallback.
- **Signed integer representation:** Permission masks are intended as nonnegative encoded sets. Negative masks would expose sign-bit and width semantics tied to the SQL type.
- **Manifest mismatch:** No sorting or row-proportional aggregate table is visible. The exact operation is a one-pass constant-state fold.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of rows and let $w$ be the fixed bit width of the SQL integer type. The engine can update both aggregate masks once per row, doing $O(w)$ bit work per mask. With fixed-width integers, $w$ is constant, so the logical running time is $O(r)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

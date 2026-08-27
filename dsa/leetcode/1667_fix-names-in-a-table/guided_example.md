# Guided Example: Fix Names in a Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 1, "name": "aLice"}, {"user_id": 2, "name": "bOB"}]}}`
- **Required output:** `{"columns": ["user_id", "name"], "rows": [[1, "Alice"], [2, "Bob"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id", "name"], "rows": [[1, "Alice"], [2, "Bob"]]}` from `{"tables": {"Users": [{"user_id": 1, "name": "aLice"}, {"user_id": 2, "name": "bOB"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize the first character separately from the suffix

The desired name has two case rules:

1. its first character must be uppercase;
2. every remaining character must be lowercase.

The SQL expression constructs those two parts independently and concatenates them:

`CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2)))`.

This is more precise than applying `UPPER` or `LOWER` to the entire name, because neither whole-string operation alone satisfies both requirements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 1, "name": "aLice"}, {"user_id": 2, "name": "bOB"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract and uppercase the first character

`LEFT(name, 1)` returns the leftmost one-character substring of `name`. Passing that result to `UPPER` ensures it is uppercase. If it was already uppercase, the value is unchanged; if it was lowercase, it is converted.

The input guarantees names consist only of lowercase and uppercase characters, so there are no digits, spaces, punctuation marks, or multiword separators needing a separate policy. SQL’s actual case conversion follows the column’s character set and collation, but for the promised English-style letter data it implements the requested transformation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `LEFT(name, 1)` returns the leftmost one-character substring... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extract and lowercase everything after it

MySQL substring positions are one-based. `SUBSTRING(name, 2)` therefore starts at the second character and continues through the end because no length argument is supplied. `LOWER` converts every character of this suffix to lowercase.

For `name = 'aLice'`, the first expression produces `'A'` and the second produces `'lice'`. `CONCAT` joins them into `'Alice'`. For `'bOB'`, the parts become `'B'` and `'ob'`, producing `'Bob'`.

The alias `AS name` is significant. It gives the computed expression the same output column name required by the result schema, rather than exposing a database-generated expression label.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "name"], "rows": [[1, "Alice"], [2, "Bob"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 1, "name": "aLice"}, {"user_id": 2, "name": "bOB"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "name"], "rows": [[1, "Alice"], [2, "Bob"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`SUBSTRING(name, 1, 1)` instead of `LEFT`:** T:** - **`SUBSTRING(name, 1, 1)` instead of `LEFT`:** This extracts the same first character and matches the editorial formulation; the rest of the query is unchanged.
- **Capitalize-style function:** Some environments provide a direct capitalization helper, but MySQL does not offer the same simple standard function used by Pandas, so composing `UPPER`, `LOWER`, and substrings is portable within MySQL.
- **Update the table:** An `UPDATE` statement would mutate source data and would not itself return the required ordered result. The task asks for a query result, so `SELECT` is appropriate.
- **Already normalized name:** Uppercasing the first character and lowercasing the suffix are idempotent, so a value such as `'Alice'` stays `'Alice'`.
- **All-uppercase input:** The first character remains uppercase and every later character becomes lowercase.
- **All-lowercase input:** Only the first character changes to uppercase.
- **Single-character name:** `LEFT(name, 1)` returns that character, while `SUBSTRING(name, 2)` returns the empty string. Concatenation therefore returns the correctly uppercased one-character name.
- **Empty name outside the stated model:** The local schema text does not give a length bound. If empty strings were allowed, both extracted parts would be empty and the output would remain empty, so no first character could be capitalized.
- **`NULL` name outside the stated model:** MySQL string functions and `CONCAT` would propagate `NULL`. The problem describes each row as containing a name and does not ask for null handling.
- **Unique IDs:** The primary key eliminates ordering ties, so no secondary sort key is necessary.
- **Case-sensitive table identifiers:** Using the declaration’s exact `Users` capitalization would be safer across arbitrary MySQL installations, though the exact source uses `users` and is accepted in its target environment.
- **Result storage:** Even when working memory is described as constant, returning `R` rows and their normalized strings necessarily occupies output space proportional to the result size.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of rows and let `C` be the total number of characters across all names. Every name character must be read and case-normalized, so expression evaluation costs $O(C)$ time. If name lengths are treated as bounded, this is often summarized as $O(R)$.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

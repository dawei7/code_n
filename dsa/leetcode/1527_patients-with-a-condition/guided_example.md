# Guided Example: Patients With a Condition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Patients": [{"patient_id": 1, "patient_name": "Daniel", "conditions": "YFEV COUGH"}, {"patient_id": 2, "patient_name": "Alice", "conditions": ""}, {"patient_id": 3, "patient_name": "Bob", "conditions": "DIAB100 MYOP"}, {"patient_id": 4, "patient_name": "George", "conditions": "ACNE DIAB100"}, {"patient_id": 5, "patient_name": "Alain", "conditions": "DIAB201"}]}}`
- **Required output:** `{"columns": ["patient_id", "patient_name", "conditions"], "rows": [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Patients`

The objective is to compute `{"columns": ["patient_id", "patient_name", "conditions"], "rows": [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]]}` from `{"tables": {"Patients": [{"patient_id": 1, "patient_name": "Daniel", "conditions": "YFEV COUGH"}, {"patient_id": 2, "patient_name": "Alice", "conditions": ""}, {"patient_id": 3, "patient_name": "Bob", "conditions": "DIAB100 MYOP"}, {"patient_id": 4, "patient_name": "George", "conditions": "ACNE DIAB100"}, {"patient_id": 5, "patient_name": "Alain", "conditions": "DIAB201"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Condition codes have token boundaries

`conditions` stores zero or more codes separated by spaces. A Type I Diabetes code is any token whose beginning is `DIAB1`. The text must therefore match in one of two places:

- At the beginning of the entire conditions string.
- Immediately after a separating space.

The stored SQL translates those cases directly:

`conditions LIKE 'DIAB1%'`

or

`conditions LIKE '% DIAB1%'`.

The percent sign in `LIKE` matches any sequence of characters, including an empty sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Patients": [{"patient_id": 1, "patient_name": "Daniel", "conditions": "YFEV COUGH"}, {"patient_id": 2, "patient_name": "Alice", "conditions": ""}, {"patient_id": 3, "patient_name": "Bob", "conditions": "DIAB100 MYOP"}, {"patient_id": 4, "patient_name": "George", "conditions": "ACNE DIAB100"}, {"patient_id": 5, "patient_name": "Alain", "conditions": "DIAB201"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understanding the first pattern

`'DIAB1%'` requires the string's first five characters to be `DIAB1`. Anything may follow, so codes such as `DIAB100` qualify. This is correct because the rule specifies a prefix, not a complete code equal to five characters.

It rejects `XDIAB100` because the required prefix is not at the string start.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `'DIAB1%'` requires the string's first five characters to be... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understanding the second pattern

`'% DIAB1%'` finds a literal space followed immediately by `DIAB1` anywhere in the string. The leading wildcard permits earlier condition tokens. The trailing wildcard permits the rest of that code and any later tokens.

For `ACNE DIAB100`, the substring ` DIAB1` exists, so the row qualifies. For `PREDIAB100`, no separating space occurs immediately before `DIAB1`, so it does not match unless the whole string itself begins with the prefix, which it does not.

Multiple spaces before a code still contain some final space directly followed by `DIAB1`, so the second pattern can match.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["patient_id", "patient_name", "conditions"], "rows": [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Patients": [{"patient_id": 1, "patient_name": "Daniel", "conditions": "YFEV COUGH"}, {"patient_id": 2, "patient_name": "Alice", "conditions": ""}, {"patient_id": 3, "patient_name": "Bob", "conditions": "DIAB100 MYOP"}, {"patient_id": 4, "patient_name": "George", "conditions": "ACNE DIAB100"}, {"patient_id": 5, "patient_name": "Alain", "conditions": "DIAB201"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["patient_id", "patient_name", "conditions"], "rows": [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Regular expression boundary:** `(^|[[:space:]]:** - **Regular expression boundary:** `(^|[[:space:]])DIAB1` expresses the two positions in one pattern and can recognize broader whitespace.
- **Tokenized normalized table:** Store one condition code per row linked to a patient. Queries and indexes become cleaner, but the schema changes substantially.
- **BINARY LIKE:** Apply binary comparison when exact uppercase matching must be guaranteed independently of collation.
- **Condition at string start:** The first pattern finds it without requiring a leading space.
- **Condition after another code:** The second pattern finds the space-delimited prefix.
- **DIAB1 inside another token:** It is rejected because there is no valid boundary immediately before it.
- **Code longer than five characters:** It qualifies because `DIAB1` is a prefix.
- **Empty conditions string:** Neither pattern matches.
- **Null conditions:** Both predicates evaluate to unknown, so the row is excluded.
- **Several matching codes:** The patient row is still returned once because filtering does not join or duplicate rows.
- **Unrestricted order:** No `ORDER BY` is needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S + n\log n)$. Let $N$ be the number of patient rows and $S$ the total number of characters in all condition strings. Because both patterns begin with or contain wildcards and inspect text, a typical plan scans rows and examines strings, requiring roughly $O(S)$ matching work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

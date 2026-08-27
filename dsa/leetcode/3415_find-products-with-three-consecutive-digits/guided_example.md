# Guided Example: Find Products with Three Consecutive Digits 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "name": "ABC123XYZ"}, {"product_id": 2, "name": "A12B34C"}, {"product_id": 3, "name": "Product56789"}, {"product_id": 4, "name": "NoDigitsHere"}, {"product_id": 5, "name": "789Product"}, {"product_id": 6, "name": "Item003Description"}, {"product_id": 7, "name": "Product12X34"}]}}`
- **Required output:** `{"columns": ["product_id", "name"], "rows": [[1, "ABC123XYZ"], [5, "789Product"], [6, "Item003Description"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "name"], "rows": [[1, "ABC123XYZ"], [5, "789Product"], [6, "Item003Description"]]}` from `{"tables": {"Products": [{"product_id": 1, "name": "ABC123XYZ"}, {"product_id": 2, "name": "A12B34C"}, {"product_id": 3, "name": "Product56789"}, {"product_id": 4, "name": "NoDigitsHere"}, {"product_id": 5, "name": "789Product"}, {"product_id": 6, "name": "Item003Description"}, {"product_id": 7, "name": "Product12X34"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The requirement is about an entire digit run, not any three-digit slice.** A product name qualifies when it contains a maximal consecutive run of digits whose length is exactly three. Merely finding three adjacent digits is insufficient. For example, `"ABC123XYZ"` qualifies, but `"Product56789"` does not: although `"567"`, `"678"`, and `"789"` are three-character digit slices, all of them belong to one five-digit run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "name": "ABC123XYZ"}, {"product_id": 2, "name": "A12B34C"}, {"product_id": 3, "name": "Product56789"}, {"product_id": 4, "name": "NoDigitsHere"}, {"product_id": 5, "name": "789Product"}, {"product_id": 6, "name": "Item003Description"}, {"product_id": 7, "name": "Product12X34"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The query expresses the exact-run condition with this regular expression:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query expresses the exact-run condition with this regula... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

It helps to read the expression as three consecutive pieces.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "name"], "rows": [[1, "ABC123XYZ"], [5, "789Product"], [6, "Item003Description"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "name": "ABC123XYZ"}, {"product_id": 2, "name": "A12B34C"}, {"product_id": 3, "name": "Product56789"}, {"product_id": 4, "name": "NoDigitsHere"}, {"product_id": 5, "name": "789Product"}, {"product_id": 6, "name": "Item003Description"}, {"product_id": 7, "name": "Product12X34"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "name"], "rows": [[1, "ABC123XYZ"], [5, "789Product"], [6, "Item003Description"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three digits without boundaries:** `[0-9]{3}` :** - **Three digits without boundaries:** `[0-9]{3}` alone incorrectly accepts any run of four or more digits because it can match a three-character portion.
- **Word-boundary token:** A regex word boundary does not mean “digit versus non-digit”; letters, digits, and underscores are all word characters in common regex rules. Explicit digit negation is the correct boundary.
- **String-length arithmetic:** Removing non-digits or splitting names can solve the task procedurally, but it is more verbose and easier to mishandle multiple runs than the direct regex.
- **Leading zeros:** `"007"` is exactly three digit characters and must qualify. Numeric conversion would erase the structural leading zeros and is inappropriate.
- **Run at the start:** The `^` alternative allows `"123ABC"` even though there is no preceding character.
- **Run at the end:** The `$` alternative allows `"ABC123"` even though there is no following character.
- **Name of exactly three digits:** Both anchors match, so the row is correctly included.
- **Several valid runs:** A name such as `"A123B456C"` is returned once, not once per regex occurrence, because `WHERE` filters rows.
- **Mixed run lengths:** A name qualifies if it has at least one exact three-digit run, even when another part of the same name contains a longer or shorter run.
- **Ordering syntax:** `ORDER BY 1` is concise but depends on select-list position. Writing `ORDER BY product_id ASC` would be more self-documenting while producing the same result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $S$ be the total number of characters across all product names scanned, and let $r$ be the number of matching rows. With a normal linear regex scan for this fixed-size pattern, filtering takes $O(S)$ time. Producing ascending order may require sorting the $r$ matching rows, costing $O(r\log r)$ time and $O(r)$ working space. This gives $O(S+r\log r)$ time and $O(r)$ sort space, consistent with the manifest's $O(S+n\log n)$ notation when $n$ denotes the result count or a safe upper bound on rows.
- **Auxiliary Space Complexity:** $O(S+n\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

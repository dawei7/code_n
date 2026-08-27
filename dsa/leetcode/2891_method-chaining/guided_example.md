# Guided Example: Method Chaining

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"animals": [{"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464}, {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41}, {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328}, {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463}, {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50}, {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}]}}`
- **Required output:** `{"columns": ["name"], "rows": [["Tatiana"], ["Jonathan"], ["Tommy"], ["Alex"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to list the names of animals that weigh **strictly more than** `100` kilograms.

The objective is to compute `{"columns": ["name"], "rows": [["Tatiana"], ["Jonathan"], ["Tommy"], ["Alex"]]}` from `{"tables": {"animals": [{"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464}, {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41}, {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328}, {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463}, {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50}, {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The chain performs three operations in contract order.** The requested table must first exclude light animals, then order qualifying animals from heaviest to lightest, then show only names. The source writes those operations as one returned expression:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"animals": [{"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464}, {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41}, {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328}, {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463}, {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50}, {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`animals[animals['weight'] > 100].sort_values('weight', ascending=false)[['name']]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `animals[animals['weight'] > 100].sort_values('weight', asce... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Method chaining shortens the syntax, but the intermediate tables still exist conceptually. Reading left to right reveals the complete algorithm.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name"], "rows": [["Tatiana"], ["Jonathan"], ["Tommy"], ["Alex"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"animals": [{"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464}, {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41}, {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328}, {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463}, {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50}, {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name"], "rows": [["Tatiana"], ["Jonathan"], ["Tommy"], ["Alex"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Named intermediate variables:** They perform t:** - **Named intermediate variables:** They perform the same operations and can be easier to debug, but do not meet the optional one-line chaining challenge.
- **Sort before filtering:** Correct membership and order are possible, but sorting all $n$ rows costs $O(n\log n)$ instead of sorting only $h$ matches.
- **`query` method:** `animals.query('weight > 100')` can replace Boolean indexing but adds expression parsing.
- **Weight exactly 100:** It is excluded because the predicate is strictly greater.
- **No heavy animals:** The result is an empty DataFrame with one `name` column.
- **All animals heavy:** Sorting dominates at $O(n\log n)$.
- **Equal weights:** Their relative order is not explicitly defined by this source; only descending weight is guaranteed.
- **Space accounting:** Include the $n$-element Boolean mask when describing the exact implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+h\log h)$. Let $n$ be the total row count and $h$ the number of animals heavier than 100. Building and applying the mask takes $O(n)$. Sorting the qualifying rows takes $O(h\log h)$, and projecting names takes $O(h)$. Total time is $O(n+h\log h)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n+h)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

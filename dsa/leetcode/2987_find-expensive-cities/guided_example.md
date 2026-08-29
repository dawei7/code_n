# Guided Example: Find Expensive Cities

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Listings": [{"listing_id": 113, "city": "LosAngeles", "price": 7560386}, {"listing_id": 136, "city": "SanFrancisco", "price": 2380268}, {"listing_id": 92, "city": "Chicago", "price": 9833209}, {"listing_id": 60, "city": "Chicago", "price": 5147582}, {"listing_id": 8, "city": "Chicago", "price": 5274441}, {"listing_id": 79, "city": "SanFrancisco", "price": 8372065}, {"listing_id": 37, "city": "Chicago", "price": 7939595}, {"listing_id": 53, "city": "LosAngeles", "price": 4965123}, {"listing_id": 178, "city": "SanFrancisco", "price": 999207}, {"listing_id": 51, "city": "NewYork", "price": 5951718}, {"listing_id": 121, "city": "NewYork", "price": 2893760}]}}`
- **Required output:** `{"columns": ["city"], "rows": [["Chicago"], ["LosAngeles"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Listings`

The objective is to compute `{"columns": ["city"], "rows": [["Chicago"], ["LosAngeles"]]}` from `{"tables": {"Listings": [{"listing_id": 113, "city": "LosAngeles", "price": 7560386}, {"listing_id": 136, "city": "SanFrancisco", "price": 2380268}, {"listing_id": 92, "city": "Chicago", "price": 9833209}, {"listing_id": 60, "city": "Chicago", "price": 5147582}, {"listing_id": 8, "city": "Chicago", "price": 5274441}, {"listing_id": 79, "city": "SanFrancisco", "price": 8372065}, {"listing_id": 37, "city": "Chicago", "price": 7939595}, {"listing_id": 53, "city": "LosAngeles", "price": 4965123}, {"listing_id": 178, "city": "SanFrancisco", "price": 999207}, {"listing_id": 51, "city": "NewYork", "price": 5951718}, {"listing_id": 121, "city": "NewYork", "price": 2893760}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare each city with one listing-weighted national mean

The national average home price is the average over every row in `Listings`:

`SELECT AVG(price) FROM Listings`.

This is not the average of the city averages. Every listing contributes one observation nationally, so a city with many listings contributes proportionally more to the national mean than a city with one listing.

The outer query groups rows by `city` and computes `AVG(price)` for each group. Its `HAVING` clause retains a city only when that group average is strictly greater than the scalar national average.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Listings": [{"listing_id": 113, "city": "LosAngeles", "price": 7560386}, {"listing_id": 136, "city": "SanFrancisco", "price": 2380268}, {"listing_id": 92, "city": "Chicago", "price": 9833209}, {"listing_id": 60, "city": "Chicago", "price": 5147582}, {"listing_id": 8, "city": "Chicago", "price": 5274441}, {"listing_id": 79, "city": "SanFrancisco", "price": 8372065}, {"listing_id": 37, "city": "Chicago", "price": 7939595}, {"listing_id": 53, "city": "LosAngeles", "price": 4965123}, {"listing_id": 178, "city": "SanFrancisco", "price": 999207}, {"listing_id": 51, "city": "NewYork", "price": 5951718}, {"listing_id": 121, "city": "NewYork", "price": 2893760}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `HAVING` appears instead of `WHERE`

`WHERE` filters individual source rows before grouping and cannot directly test `AVG(price)` for a completed city group. `HAVING` is evaluated after grouping and may refer to aggregate expressions. The logical sequence is:

1. read all listing rows;
2. form one group per city;
3. calculate each group’s average;
4. compare that average with the scalar subquery result;
5. keep qualifying groups.

No row-level price threshold is applied. A city may have some cheap listings and still qualify if its overall mean exceeds the national mean.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The scalar subquery is global

The inner average has no correlation with the current outer city and no `GROUP BY`. It produces one value for the full table. MySQL can evaluate this uncorrelated scalar subquery once and reuse it for every city comparison.

Conceptually, if prices are $p_1,\ldots,p_R$, the national value is

$$
\frac{p_1+\cdots+p_R}{R}.
$$

For a city with $r$ listings and sum $S$, its value is $S/r$. The city survives only if $S/r$ is strictly larger than the national quotient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["city"], "rows": [["Chicago"], ["LosAngeles"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Listings": [{"listing_id": 113, "city": "LosAngeles", "price": 7560386}, {"listing_id": 136, "city": "SanFrancisco", "price": 2380268}, {"listing_id": 92, "city": "Chicago", "price": 9833209}, {"listing_id": 60, "city": "Chicago", "price": 5147582}, {"listing_id": 8, "city": "Chicago", "price": 5274441}, {"listing_id": 79, "city": "SanFrancisco", "price": 8372065}, {"listing_id": 37, "city": "Chicago", "price": 7939595}, {"listing_id": 53, "city": "LosAngeles", "price": 4965123}, {"listing_id": 178, "city": "SanFrancisco", "price": 999207}, {"listing_id": 51, "city": "NewYork", "price": 5951718}, {"listing_id": 121, "city": "NewYork", "price": 2893760}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["city"], "rows": [["Chicago"], ["LosAngeles"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Average the city averages:** This weights cities equally rather than listings and gives a different national statistic when city sizes differ.
- **Filter rows in `WHERE` by national average:** That would select expensive individual listings before averaging and solve a different problem.
- **CTE for the national mean:** Computing it once in a named CTE is equivalent; the uncorrelated scalar subquery is compact.
- **Window average:** `AVG(price) OVER ()` can attach the national value to rows before grouping, but introduces an intermediate relation.
- **One city only:** Its mean equals the national mean, so no result is returned.
- **City exactly at the national mean:** Strict `>` excludes it.
- **Cities with different row counts:** The national mean remains listing-weighted, as required.
- **Duplicate prices or names:** They are ordinary separate listings because `listing_id` identifies rows.
- **Output ordering:** `ORDER BY 1` sorts city names ascending.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the listing-row count and $C$ the number of cities. The scalar subquery scans $R$ rows, and the outer grouping scans them again. This is still $O(R)$ aggregate work. Group construction may use hashing or sorting; a conservative general bound is $O(R\log R)$.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

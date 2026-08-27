# Guided Example: Filter Restaurants by Vegan-Friendly, Price and Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], "veganFriendly": 1, "maxPrice": 50, "maxDistance": 10}`
- **Required output:** `[3, 1, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `restaurants` where  $\text{restaurants}[i] = [\text{id}_{i}, \text{rating}_{i}, \text{veganFriendly}_{i}, \text{price}_{i}, \text{distance}_{i}]$. You have to filter the restaurants using three filters.

The objective is to compute `[3, 1, 5]` from `{"restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], "veganFriendly": 1, "maxPrice": 50, "maxDistance": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode the required descending order

Python sorts keys in ascending order by default. The key function returns `(-x[1], -x[0])` for a restaurant `x`:

- `x[1]` is the rating, so a larger rating becomes a smaller negative number and appears earlier.
- `x[0]` is the identifier, so among equal ratings, a larger identifier likewise appears earlier.

For example, suppose three restaurants have rating and identifier pairs `(5, 3)`, `(8, 1)`, and `(5, 7)`. Their keys are `(-5, -3)`, `(-8, -1)`, and `(-5, -7)`. Ascending tuple order places rating eight first. Among the two rating-five records, `(-5, -7)` comes before `(-5, -3)`, so identifier seven correctly precedes identifier three.

The call `restaurants.sort(...)` sorts the supplied list in place. After this line, every record is already in the exact priority order required for the final answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], "veganFriendly": 1, "maxPrice": 50, "maxDistance": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read each field according to the record contract

The loop header `for idx, _, vegan, price, dist in restaurants` unpacks the five fields:

- `idx` receives the restaurant identifier.
- `_` receives the rating. The conventional underscore name signals that no later calculation needs it because sorting has already used it.
- `vegan` receives the binary vegan-friendly flag.
- `price` and `dist` receive the two numeric limits being tested.

Using field positions exactly is important. The restaurant identifier is not the record’s list index, and the price and distance constraints are separate. Unpacking gives descriptive names and makes each comparison correspond directly to one part of the contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop header `for idx, _, vegan, price, dist in restauran... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One comparison handles both vegan modes

The condition is `vegan >= veganFriendly`. Both values are binary:

- When `veganFriendly` is zero, both zero and one are greater than or equal to zero, so the vegan flag does not exclude any restaurant.
- When `veganFriendly` is one, only a restaurant whose flag is one passes.

This avoids a separate branch for the two request modes. It is correct because the allowed values are exactly zero and one; the comparison should not be generalized blindly to unrelated flags.

The remaining tests are `price <= maxPrice` and `dist <= maxDistance`. The inclusive comparisons matter: a restaurant costing exactly `maxPrice` or located exactly `maxDistance` away is allowed. All three tests are connected by `and`, so a record is appended only if every required condition is true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], "veganFriendly": 1, "maxPrice": 50, "maxDistance": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Filter before sorting:** Build a list of quali:** - **Filter before sorting:** Build a list of qualifying records first, then sort only those records by rating and identifier. This has $O(n + q \log q)$ time for $q$ matches and avoids sorting rejected records, but it requires storing the qualifying records before extracting identifiers.
- **Non-mutating sorted copy:** Use `sorted(restaurants, key=...)` to preserve the caller’s input order. It has the same asymptotic time and space bounds but allocates a separate list.
- **Sorting with positive keys and reverse mode:** A key of `(rating, id)` together with `reverse=true` also produces descending order for both fields. Negative keys make the two required directions explicit without relying on a global reversal.
- **Heap-based selection:** A heap is useful when only the best few results are requested. Here every qualifying identifier must be returned, so a complete ordered result still requires work comparable to sorting.
- **Vegan filter disabled:** When `veganFriendly == 0`, restaurants with either flag value pass the vegan test. The `>=` comparison implements this without a special case.
- **Vegan filter enabled:** When `veganFriendly == 1`, only records whose vegan field is one pass. A zero is rejected before the identifier can be appended.
- **Inclusive limits:** Prices and distances equal to their maximum limits must be accepted. Replacing `<=` with `<` would incorrectly remove boundary records.
- **Equal ratings:** Larger identifiers must come first. The second component `-x[0]` supplies exactly that tie-breaker.
- **No matches:** The loop performs no append and returns `[]`, which is already a valid ordered result.
- **All records match:** Every identifier is returned in the order established by the initial sort; the result may use $O(n)$ space.
- **Input side effect:** Because the sort is in place, code outside this method observes the reordered restaurant records. Use a copied or non-mutating sort if preserving the original list is an additional requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the number of restaurant records.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

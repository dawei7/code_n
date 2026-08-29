# Guided Example: Rectangles Area

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Points": [{"id": 9, "x_value": -2, "y_value": -3}]}}`
- **Required output:** `{"columns": ["p1", "p2", "area"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Points`

The objective is to compute `{"columns": ["p1", "p2", "area"], "rows": []}` from `{"tables": {"Points": [{"id": 9, "x_value": -2, "y_value": -3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Any two suitable points determine opposite corners.** For an axis-aligned rectangle, two opposite corners must differ in both their x-coordinates and y-coordinates. Their horizontal side length is the absolute x difference, and their vertical side length is the absolute y difference. The area is their product.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Points": [{"id": 9, "x_value": -2, "y_value": -3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The query creates two aliases, `p1` and `p2`, of the `Points` table. Joining them considers pairs of point rows. The condition `p1.id < p2.id` does two jobs at once: it prevents pairing a point with itself, and it keeps exactly one orientation of every unordered pair.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Without that inequality, points with IDs one and two would appear both as `1, 2` and `2, 1`. Since the rectangle is the same in both directions, that would duplicate the output. Choosing smaller ID as `p1` also satisfies the contract's canonical `p1 < p2` representation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["p1", "p2", "area"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Points": [{"id": 9, "x_value": -2, "y_value": -3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["p1", "p2", "area"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cross join with a WHERE pair condition:** Writing `CROSS JOIN Points p2 WHERE p1.id < p2.id` is logically equivalent. Keeping the pair condition in `JOIN ... ON` makes pair formation explicit.
- **Filter on area greater than zero:** This is equivalent for integer coordinates but repeats or aliases the area calculation. Testing coordinate inequality states the geometry directly.
- **Use LEAST and GREATEST for IDs:** Generate both orientations and normalize the IDs afterward. That performs duplicate work; `p1.id < p2.id` prevents duplicates earlier.
- **GROUP BY normalized pair:** It could remove duplicated orientations, but correct join construction makes aggregation unnecessary.
- **Same x-coordinate:** Width is zero, so the pair is excluded.
- **Same y-coordinate:** Height is zero, so the pair is excluded.
- **Identical coordinates with different IDs:** Both differences are zero and the pair is excluded even though the rows are distinct.
- **Negative coordinates:** Absolute differences produce the correct positive side lengths.
- **Smaller ID lies right or above:** Spatial order does not matter because `ABS` handles direction.
- **Equal areas:** Rows are ordered by `p1` ascending and then `p2` ascending.
- **No valid pairs:** The result is empty; the query does not invent rectangles.
- **Exactly two valid points:** Their one canonical pair produces one row.
- **Other corners absent from Points:** The pair still determines an axis-aligned rectangle under this contract; no four-point existence check is required.
- **Unique ID guarantee:** It makes `p1.id < p2.id` a reliable strict ordering and ensures output pair identities are unique.
- **Area overflow in other systems:** Coordinate ranges and SQL integer promotion should be considered in a broader schema. Casting to a wider numeric type may be needed for extremely large coordinates.
- **Ordering aliases:** MySQL permits `area`, `p1`, and `p2` in `ORDER BY` because they are selected aliases.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P^2 + R log R)$. Let `P` be the number of point rows and `R` the number of valid reported pairs. The self-join can consider `P(P - 1) / 2` unordered pairs, so pair generation and filtering take `O(P^2)` work in the conventional nested-pair model.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

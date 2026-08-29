# Guided Example: Count Apples and Oranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Boxes": [{"box_id": 2, "chest_id": null, "apple_count": 6, "orange_count": 15}, {"box_id": 18, "chest_id": 14, "apple_count": 4, "orange_count": 15}, {"box_id": 19, "chest_id": 3, "apple_count": 8, "orange_count": 4}, {"box_id": 12, "chest_id": 2, "apple_count": 19, "orange_count": 20}, {"box_id": 20, "chest_id": 6, "apple_count": 12, "orange_count": 9}, {"box_id": 8, "chest_id": 6, "apple_count": 9, "orange_count": 9}, {"box_id": 3, "chest_id": 14, "apple_count": 16, "orange_count": 7}], "Chests": [{"chest_id": 6, "apple_count": 5, "orange_count": 6}, {"chest_id": 14, "apple_count": 20, "orange_count": 10}, {"chest_id": 2, "apple_count": 8, "orange_count": 8}, {"chest_id": 3, "apple_count": 19, "orange_count": 4}, {"chest_id": 16, "apple_count": 19, "orange_count": 19}]}}`
- **Required output:** `{"columns": ["apple_count", "orange_count"], "rows": [[151, 123]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Boxes`

The objective is to compute `{"columns": ["apple_count", "orange_count"], "rows": [[151, 123]]}` from `{"tables": {"Boxes": [{"box_id": 2, "chest_id": null, "apple_count": 6, "orange_count": 15}, {"box_id": 18, "chest_id": 14, "apple_count": 4, "orange_count": 15}, {"box_id": 19, "chest_id": 3, "apple_count": 8, "orange_count": 4}, {"box_id": 12, "chest_id": 2, "apple_count": 19, "orange_count": 20}, {"box_id": 20, "chest_id": 6, "apple_count": 12, "orange_count": 9}, {"box_id": 8, "chest_id": 6, "apple_count": 9, "orange_count": 9}, {"box_id": 3, "chest_id": 14, "apple_count": 16, "orange_count": 7}], "Chests": [{"chest_id": 6, "apple_count": 5, "orange_count": 6}, {"chest_id": 14, "apple_count": 20, "orange_count": 10}, {"chest_id": 2, "apple_count": 8, "orange_count": 8}, {"chest_id": 3, "apple_count": 19, "orange_count": 4}, {"chest_id": 16, "apple_count": 19, "orange_count": 19}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from boxes because only their contents count

The result asks for fruit contained in all boxes. Every `Boxes` row contributes its own apples and oranges. A chest contributes only when a box references it.

Accordingly, `Boxes AS b` is the left side of the join. This guarantees that every box remains in the intermediate result, whether or not `chest_id` is null or finds a matching chest.

Starting from `Chests` would incorrectly include unreferenced chests and could omit boxes without chests.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Boxes": [{"box_id": 2, "chest_id": null, "apple_count": 6, "orange_count": 15}, {"box_id": 18, "chest_id": 14, "apple_count": 4, "orange_count": 15}, {"box_id": 19, "chest_id": 3, "apple_count": 8, "orange_count": 4}, {"box_id": 12, "chest_id": 2, "apple_count": 19, "orange_count": 20}, {"box_id": 20, "chest_id": 6, "apple_count": 12, "orange_count": 9}, {"box_id": 8, "chest_id": 6, "apple_count": 9, "orange_count": 9}, {"box_id": 3, "chest_id": 14, "apple_count": 16, "orange_count": 7}], "Chests": [{"chest_id": 6, "apple_count": 5, "orange_count": 6}, {"chest_id": 14, "apple_count": 20, "orange_count": 10}, {"chest_id": 2, "apple_count": 8, "orange_count": 8}, {"chest_id": 3, "apple_count": 19, "orange_count": 4}, {"chest_id": 16, "apple_count": 19, "orange_count": 19}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match a box to its optional chest

`LEFT JOIN Chests AS c USING (chest_id)` joins rows whose `chest_id` values are equal. `USING` is concise because both tables use the same column name.

`Chests.chest_id` is unique, so one box can match at most one chest. The join therefore does not multiply a box because of several chest-table matches.

When no match exists, all projected `c` columns are null while the box row remains. This is precisely the optional relationship needed by the problem.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Treat absent chest fruit as zero

SQL arithmetic involving null produces null. Without protection, `b.apple_count + c.apple_count` would be null for a box with no chest, and that box's own fruit could disappear from the aggregate.

The query uses

`COALESCE(c.apple_count, 0)`

and the corresponding orange expression. `COALESCE` returns the chest count when present and zero otherwise, so a chestless box contributes only its own contents.

The box columns are also wrapped in `COALESCE(b.apple_count, 0)` and `COALESCE(b.orange_count, 0)`. The schema normally supplies counts, but this makes a generalized null box count contribute zero rather than nullifying its row expression.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["apple_count", "orange_count"], "rows": [[151, 123]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Boxes": [{"box_id": 2, "chest_id": null, "apple_count": 6, "orange_count": 15}, {"box_id": 18, "chest_id": 14, "apple_count": 4, "orange_count": 15}, {"box_id": 19, "chest_id": 3, "apple_count": 8, "orange_count": 4}, {"box_id": 12, "chest_id": 2, "apple_count": 19, "orange_count": 20}, {"box_id": 20, "chest_id": 6, "apple_count": 12, "orange_count": 9}, {"box_id": 8, "chest_id": 6, "apple_count": 9, "orange_count": 9}, {"box_id": 3, "chest_id": 14, "apple_count": 16, "orange_count": 7}], "Chests": [{"chest_id": 6, "apple_count": 5, "orange_count": 6}, {"chest_id": 14, "apple_count": 20, "orange_count": 10}, {"chest_id": 2, "apple_count": 8, "orange_count": 8}, {"chest_id": 3, "apple_count": 19, "orange_count": 4}, {"chest_id": 16, "apple_count": 19, "orange_count": 19}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["apple_count", "orange_count"], "rows": [[151, 123]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Inner join:** It would discard boxes whose `chest_id` is null or unmatched, losing their own fruit counts.
- **Start from Chests:** It risks including unreferenced chests and does not naturally preserve chestless boxes.
- **Correlated subqueries:** Looking up chest apples and oranges separately per box repeats work and is less clear than one join.
- **`IFNULL` instead of `COALESCE`:** MySQL's two-argument `IFNULL` can supply the same zeros; `COALESCE` is standard and handles multiple fallbacks.
- **Box without a chest:** The left join supplies null chest columns, converted to zero.
- **Referenced chest:** Its apples and oranges are each added to the corresponding box counts.
- **Chest referenced by several boxes:** Its fruit contributes once per joined box, as the exact query specifies.
- **Unreferenced chest:** It contributes nothing because there is no left-side box row.
- **Null box counts in generalized data:** The explicit box-side `COALESCE` treats them as zero.
- **Unique chest key:** It prevents one box from being duplicated by several matching chest rows.
- **No grouping:** A single total row is intended; grouping by box or chest would change the output shape.
- **Empty Boxes table outside stated examples:** Standard SQL `SUM` over no rows returns null rather than zero; an outer `COALESCE(SUM(...),0)` would be needed if a zero row were required.
- **Independent fruit totals:** Apples and oranges are summed with parallel expressions, so neither category affects the other.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let $B$ be the number of boxes and $C$ the number of chests. With a hash join, building a lookup for chests costs expected $O(C)$ time and space, then scanning boxes and updating the two sums costs $O(B)$ time. Total expected time is $O(B+C)$ and working space is $O(C)$.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Binary Tree Nodes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tree": [{"N": 1, "P": 2}, {"N": 3, "P": 2}, {"N": 6, "P": 8}, {"N": 9, "P": 8}, {"N": 2, "P": 5}, {"N": 8, "P": 5}, {"N": 5, "P": null}]}}`
- **Required output:** `{"columns": ["N", "Type"], "rows": [[1, "Leaf"], [2, "Inner"], [3, "Leaf"], [5, "Root"], [6, "Leaf"], [8, "Inner"], [9, "Leaf"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tree`

The objective is to compute `{"columns": ["N", "Type"], "rows": [[1, "Leaf"], [2, "Inner"], [3, "Leaf"], [5, "Root"], [6, "Leaf"], [8, "Inner"], [9, "Leaf"]]}` from `{"tables": {"Tree": [{"N": 1, "P": 2}, {"N": 3, "P": 2}, {"N": 6, "P": 8}, {"N": 9, "P": 8}, {"N": 2, "P": 5}, {"N": 8, "P": 5}, {"N": 5, "P": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Classify root status from the node's own row.** In `Tree`, column `P` stores a node's parent. A null parent means the node is the root. The outer `IF` checks `t1.P IS NULL` first and returns `'Root'`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tree": [{"N": 1, "P": 2}, {"N": 3, "P": 2}, {"N": 6, "P": 8}, {"N": 9, "P": 8}, {"N": 2, "P": 5}, {"N": 8, "P": 5}, {"N": 5, "P": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This priority matters because the root can also have children. Its child status must not cause it to be labeled inner.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Discover children with a self left join.** Alias `t1` represents the node being classified. Alias `t2` represents a potential child. The join condition is

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["N", "Type"], "rows": [[1, "Leaf"], [2, "Inner"], [3, "Leaf"], [5, "Root"], [6, "Leaf"], [8, "Inner"], [9, "Leaf"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tree": [{"N": 1, "P": 2}, {"N": 3, "P": 2}, {"N": 6, "P": 8}, {"N": 9, "P": 8}, {"N": 2, "P": 5}, {"N": 8, "P": 5}, {"N": 5, "P": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["N", "Type"], "rows": [[1, "Leaf"], [2, "Inner"], [3, "Leaf"], [5, "Root"], [6, "Leaf"], [8, "Inner"], [9, "Leaf"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`EXISTS` correlated subquery:** Check whether any row has `P=t1.N`. It avoids duplicate child rows and therefore removes the need for `DISTINCT`.
- **Parent-value set CTE:** Materialize distinct non-null parents, then left join that set to nodes. This makes child existence explicit.
- **Inner join:** It is incorrect because leaves would vanish from the result.
- **Root with children:** The outer root check takes priority and returns Root.
- **Root with no children:** A one-node tree is still Root, not Leaf, because null parent is checked first.
- **Node with two children:** Join duplication is collapsed by `DISTINCT`.
- **Non-root with no children:** Null-extended `t2.P` yields Leaf.
- **Non-root with a child:** At least one match yields Inner.
- **Ascending order:** `ORDER BY 1` sorts by node value `N`.
- **Valid-tree assumption:** The classification assumes the table represents a tree; cycles or multiple roots would be labeled mechanically from the same rules.
- **Why checking `t2.P` signals a match:** On a genuine child row, the join predicate makes `t2.P=t1.N`, so it is non-null for a valid node identifier. On no match, left-join null extension makes it null. A dedicated child ID test would communicate this more directly but behave the same.
- **Distinct cost is caused by the join shape:** Without `DISTINCT`, a parent appears once per child. A valid binary tree limits this to two, but the required result still needs exactly one row per node.
- **Node values need not be consecutive:** Classification uses equality relationships, not arithmetic on `N`. Sparse, negative, or large identifiers would work identically if allowed by the table.
- **Ordering after deduplication:** The final sort acts on the one-row-per-node result, ensuring duplicate child matches do not disturb the ascending node sequence.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of nodes. With an index on parent column `P`, matching children can be found efficiently; ordering and duplicate elimination commonly lead to an $O(R\log R)$ logical upper bound. Without a useful index, a naive nested-loop self-join could degrade toward $O(R^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

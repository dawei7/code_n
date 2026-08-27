# Guided Example: Tree Node

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tree": [{"id": 1, "p_id": null}, {"id": 2, "p_id": 1}, {"id": 3, "p_id": 2}]}}`
- **Required output:** `{"columns": ["id", "type"], "rows": [[1, "Root"], [2, "Inner"], [3, "Leaf"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tree`

The objective is to compute `{"columns": ["id", "type"], "rows": [[1, "Root"], [2, "Inner"], [3, "Leaf"]]}` from `{"tables": {"Tree": [{"id": 1, "p_id": null}, {"id": 2, "p_id": 1}, {"id": 3, "p_id": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identifying the root

The root is the only node without a parent in a valid tree. This test must come first. A one-node tree has no parent and no children; by the problem’s rule it is Root, not Leaf. First-match `CASE` semantics ensure the root classification wins before child checks.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tree": [{"id": 1, "p_id": null}, {"id": 2, "p_id": 1}, {"id": 3, "p_id": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Identifying nodes with children

The subquery lists every parent reference used by any node. If current `id` appears there, at least one other row names it as parent, so it has at least one child.

Because the root was handled already, a remaining node that has children also has its own non-null parent and is exactly an Inner node.

The subquery includes the root row’s null `p_id`. SQL `IN` with a null-containing list has three-valued behavior: a matching non-null parent still yields true; a nonmatching ID may yield unknown rather than false. In a `WHEN` condition, unknown is not true, so execution falls to `ELSE`. The result remains correct. Filtering `WHERE p_id IS NOT NULL` would make the intent clearer and avoid this subtlety.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The subquery lists every parent reference used by any node.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Everything else is a leaf

A row reaching:



is not root, so it has a parent. It did not match any parent reference, so it has no children. Those are exactly the leaf conditions.

For the sample, node 1 has null parent and is Root. Node 2 appears as `p_id` for nodes 4 and 5, so after failing the root test it is Inner. Nodes 3, 4, and 5 never appear as a parent and become Leaf.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "type"], "rows": [[1, "Root"], [2, "Inner"], [3, "Leaf"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tree": [{"id": 1, "p_id": null}, {"id": 2, "p_id": 1}, {"id": 3, "p_id": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "type"], "rows": [[1, "Root"], [2, "Inner"], [3, "Leaf"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Left join to children and grouping:** Join eac:** - **Left join to children and grouping:** Join each node to rows whose `p_id` equals its ID, then classify based on null parent and child count. Works but may multiply rows before grouping.
- **`EXISTS`:** `EXISTS (SELECT 1 FROM Tree child WHERE child.p_id = Tree.id)` directly tests for a child and avoids `IN` null semantics.
- **Three `UNION` branches:** Query roots, inner nodes, and leaves separately. More verbose and repeats table logic.
- **Root checked after parent membership:** Risky for a one-node tree or any root with children; root status must have priority.
- **One-node tree:** Null parent makes it Root even though it also has no children.
- **Root with children:** First branch still labels Root, not Inner.
- **Non-root with children:** Appears in `p_id` and becomes Inner.
- **Non-root without children:** Falls to Leaf.
- **Null inside `IN` subquery:** A nonmatch can be unknown; `CASE WHEN` treats it as not true and reaches Leaf. Filtering nulls is clearer.
- **Repeated parent IDs:** Merely mean multiple children and do not change membership.
- **Any output order:** No sort is required.
- **Valid-tree guarantee:** Ensures the categories cover the structure consistently.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of nodes. A database can materialize/hash the `p_id` subquery in $O(n)$ expected time and space, then test each outer row in expected constant time, for expected $O(n)$ total work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Find Center of Star Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [[1, 2], [2, 3], [4, 2]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one **center** node and **exactly** $n - 1$ edges that connect the center node with every other node.

The objective is to compute `2` from `{"edges": [[1, 2], [2, 3], [4, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the promise that the graph is already a valid star

A star graph has one center connected to every other node. Each non-center node is a leaf connected only to that center. Therefore, the center is an endpoint of every edge, while a leaf appears in exactly one edge.

A degree-counting solution could inspect all $n-1$ edges and find the node with degree $n-1$. That is unnecessary because the input is guaranteed to be a valid star. Any two different star edges must share the center, and they cannot share a leaf.

The graph has at least three nodes, so it has at least two edges. The protected solution looks only at `edges[0]` and `edges[1]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [[1, 2], [2, 3], [4, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test one endpoint of the first edge

Write the first edge as `[a, b]`. Exactly one of `a` and `b` is the center; the other is the leaf attached by this edge.

The expression `edges[0][0] in edges[1]` asks whether `a` is one of the two endpoints of the second edge. Membership in this two-element list performs at most two equality checks.

- If `a` appears in the second edge, then `a` belongs to two distinct star edges. A leaf has degree one and cannot do that, so `a` must be the center.
- If `a` does not appear in the second edge, then `a` is the first edge's leaf. The other first-edge endpoint `b` must therefore be the center, so the solution returns `edges[0][1]`.

This conditional completely identifies the common endpoint without constructing sets, degree arrays, or an adjacency list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first two edges must have exactly one common endpoint

Every edge in a star has the form `[center, leaf]`, although the input may list those two endpoints in either order. The first two entries of `edges` represent two different connections in the valid $n-1$ edge star. Their leaf endpoints are different nodes because each leaf has exactly one connection and the star contains one edge per leaf. Both edges contain the center. They consequently intersect in exactly that one node.

This is why checking just one endpoint of the first edge is enough. If it is not the common node, the first edge has only one other endpoint, and that other endpoint must be common.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [[1, 2], [2, 3], [4, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Degree counting:** Count both endpoints of every edge and return the node with degree $n-1$. This works for a valid star but costs $O(n)$ time and $O(n)$ space.
- **Adjacency list:** Building the full graph also reveals degrees, but it stores information that the star guarantee makes unnecessary.
- **Set intersection:** Intersecting the endpoint sets of the first two edges finds the center in constant time, though allocating sets is more machinery than the direct membership test.
- **Compare all four endpoint combinations:** It works, but testing one first-edge endpoint already determines which of the two is common.
- **Arbitrary endpoint order:** The center may appear first or second in either edge; list membership handles both orientations.
- **Minimum graph size:** With $n=3$, there are exactly two edges, so both required entries exist and their shared endpoint is the center.
- **Many-node star:** The method still reads only two edges; graph size does not affect its work.
- **First tested node is the center:** Membership succeeds and returns that node.
- **Second first-edge node is the center:** Membership for the first node fails, so the conditional returns the other endpoint.
- **Distinct leaves:** Two different valid star edges cannot share a leaf, which makes their intersection unique.
- **Duplicate edges:** They would undermine the "two distinct leaves" reasoning, but duplicate connections are not part of the promised valid star representation.
- **Self-loops:** The contract excludes them through `u_i != v_i` and the valid-star guarantee.
- **Invalid arbitrary graph:** The first two edges may share a non-global node or share nothing, so this constant-time rule must not be reused without the star guarantee.
- **No need to infer `n`:** The center is identified directly; computing `len(edges) + 1` adds no useful information.
- **Input preservation:** The expression only reads endpoints and never reorders or mutates `edges`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The solution accesses two fixed edges and tests membership in a list of exactly two integers. The number of comparisons is bounded by a constant independent of $n$ and the number of edges. Time complexity is therefore $O(1)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

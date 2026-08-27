# Guided Example: Minimum Number of Vertices to Reach All Nodes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "edges": [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]}`
- **Required output:** `[0, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a** directed acyclic graph**, with `n` vertices numbered from `0` to `n-1`, and an array `edges` where $\text{edges}[i] = [\text{from}_{i}, \text{to}_{i}]$ represents a directed edge from node $\text{from}_{i}$ to node $\text{to}_{i}$.

The objective is to compute `[0, 3]` from `{"n": 6, "edges": [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify vertices that nothing else can enter

A vertex with in-degree zero has no incoming directed edge. No path starting at a different vertex can reach it, because the final step of any such path would have to be an incoming edge.

Therefore every zero-in-degree vertex is mandatory in any starting set that reaches the whole graph. Omitting even one would leave that vertex unreachable.

The exact source counts which vertices appear as edge targets. `Counter(t for _, t in edges)` ignores each source endpoint and records one occurrence for every incoming edge at target `t`.

The actual numeric in-degree is more information than the final filter needs, but `Counter` provides it compactly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "edges": [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use Counter's missing-key behavior

For each vertex `i` from zero through `n-1`, the list comprehension checks `cnt[i] == 0`.

A `Counter` returns zero for a key that was never inserted. Thus a vertex that never occurs as a target is recognized without preinitializing all vertices in the counter.

Vertices with one or many incoming edges both fail the zero test and are excluded.

The returned order is increasing vertex number because `range(n)` is scanned in that order. The problem accepts any order, so this deterministic ordering is valid but not required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each vertex `i` from zero through `n-1`, the list compre... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every selected vertex is necessary

Take a returned vertex `v`. Its in-degree is zero.

If a path from another vertex reached `v`, that path would contain a last directed edge `u -> v`. Such an edge would give `v` positive in-degree, contradicting the selection rule.

The only way to make `v` reachable from the chosen set is therefore to choose `v` itself. Every valid solution must contain every returned vertex.

This proves a lower bound: no solution can use fewer starting vertices than the number of zero-in-degree vertices.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "edges": [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean target array:** Mark every destination:** - **Boolean target array:** Mark every destination true and return false entries. It uses $O(N)$ space and avoids storing exact counts.
- **Full DFS from candidate sources:** It repeats reachability work that the DAG in-degree proof makes unnecessary.
- **Topological sorting:** Its initial queue contains the same zero-in-degree vertices, but producing the complete ordering is extra work.
- **Vertex with several incoming edges:** It is excluded just like a vertex with one incoming edge.
- **Vertex with no outgoing edges:** It may still be reachable and does not belong in the answer unless its in-degree is also zero.
- **Disconnected underlying graph:** Each DAG component has at least one zero-in-degree source, and the method selects sources from every component.
- **No incoming target occurrence:** `Counter` returns zero for the missing key.
- **Multiple source vertices:** Every one is mandatory even when their reachable regions overlap.
- **Any output order:** Increasing numeric order from the comprehension is acceptable.
- **Cycle outside the contract:** A cyclic source component could have no zero-in-degree vertex, so the proof would fail.
- **Duplicate edges:** The contract excludes duplicate pairs, but duplicates would only increase a positive count and would not change the zero/nonzero classification.
- **Self-loop:** It is incompatible with a DAG and would also invalidate the reachability argument.
- **Unique solution:** It follows from every zero-in-degree vertex being mandatory and the entire set being sufficient.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+M)$. Let $N$ be vertex count and $M$ be edge count. Building the counter examines each edge once, costing expected $O(M)$ time. Scanning all vertices costs $O(N)$. Total time is $O(N+M)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

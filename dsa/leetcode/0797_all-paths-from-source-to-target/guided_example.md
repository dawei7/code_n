# Guided Example: All Paths From Source to Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"graph": [[1, 2], [3], [3], []]}`
- **Required output:** `[[0, 1, 3], [0, 2, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to $n - 1$, find all possible paths from node `0` to node $n - 1$ and return them in **any order**.

The objective is to compute `[[0, 1, 3], [0, 2, 3]]` from `{"graph": [[1, 2], [3], [3], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat each queue entry as one unfinished path

The task asks for paths, not merely reachable vertices. Two different routes that arrive at the same vertex must remain separate because each may produce a different final answer.

The queue therefore stores complete path lists. It begins with `[0]`, the one path containing only the source. For a queued path, its last element is the current vertex:

`u = path[-1]`.

Every earlier list element records the exact route used to reach `u`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"graph": [[1, 2], [3], [3], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Expand a path by one directed edge

If `u` is not the target, the algorithm visits every outgoing neighbor `v` in `graph[u]`. The extended path is:

`path + [v]`.

Python list concatenation creates a new list. That copy is essential: all queue entries must own independent path histories. Mutating and reusing one list would let later extensions corrupt paths already waiting in the queue.

Each appended entry represents exactly one additional directed edge from its previous last vertex to `v`, so every queued list is always a valid source-originating path.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize completed paths

The target vertex is `n - 1`. When the dequeued path ends there, the method appends that list to `ans` and executes `continue`.

There is no need to explore outgoing edges from the target. The requested path ends on its first arrival at that vertex. Even if an input representation listed target neighbors, extending beyond the target would no longer be a source-to-target path of the requested form.

The target-ending list can be stored directly because that queue entry will never be mutated. Every extension elsewhere is created through concatenation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 1, 3], [0, 2, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"graph": [[1, 2], [3], [3], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 1, 3], [0, 2, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Depth-first backtracking:** Maintain one mutable path, copy it only at the target, and undo each choice. It has the same unavoidable output cost but usually smaller frontier memory.
- **Memoized paths from each vertex:** Reuse suffix paths in the DAG, but constructing prefixed copies still incurs output-sized work and may store many intermediate lists.
- **Vertex-level visited set:** Incorrect because different prefixes reaching the same vertex represent different answers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E+P\cdot V)$. Let $V$ be the number of vertices, $P$ the number of returned paths, and $R$ the number of source-originating path prefixes actually dequeued, including prefixes that end at dead ends. Let $L$ be the sum of the lengths of all generated prefixes.
- **Auxiliary Space Complexity:** $O(V + E + P \cdot V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

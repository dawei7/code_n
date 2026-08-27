# Guided Example: Sequence Reconstruction

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3]]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` where `nums` is a permutation of the integers in the range `[1, n]`. You are also given a 2D integer array `sequences` where $\text{sequences}[i]$ is a subsequence of `nums`.

The objective is to compute `false` from `{"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a directed graph represents the subsequences

Create one vertex for each value from `1` through `n`. If two values appear consecutively in one row as `a, b`, add a directed edge from `a` to `b`. That edge means that every valid supersequence must place `a` before `b`.

It is enough to add edges only between adjacent values of a row. Suppose a row is `[a, b, c, d]`. The edges $a \to b$, $b \to c$, and $c \to d$ already imply, by following paths, that `a` precedes `c` and `d`, that `b` precedes `d`, and so on. Adding an edge for every nonadjacent pair would repeat facts already supplied by transitivity and would make the graph unnecessarily large.

The code stores values as zero-based vertex indices. Because the contract guarantees that every value lies in `[1, n]`, subtracting one maps value `v` to index `v - 1` safely. `g[u]` contains every outgoing neighbor of vertex `u`, and `indeg[v]` records how many incoming edge occurrences still constrain vertex `v`.

An edge may be repeated when the same adjacent pair occurs in more than one sequence. The implementation deliberately does not deduplicate it. This remains correct: every stored copy increments the destination's indegree once, and processing the source later traverses every stored copy and decrements that indegree once. The copies therefore balance exactly. Here $E$ means the number of adjacent-pair occurrences, including duplicates.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why topological order captures a shortest supersequence

A topological ordering lists every graph vertex while respecting every directed edge. Thus it respects every adjacent relation, and consequently every entire row of `sequences` is a subsequence of it. Since `nums` is a permutation of all values `1` through `n`, a topological order also has exactly those values once each.

The input guarantees that every row is already a subsequence of `nums`. Therefore every graph edge points forward according to `nums`. This has two crucial consequences: the graph cannot contain a directed cycle, and `nums` itself is a valid topological order. The remaining question is whether another order is possible or whether some value is not needed in the shortest supersequence. In either situation, the partial constraints fail to force the whole permutation uniquely.

Kahn's topological-sort algorithm exposes exactly that ambiguity. A vertex whose indegree is zero has no unprocessed prerequisite, so it may legally be chosen next. Initially, the deque `q` contains every such vertex.

- If the deque contains exactly one vertex, that vertex is forced as the next element of every valid ordering.
- If it contains two or more vertices, either one can be chosen next. The constraints do not determine a unique order, so the answer must be `false`.
- If it is empty, there is no currently legal next vertex. Under a general graph this could mean either that all vertices were processed or that a cycle blocks the remaining vertices.

The loop condition `while len(q) == 1` encodes the first two cases directly. The algorithm proceeds only while the next choice is unique. It removes that sole vertex, then removes all of its outgoing constraints by decreasing its neighbors' indegrees. Any neighbor whose indegree reaches zero becomes available.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A topological ordering lists every graph vertex while respec... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the compact final check works here

The solution returns `len(q) == 0` without storing the produced order or a processed-vertex count. That is safe because of the source contract, not because it would be safe for an arbitrary directed graph.

If ambiguity ever occurs, the loop stops with at least two vertices in `q`; the final test is then false. If every choice is forced, the loop processes one vertex after another. Because all edges agree with the known permutation `nums`, no cycle can trap unprocessed vertices. Eventually the last forced vertex is removed and no new vertex remains, so the deque is empty and the result is true.

This also handles missing information. In Example 2, constraints from `[1, 2]` do not require `3` at all. In the graph, both `1` and `3` initially have indegree zero, so the deque immediately has multiple choices and the method returns false. This corresponds to the supersequence viewpoint: `[1, 2]` is shorter than `nums`, and the constraints do not force the omitted value into the answer.

For a concrete uniqueness example, take `nums = [1, 2, 3]` and `sequences = [[1, 2], [1, 3], [2, 3]]`. The edges are $1 \to 2$, $1 \to 3$, and $2 \to 3$. Initially only `1` has indegree zero. Processing `1` makes only `2` available because `3` still has the incoming edge from `2`. Processing `2` then makes `3` available. Every stage has one choice, so the unique order is `[1, 2, 3]`.

By contrast, with `[[1, 2], [1, 3]]`, processing `1` makes both `2` and `3` available. Their relative order is unconstrained, matching the two shortest supersequences `[1, 2, 3]` and `[1, 3, 2]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerating all supersequences:** Generating p:** - **Enumerating all supersequences:** Generating permutations or recursively trying every available next value can detect uniqueness, but the search may explore exponentially many orders. Kahn's algorithm detects the first branch point directly.
- **Checking only whether `nums` satisfies every row:** That proves `nums` is a valid supersequence, which is already guaranteed, but it does not prove that it is shortest or unique. The graph must show that every next value is forced.
- **Comparing consecutive pairs of `nums` against a set of observed relations:** Under this problem's guarantees, requiring every adjacent pair of `nums` to be implied can support another linear approach, but the graph formulation expresses transitive constraints and uniqueness uniformly and matches the exact solution.
- **Duplicate adjacent relations:** Repeated edges are harmless because indegree increments and decrements remain paired. Deduplicating them is optional and would require extra set storage.
- **A value weakly constrained or absent:** Such a value becomes available too early alongside another vertex, or otherwise fails to be forced. The deque then contains multiple choices and the answer is false.
- **A single value:** With `n = 1`, the only vertex is initially available, is processed, and leaves the deque empty, so the method returns true under the nonempty valid-sequence contract.
- **Cycles outside the stated contract:** In an unrestricted graph, a cycle could make `q` empty before all vertices were processed, and this exact final check would incorrectly accept it. Here every row is guaranteed to be a subsequence of the permutation `nums`, so all edges point forward in `nums` and a cycle is impossible.
- **Values outside `[1, n]`:** The code intentionally performs no validation before converting values to zero-based indices. The range guarantee is therefore part of the implementation's correctness.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V = n$ be the number of values and let $E$ be the total number of adjacent-pair occurrences across all rows. If the total number of listed elements is $S$, then $E \le S$, because a row of length $k$ contributes $k-1$ edges.
- **Auxiliary Space Complexity:** $O(V+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

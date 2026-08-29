# Guided Example: Find Champion II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [1, 2]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` teams numbered from `0` to $n - 1$ in a tournament; each team is also a node in a **DAG**.

The objective is to compute `0` from `{"n": 3, "edges": [[0, 1], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why zero indegree matches the definition

If a team has an incoming edge, the edge's source is stronger, so the team fails the champion condition immediately.

If a team has no incoming edge, no other team is declared stronger than it. The reference graph is a DAG representing the strength relations, including the stated transitive consistency. Thus it is a source of the strength ordering and satisfies the definition of a possible champion.

There can be several sources in a DAG. When that happens, none has a stronger incoming team, but the contract asks for a champion only if it is unique. The algorithm must count all zero entries rather than return the first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Exact final selection

`indeg.count(0)` scans the array and obtains the number of source teams. If that number is not one, the source returns `-1`.

If it is exactly one, `indeg.index(0)` finds and returns that sole source's label. Calling `index` only in this branch is safe because existence and uniqueness have already been established.

For $n=4$ with edges `[[0,2],[1,3],[1,2]]`, indegrees are `[0,0,2,1]`. Teams $0$ and $1$ both have zero indegree, so there is no unique champion and the result is `-1`.

For edges `[[0,1],[1,2]]`, indegrees are `[0,1,1]`. Only team $0$ is unmarked and is returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why reachability does not need to be computed

One might think a champion must reach every other node through directed paths. Under a unique-source DAG, every node is reachable from that source: if some node were unreachable, following its incoming predecessors backward within the finite DAG would eventually reach another zero-indegree source, contradicting uniqueness.

The local definition itself asks only that no stronger team exists, so incoming-edge marking is already direct. Transitive closure, topological sorting, and graph traversal are unnecessary for selecting the unique source.


Every returned team has indegree zero, so no edge identifies a stronger team. Uniqueness of the zero ensures there is no second champion candidate.

If a unique champion exists, it cannot have an incoming edge and therefore appears among the zero-indegree entries. Any other zero-indegree team would also have no stronger team and contradict uniqueness. Hence the count is exactly one and the algorithm returns the champion.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Topological sort:** It also begins with indegrees but maintaining a queue and removing nodes is unnecessary when only the number of initial sources matters.
- **Build an adjacency list:** Useful for reachability questions, but redundant here; every required update is determined directly by an edge destination.
- **Transitive closure:** Computing all strength relationships would cost much more and does not change which vertices have incoming edges.
- **No edges:** Every team has indegree zero. Return the sole team only when $n=1$; otherwise return `-1`.
- **One team:** Its indegree is zero, so it is the unique champion.
- **Duplicate edges:** The declared graph data normally treats edges as entries; duplicates would raise an indegree further but would not change zero-versus-positive classification.
- **Multiple zero-indegree teams:** Do not arbitrarily pick one. The required answer is `-1`.
- **Positive indegree magnitude:** Only whether it is zero matters; counting rather than Boolean marking remains simple and standard.
- **DAG guarantee:** Cycles are excluded. The zero-indegree logic still rejects cycle vertices, but an all-cycle graph could have no source and returns `-1`.
- **Why outgoing edges are unnecessary:** A champion may be connected to weaker teams indirectly. Its defining feature is absence of a stronger predecessor, which incoming-edge marking captures without counting victories.
- **Disconnected components:** A DAG with multiple disconnected components has at least one source in each, so it cannot have a unique champion unless only one component supplies all nodes through reachability.
- **Two linear scans of indegree:** `count` followed by `index` is still $O(n)$; combining them in one loop would only improve a constant factor.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $m$ be number of edges. Initializing the indegree array takes $O(n)$ time. Scanning edges takes $O(m)$. `count` and, in the successful case, `index` each take $O(n)$. Total time is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

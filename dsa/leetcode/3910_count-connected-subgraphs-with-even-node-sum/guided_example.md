# Guided Example: Count Connected Subgraphs with Even Node Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 1], "edges": [[0, 1], [1, 2]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an undirected graph with `n` nodes labeled from 0 to $n - 1$. Node `i` has a **value** of $\text{nums}[i]$, which is either 0 or 1. The edges of the graph are given by a 2D array `edges` where $\text{edges}[i] = [u_{i}, v_{i}]$ represents an edge between node $u_{i}$ and node $v_{i}$.

The objective is to compute `2` from `{"nums": [1, 0, 1], "edges": [[0, 1], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building the undirected adjacency lists

For each edge $[u,v]$, the source appends:

- $v$ to `g[u]`; and
- $u$ to `g[v]`.

This symmetric insertion lets DFS travel in either direction along every undirected edge.

The traversal later uses only edges whose endpoints are selected. It does not need to construct a new graph for every subset; the visited-mask initialization blocks excluded endpoints.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 1], "edges": [[0, 1], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerating every nonempty subset

The value

$$
m=(1\ll n)-1
$$

has its lowest $n$ bits set to one. For example, with $n=4$:

$$
m=1111_2.
$$

The loop `for sub in range(1, m + 1)` visits every nonzero $n$-bit mask exactly once. Starting at 1 excludes the empty subset, as required.

There are $2^n-1$ such candidates. This exponential enumeration is acceptable only because $n\le13$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Checking the even-sum condition

The input values are binary, but ordinary summation is sufficient:



The bit expression selects exactly the nodes contained in `sub`. If `s % 2` is one, the sum is odd and the subset cannot count, so the source skips connectivity work.

If the sum is even, the subset still has to pass the induced-connectivity condition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 1], "edges": [[0, 1], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bitmask adjacency traversal:** Store each node's neighbors as an integer mask and expand a frontier with bit operations. This can avoid scanning excluded adjacency-list entries and better supports the manifest's $O(n2^n)$ characterization.
- **Enumerate connected subsets directly:** Frontier-based generation may skip disconnected masks but requires careful duplicate prevention and still has exponential worst-case behavior.
- **Disjoint-set rebuild per subset:** Unioning selected edges for every mask is more cumbersome and has similar or worse edge-scanning cost.
- **Empty subset:** It is excluded by starting enumeration at mask 1.
- **Singleton with value zero:** Its induced graph is connected and its sum is even, so it counts.
- **Singleton with value one:** It is connected but skipped because its sum is odd.
- **Disconnected original graph:** A subset can still count if all its selected nodes lie in and connect within one component.
- **Paths through excluded nodes:** They do not establish induced connectivity; premarking excluded bits prevents DFS from using them.
- **All zero values:** Every subset passes parity, exposing the worst-case connectivity-running time.
- **All one values:** Exactly even-cardinality subsets pass the parity filter, after which connectivity is still checked.
- **No edges:** Only zero-valued singleton subsets can count; every larger induced subgraph is disconnected.
- **Complete graph:** Every nonempty subset is connected, so counting reduces to even value-sum masks, but the source still scans adjacency lists.
- **Recursion safety:** DFS depth is at most 13 under the contract, far below Python's normal recursion limit.
- **Manifest mismatch:** Actual adjacency storage is $O(n+E)$ and dense-graph time is $O((n+E)2^n)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n 2^n)$. Let $n$ be the number of nodes and $E$ the number of edges.
- **Auxiliary Space Complexity:** $O(n+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

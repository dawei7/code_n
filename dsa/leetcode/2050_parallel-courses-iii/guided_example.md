# Guided Example: Parallel Courses III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "relations": [[1, 3], [2, 3]], "time": [3, 2, 5]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where $\text{relations}[j] = [\text{prevCourse}_{j}, \text{nextCourse}_{j}]$ denotes that course $\text{prevCourse}_{j}$ has to be completed **before** course $\text{nextCourse}_{j}$ (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where $\text{time}[i]$ denotes how many **months** it takes to complete the $(i+1)^th$ course.

The objective is to compute `8` from `{"n": 3, "relations": [[1, 3], [2, 3]], "time": [3, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model prerequisites as a directed acyclic graph

Each course is a vertex. Relation `[a,b]` creates a directed edge from prerequisite `a` to dependent course `b`.

The source converts one-based labels to zero-based indices, appends `b-1` to `g[a-1]`, and increments `indeg[b-1]`. The indegree records how many prerequisites of each course have not yet been topologically processed.

The graph is guaranteed acyclic, so every course can eventually enter a topological order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "relations": [[1, 3], [2, 3]], "time": [3, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Unlimited parallelism turns the objective into a critical path

Courses with satisfied prerequisites can run simultaneously. A dependent course cannot start until all its prerequisites finish, so its earliest start is the latest completion time among them.

Define `f[i]` as the earliest possible completion month of course `i`. For a source course with no prerequisites, it can start at month zero and finishes at `time[i]`.

For an edge from `i` to `j`, completing `j` through that prerequisite chain would take

`f[i] + time[j]`.

Because all prerequisites must be finished, `f[j]` is the maximum of this value over every incoming prerequisite.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Courses with satisfied prerequisites can run simultaneously.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize all immediately available courses

The source scans `zip(indeg, time)`. Every course whose indegree is zero is placed in queue `q`, assigned `f[i]=time[i]`, and considered for global `ans`.

All such courses can begin together at month zero. The queue order among them does not affect completion times because their dependency subgraphs are handled through maxima.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "relations": [[1, 3], [2, 3]], "time": [3, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Memoized DFS:** Compute the longest duration p:** - **Memoized DFS:** Compute the longest duration path starting or ending at each course; also $O(N+M)$ but recursion depth can be large.
- **Ordinary shortest path:** Wrong objective; prerequisites impose a longest critical path, not a shortest route.
- **Sum all prerequisite finishes:** Incorrect because prerequisites run concurrently.
- **No relations:** Every course starts at zero and the answer is the largest individual duration.
- **One course:** Its own duration is the answer.
- **Several source courses:** All are initialized and run in parallel.
- **Several prerequisites:** Their maximum finish controls the dependent start.
- **Several outgoing edges:** One completed course can unlock timing updates for many dependents.
- **Duplicate relations:** Excluded by the contract; otherwise indegree and adjacency would both duplicate consistently but unnecessarily.
- **Cycle:** Excluded by the DAG guarantee.
- **Independent components:** They execute in parallel, and the slower component determines `ans`.
- **Input preservation:** Only new graph and state arrays are mutated.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+M)$. Let $N$ be the number of courses and $M$ the number of prerequisite relations. Graph construction takes $O(N+M)$ initialization time. Kahn's process enqueues each course once and scans each directed edge once, so total time is $O(N+M)$.
- **Auxiliary Space Complexity:** $O(N+M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

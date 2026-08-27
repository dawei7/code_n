# Guided Example: Sort Array Using Prefix Reversals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 0, 1], "pre": [2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers in the range `[0, n - 1]`.

The objective is to compute `2` from `{"nums": [2, 0, 1], "pre": [2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why tuples represent states

The source converts both the input and target to tuples:



Tuples are immutable and hashable, so they can be keys in the visited set. A list cannot be inserted into a set.

The conversion also ensures neighbor construction creates new states without mutating the caller's `nums`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 0, 1], "pre": [2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Already sorted input

If `start==target`, zero operations are required. The source returns immediately before constructing the queue.

This branch is also relevant to the stored dependency defect: an already sorted call would not reach `deque`, although ordinary module loading still fails earlier on the unresolved annotation name.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `start==target`, zero operations are required.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generating one neighbor

For allowed length `x`:



The pieces mean:

- `state[:x]` is the prefix;
- `[::-1]` reverses that prefix;
- `state[x:]` is the untouched suffix;
- tuple concatenation forms the complete next permutation.

The contract guarantees `1\le x\le n`. Length one produces the same state, which the visited set immediately rejects.

Prefix reversal is its own inverse: applying the same length twice restores the original state. This symmetry is not required by BFS, but it confirms the state graph has undirected connections even though neighbors are generated in one direction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 0, 1], "pre": [2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Greedy pancake sorting:** It assumes access to:** - **Greedy pancake sorting:** It assumes access to useful reversal lengths and does not guarantee the minimum number under an arbitrary `pre` set.
- **- **Depth-first search:** DFS can establish reacha:** - **Depth-first search:** DFS can establish reachability but does not naturally return the shortest number of unit-cost operations without additional distance handling.
- **- **Dijkstra's algorithm:** All transitions cost o:** - **Dijkstra's algorithm:** All transitions cost one, so BFS provides the same shortest distances with less overhead.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Pqn)$. Let `P=n!` be the maximum number of permutation states and `q=\lvert pre\rvert`.
- **Auxiliary Space Complexity:** $O(Pn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

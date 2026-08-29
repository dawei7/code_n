# Guided Example: Open the Lock

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"deadends": ["0201", "0101", "0102", "1212", "2002"], "target": "0202"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The objective is to compute `6` from `{"deadends": ["0201", "0101", "0102", "1212", "2002"], "target": "0202"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model lock combinations as an unweighted graph

Each four-digit display is a graph vertex. Turning one wheel one slot produces an edge to another display. Every move costs exactly one turn, so the minimum number of turns is an unweighted shortest-path distance from `"0000"` to `target`.

Breadth-first search is the correct tool because it explores vertices by increasing edge distance.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"deadends": ["0201", "0101", "0102", "1212", "2002"], "target": "0202"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate exactly eight neighbors

For each of four wheel positions, the helper creates two states:

- One after rotating the digit down by one.
- One after rotating it up by one.

The wrap rules are explicit: zero rotated downward becomes nine, and nine rotated upward becomes zero.

The helper temporarily changes one character in a list, joins it into a string for each neighbor, then restores the original character before moving to the next wheel. Therefore every returned state differs from the input at exactly one wheel.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Treat deadends and visited states together

The set `s` begins with all deadend combinations. A state in this set must never be enqueued.

After the starting-state checks, `"0000"` is added to the same set, and every newly enqueued state is added immediately. The set thus means “blocked or already discovered.” These two categories need the same BFS action: never enter them again.

Marking at enqueue time prevents the same combination from being added through multiple parents in one layer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"deadends": ["0201", "0101", "0102", "1212", "2002"], "target": "0202"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bidirectional BFS:** Search simultaneously from start and target and expand the smaller frontier. It can greatly reduce explored states while preserving shortest paths.
- **Depth-first search:** DFS can find a route but does not naturally guarantee the minimum number of moves.
- **Dijkstra’s algorithm:** It works, but all edges have equal weight, so a priority queue is unnecessary overhead.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d + 10^w w)$. For `w` wheels there are at most `10^w` displays, plus `d` deadends. Each visited display considers `2w` moves.
- **Auxiliary Space Complexity:** $O(d + 10^w)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

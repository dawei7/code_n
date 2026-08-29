# Guided Example: Robot Room Cleaner

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"robot": {"room": [[1]], "row": 0, "col": 0, "direction": 0}}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are controlling a robot that is located somewhere in a room. The room is modeled as an `m x n` binary grid where `0` represents a wall and `1` represents an empty slot.

The objective is to compute `1` from `{"robot": {"room": [[1]], "row": 0, "col": 0, "direction": 0}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The robot cannot inspect the room grid, learn its absolute row and column, or teleport back to an earlier cell. It can only sense whether a forward move succeeds. The solution nevertheless performs an ordinary depth-first search by creating its own coordinate system relative to the starting position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"robot": {"room": [[1]], "row": 0, "col": 0, "direction": 0}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The starting cell is called `(0, 0)`, regardless of its hidden grid coordinates. Direction numbers are

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `0` for up,
- `1` for right,
- `2` for down,
- `3` for left.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"robot": {"room": [[1]], "row": 0, "col": 0, "direction": 0}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative DFS with an explicit stack:** It can avoid Python recursion depth, but each stack frame must preserve both exploration direction and the physical route needed to restore the robot. The recursive entry/exit contract expresses that bookkeeping naturally.
- **Breadth-first search:** A queue can plan graph exploration, but the physical robot still has to travel between queued cells and cannot teleport. DFS matches physical backtracking much more directly.
- **Wall-following alone:** Always turning at walls can traverse some boundaries but does not reliably explore every branch in an arbitrary connected room. The visited-coordinate DFS explicitly returns to branch points.
- **Unknown absolute location:** Relative `(0, 0)` coordinates are sufficient. Translation of every coordinate by the hidden start position would describe the same adjacency graph.
- **Unknown dimensions:** The algorithm stops by exhausting reachable neighbors, so it never needs `m` or `n`.
- **Failed move:** The robot remains in place, exactly as the parent loop assumes before its unconditional right turn.
- **Previously visited neighbor:** The algorithm does not physically enter it. It simply rotates to the next direction, avoiding cycles.
- **Single-cell room:** The cell is cleaned once, four wall checks fail, and four right turns restore the initial orientation.
- **Long corridor:** Recursion depth can be linear in the number of cells. The asymptotic space bound includes this stack depth, and a language recursion limit may motivate an explicit-stack implementation.
- **Backtracking move must succeed:** It traverses the same open edge by which the child was entered; room geometry does not change, so no obstacle can appear on that return edge.
- **Clean exactly once versus at least once:** `vis` ensures each cell's DFS call and `clean()` occur once. The requirement only needs every cell cleaned, but avoiding repeated cleaning also limits work.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $c$ be the number of accessible cells. Each accessible cell enters `dfs` once because it is added to `vis` before neighbors are explored. Each call checks exactly four directions, and every check performs a constant number of robot operations apart from a recursive traversal charged to another cell. Total time is therefore $O(c)$.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Build a Matrix With Conditions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"k": 3, "rowConditions": [[1, 2], [3, 2]], "colConditions": [[2, 1], [3, 2]]}`
- **Required output:** `[[0, 0, 1], [3, 0, 0], [0, 2, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `k`. You are also given:

The objective is to compute `[[0, 0, 1], [3, 0, 0], [0, 2, 0]]` from `{"k": 3, "rowConditions": [[1, 2], [3, 2]], "colConditions": [[2, 1], [3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate row constraints from column constraints

Each number `1` through `k` needs one row and one column. Row conditions restrict only relative row positions; column conditions restrict only relative column positions. These two dimensions can be solved independently.

A condition `[a, b]` in `rowConditions` means `a` must precede `b` in a top-to-bottom ordering. A column condition means the same precedence in a left-to-right ordering. Both are directed-graph topological-order problems.

Once a valid row order and valid column order are known, number `v` can be placed at the intersection of its row-order position and column-order position. Independent valid orders cannot conflict because a matrix cell is uniquely determined by one row and one column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"k": 3, "rowConditions": [[1, 2], [3, 2]], "colConditions": [[2, 1], [3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a directed graph for one condition set

The helper `f(cond)` creates adjacency lists `g` and an indegree array. For every condition `[a, b]`, it adds directed edge `a -> b` and increments `indeg[b]`.

An indegree counts how many required predecessors have not yet been placed. Values with indegree zero can safely appear next because no condition requires another unprocessed value before them.

All numbers `1` through `k` must be included even if they never appear in a condition. The initial queue is built from the full numeric range and therefore includes unconstrained values with indegree zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Produce a topological order with Kahn's algorithm

The queue begins with every zero-indegree value. Repeatedly, the helper removes a value `i`, appends it to `res`, and conceptually deletes all outgoing edges. For each neighbor `j`, it decrements `indeg[j]`. When that indegree reaches zero, all of `j`'s prerequisites have been processed and `j` enters the queue.

The extra loop over `range(len(q))` processes one queue layer at a time. Layer separation is not necessary for producing a topological order, but it does not change correctness; all nodes already in the queue are currently legal choices.

Duplicate conditions are also safe. They create duplicate adjacency entries and increment indegree multiple times. When their source is processed, every duplicate edge is removed and decrements the matching count, so the target becomes ready at the proper moment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0, 1], [3, 0, 0], [0, 2, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"k": 3, "rowConditions": [[1, 2], [3, 2]], "colConditions": [[2, 1], [3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0, 1], [3, 0, 0], [0, 2, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **DFS topological sort:** Three-color visitation can detect cycles and append nodes in reverse finish order. It has the same asymptotic bounds but recursive depth can be a concern.
- **One combined graph of row and column constraints:** Row and column positions are independent dimensions; merging them would impose relationships the problem never requires.
- **Cycle in only one dimension:** No matrix exists even if the other dimension has a valid order.
- **Unconstrained value:** It begins with zero indegree and is placed somewhere valid in both orders.
- **Duplicate condition:** Parallel edges balance their duplicated indegree increments and do not change the logical order.
- **Multiple valid orders:** Queue order may choose any; the problem accepts any valid matrix.
- **All zeros except `k` cells:** Initialization supplies zeros, and exactly one assignment is made per value.
- **Independent coordinate maps:** A value's row position does not need to match its column position.
- **Self-condition:** The contract excludes `a == b`; such a condition would be an immediate cycle.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k^2)$. Let $r$ and $c$ be the counts of row and column conditions. Each topological sort initializes $O(k)$ state and processes every directed edge once, taking $O(k+r)$ and $O(k+c)$ time respectively.
- **Auxiliary Space Complexity:** $O(k^2 + r + c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Moving Stones Until Consecutive

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": 1, "b": 2, "c": 5}`
- **Required output:** `[1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are three stones in different positions on the X-axis. You are given three integers `a`, `b`, and `c`, the positions of the stones.

The objective is to compute `[1, 2]` from `{"a": 1, "b": 2, "c": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort the three positions conceptually

The input names `a`, `b`, and `c` do not indicate left-to-right order. The method derives:

- `x` as the minimum position.
- `z` as the maximum position.
- `y = a + b + c - x - z` as the remaining middle position.

The three positions are distinct, so this guarantees `x < y < z`. Only their sorted gaps matter to the game.

Let the left gap be `g_1 = y - x` and the right gap be `g_2 = z - y`. The stones are consecutive exactly when both gaps equal one, which is equivalent to `z - x = 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": 1, "b": 2, "c": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Already finished

Three distinct integer positions cannot have span smaller than two. Therefore, if `z - x` is not greater than two, it must equal two, and the positions are `x, x + 1, x + 2`.

No unoccupied integer lies between the endpoints, so no legal move exists. The initialized values `mi = mx = 0` are returned.

This explains the outer condition `if z - x > 2`. All nonterminal configurations have a larger span.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Minimum moves when one gap is small

The test `y - x < 3 or z - y < 3` means at least one gap has size one or two.

If `y - x = 1`, the left pair is already consecutive. Move the right endpoint `z` to `y + 1`. Because the overall configuration was not already complete, `y + 1 < z`, so the target lies strictly between the old endpoints and is unoccupied. The result is three consecutive stones.

If `y - x = 2`, position `x + 1` is the single hole between the left pair. Move endpoint `z` into that hole. The new positions are `x, x + 1, x + 2`.

The two symmetric arguments apply when the right gap is one or two: move the left endpoint next to the right pair or into its one-cell hole.

Thus at least one move is necessary because the current state is nonterminal, and one move is sufficient. The minimum is one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": 1, "b": 2, "c": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search over configurations:** Enumerating every legal move can find the minimum for small coordinates, but state count grows and it gives no simple maximum proof. Gap formulas solve both objectives directly.
- **Recursive game simulation:** Exploring move sequences repeats configurations and obscures why maximum play is finite. The empty-position potential gives an exact bound.
- **Sort a three-element list:** `sorted([a, b, c])` is equally correct and still constant time. The exact solution derives the middle through the sum to avoid allocating the temporary list.
- **Input already sorted or reversed:** Minimum, maximum, and total-sum recovery produce the same `x, y, z` regardless of argument order.
- **Three consecutive positions:** Span equals two, so both answers remain zero.
- **One adjacent pair:** A gap of one guarantees a one-move finish by placing the opposite endpoint beside that pair.
- **A one-position hole:** A gap of two also gives a one-move finish by filling the hole with the opposite endpoint.
- **Both gaps at least three:** One move is impossible because whichever endpoint remains paired with the middle is still too far away; exactly two moves suffice.
- **Highly unbalanced gaps:** Minimum may still be one if the small gap is one or two, while maximum counts holes across both gaps.
- **Strictly interior target rule:** The one-move constructions always place the moved endpoint between the old endpoints, not outside or on an occupied location.
- **Dynamic endpoints:** After a move, the lowest and highest stones may be different physical stones. The maximum construction reasons about positions, not stone identities.
- **Why maximum is not the larger gap alone:** Empty positions in both gaps can be consumed one at a time, so the total `(g_1 - 1) + (g_2 - 1)` equals `z - x - 2`.
- **Distinct-value guarantee:** It ensures strict order and prevents zero gaps. Duplicate positions would not describe three separate stones under the source contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method computes one minimum, one maximum, several additions and subtractions, and a constant number of comparisons. It does not loop over the coordinate range. Time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

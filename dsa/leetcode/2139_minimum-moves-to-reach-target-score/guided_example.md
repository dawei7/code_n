# Guided Example: Minimum Moves to Reach Target Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"target": 5, "maxDoubles": 0}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a game with integers. You start with the integer `1` and you want to reach the integer `target`.

The objective is to compute `4` from `{"target": 5, "maxDoubles": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Handle states where no choice remains

If `target == 1`, the starting score has already been reached, so the method returns zero.

If `maxDoubles == 0`, no reverse halving is permitted. The only possible forward plan is to increment from one to `target`, requiring `target - 1` moves. Returning that value immediately is important: it avoids a long recursive chain of individual subtractions when the remaining answer can be computed directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"target": 5, "maxDoubles": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Undo a double whenever the target is even

If `target` is even and a double remains, the source returns `1 + minMoves(target >> 1, maxDoubles - 1)`.

The expression `target >> 1` equals integer division by two for the positive target. The added one counts the reverse halving, which corresponds to one forward doubling.

Why is using the double greedy-optimal? To reach an even value $t$ without making the last move a double, the last move must be an increment from $t-1$. In reverse, that means subtracting one to an odd value. That odd value still cannot be halved, so another subtraction would be needed before any halving becomes possible. Directly halving even $t$ reaches $t/2$ in one move, while refusing it requires at least two reverse moves merely to reach $(t-2)/2=t/2-1$. Spending an available double at the larger even value cannot require more moves than postponing it.

Another way to see the benefit is that a forward double magnifies all progress accumulated before it. In an optimal forward plan, available doubles should be used as late as needed relative to increments; backward traversal encounters those high-impact final doubles first.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Make an odd target divisible by two

When `target` is odd and greater than one, it cannot be the result of a forward doubling. Therefore the final forward move must have been an increment from `target - 1`. The only valid reverse action is `1 + minMoves(target - 1, maxDoubles)`.

This subtraction makes the target even. If a double remains, the next recursive call will halve it. Consequently, while doubles are available, each binary digit is handled with at most one subtraction followed by one halving.

For `target = 19` and `maxDoubles = 2`, the reverse path begins $19\to18\to9\to8\to4$. Those are four moves: subtract, halve, subtract, halve. The double budget is then exhausted, so reaching one from four costs three more decrements. Total moves are seven.

For `target = 10` with four available doubles, the path is $10\to5\to4\to2\to1$, taking four moves. Read forward, this becomes $1\to2\to4\to5\to10$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"target": 5, "maxDoubles": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative backward greedy:** Repeatedly halve even targets while budget remains, decrement odd targets, and finally add `target - 1`. This preserves the recurrence and time bound while eliminating recursion-stack space.
- **Breadth-first search from one:** BFS can find a shortest path but explores many scores and is infeasible near a target of $10^9$. The inverse operations expose a deterministic greedy path.
- **Forward greedy doubling whenever possible:** Doubling too early can overshoot or leave costly increments. The backward view knows exactly whether the last operation can be a double.
- **Dynamic programming over all scores:** Storing answers through `target` costs $O(\textit{target})$ time and space, far more than the logarithmic reduction.
- **Target equals one:** The first base case returns zero even if doubles are available, because no move should be made.
- **Zero double budget:** The second base case returns `target - 1` directly, including for very large targets.
- **Even target with budget:** Halving consumes exactly one double through `maxDoubles - 1`.
- **Odd target with budget:** Subtracting one does not consume a double because it reverses an increment.
- **More doubles than necessary:** The recursion stops at target one; unused capacity is allowed because the limit is “at most.”
- **Target two:** With a double, one halving reaches one in one move. Without a double, one increment is still one move.
- **Powers of two:** With enough doubles, repeated halving uses exactly $\log_2(\textit{target})$ moves and no decrements.
- **Stack accounting:** The implementation does not use a list or map, but recursive frames are auxiliary memory and must not be described as constant space.
- **Positive-target guarantee:** Right shifting is safe and subtraction never needs to go below one because the target is always at least one.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log \textit{target})$. While a double is available, an even target is halved immediately. An odd target is decremented once and then becomes even. Thus each halving is accompanied by at most one preceding decrement. There can be at most $O(\log \textit{target})$ halvings before the value reaches one, and the method stops in constant time as soon as the double budget reaches zero. Total time is $O(\log \textit{target})$.
- **Auxiliary Space Complexity:** $O(\log \textit{target})$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

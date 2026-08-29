# Guided Example: Find the Winner of an Array Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 1, 3, 5, 4, 6, 7], "k": 2}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr` of **distinct** integers and an integer `k`.

The objective is to compute `5` from `{"arr": [2, 1, 3, 5, 4, 6, 7], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the front element as the current champion

In every round, the element at the front competes against the next element. The larger one stays in front, while the smaller one moves behind all still-waiting players.

Call the front winner `mx`. Initially `mx = arr[0]`. The stored solution then visits the original remaining elements in order through `arr[1:]`. Each visited `x` is the next challenger that has not yet faced the current champion.

The important simplification is that a loser need not actually be appended to a queue. Before the global maximum first becomes champion, every element that loses moves behind all unprocessed original challengers. It cannot return to the front before those challengers have played. Once the global maximum becomes champion, it can never lose, so delayed losers can never change the eventual winner.

Therefore, a single left-to-right pass reproduces every relevant championship change without physically rotating the array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 1, 3, 5, 4, 6, 7], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the consecutive-win count

`cnt` records the current champion's consecutive victories.

If `mx < x`, the challenger is larger and wins this round. It becomes the new champion through `mx = x`. Its streak is exactly one because the just-completed round is its first consecutive win, so the code assigns `cnt = 1`.

Otherwise `mx > x` because all values are distinct. The champion wins again and `cnt += 1` extends its streak.

There is no equality branch to define because the distinct-values guarantee prevents a tied round.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why breaking at k victories is correct

After each simulated relevant round, the code checks `cnt == k`. At that moment `mx` has won exactly $k$ consecutive rounds, so the game ends under the stated rule. Breaking the loop and returning `mx` yields the actual winner.

The check uses equality rather than greater-than-or-equal because `cnt` increases by one per round. It cannot jump over $k$.

For `k = 1`, the first comparison immediately identifies the winner: either the initial champion defeats `arr[1]`, or that challenger replaces it. The count becomes one and the loop stops.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 1, 3, 5, 4, 6, 7], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal deque simulation:** It mirrors the rules directly but uses $O(N)$ queue space; stopping when the maximum becomes champion is necessary to avoid dependence on huge $k$.
- **Rotate a Python list:** Removing and appending can make rounds expensive because front deletion shifts elements.
- **Index-based champion pass:** It is algorithmically identical and avoids the linear list slice, achieving true $O(1)$ auxiliary space.
- **k equals one:** The winner of the first comparison is returned immediately.
- **k larger than the array length:** The pass reaches the global maximum and returns it without simulating all required future wins.
- **Initial element is maximum:** It defeats every challenger and is returned either when its streak reaches $k$ or when the pass ends.
- **Maximum appears later:** Every earlier champion eventually loses when the scan reaches that maximum.
- **Strictly increasing array:** Each challenger becomes the new champion with streak one; the final element is the global maximum.
- **Strictly decreasing array:** The first element remains champion throughout.
- **Distinctness:** It removes the need for a tie rule and makes the `else` branch a strict champion victory.
- **Count reset:** A new champion starts at one, not zero, because becoming champion happened by winning the current round.
- **No explicit maximum call:** Completing the running comparisons computes the maximum naturally, so a separate `max(arr)` pass is unnecessary.
- **Guaranteed winner:** Once the maximum is champion, repeated victories ensure termination for every positive finite $k$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length. At most $N-1$ challengers are examined, each with constant work, so time is $O(N)$. Early termination can use fewer iterations, but the worst case still scans the array.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Find the Winner of the Circular Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "k": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the $$i^{\text{th}}$$ friend brings you to the $(i+1)^th$ friend for $1 \le i < n$, and moving clockwise from the $$n^{\text{th}}$$ friend brings you to the $1^st$ friend.

The objective is to compute `3` from `{"n": 5, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the game after the first elimination

This is the Josephus problem. After the first friend is removed, the remaining friends still form the same kind of circular game with one fewer participant and the same step size $k$.

The only complication is translating the winner's position from that smaller circle back to the original numbering.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Base case

With one friend, that friend wins. The protected recursive function returns one for `n == 1`.

This is a one-based result because the problem labels friends from 1.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | With one friend, that friend wins.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the smaller circle is renumbered

In a circle of $n$ friends, counting from friend 1 removes the $k$th counted position, wrapping as needed.

The next round begins immediately clockwise from the removed friend. If we conceptually renumber that next friend as position 1 of a new circle, the remaining game is exactly the problem for $n-1$ friends.

Suppose the recursive call returns one-based winner position $p$ in this rotated smaller circle. Mapping it back to the original circle shifts by $k$ positions with wraparound.

The exact source computes

`ans = (k + p) % n`

and returns `n` when that remainder is zero, otherwise `ans`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative Josephus recurrence:** It attains th:** - **Iterative Josephus recurrence:** It attains the manifest's $O(n)$ time and $O(1)$ space without changing the mathematics.
- **List simulation:** Repeated middle deletion can cost $O(n^2)$ time and requires $O(n)$ storage.
- **Queue rotation:** It models the rules clearly but takes $O(nk)$ time and $O(n)$ space.
- **`n = 1`:** The sole friend wins immediately.
- **`k = 1`:** Friends leave in current order, so friend $n$ wins.
- **Remainder zero:** It represents one-based label $n$, which the explicit conditional restores.
- **Large `k` relative to remaining size:** Modulo handles multiple wraps.
- **One-based labels:** The zero remainder conversion prevents returning invalid friend zero.
- **Recursive depth:** Safe under the current constraint but not constant space.
- **No elimination-order storage:** Only the final survivor is required.
- **Clockwise rotation:** Renumbering begins at the friend after the eliminated one, which creates the $+k$ shift.
- **Original start friend:** The top-level numbering already begins at friend 1.
- **Deterministic game:** No tie or choice affects the recurrence.
- **Input scalars:** The function mutates no external state.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The method makes one recursive call for every circle size from $n$ down to one. Each level performs constant arithmetic, so time complexity is $O(n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

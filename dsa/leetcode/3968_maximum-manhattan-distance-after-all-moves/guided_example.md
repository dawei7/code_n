# Guided Example: Maximum Manhattan Distance After All Moves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"moves": "L_D_"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `moves` consisting of the characters `'U'`, `'D'`, `'L'`, `'R'`, and `'_'`.

The objective is to compute `4` from `{"moves": "L_D_"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why one wildcard can improve the distance by at most one

One underscore becomes one unit move. If it changes one coordinate from `a` to `a+1` or `a-1`, the absolute value of that coordinate changes by at most one:

$$
\bigl\lvert\,\lvert a\pm1\rvert-\lvert a\rvert\,\bigr\rvert\le1.
$$

The other coordinate does not change. Therefore one wildcard can increase the final Manhattan distance by no more than one. With `z` wildcards, no assignment can improve the fixed displacement by more than `z`:

$$
\text{maximum distance}
\le
\lvert x\rvert+\lvert y\rvert+z.
$$

This is also an application of the triangle inequality. Every wildcard step has Manhattan length one, so adding all wildcard displacement vectors can increase the norm by at most the sum of their lengths.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"moves": "L_D_"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the upper bound is always attainable

At least one direction can be chosen so that each wildcard extends the displacement rather than canceling it.

- If `x>0`, assign every wildcard to the move that increases `x`.
- If `x<0`, assign every wildcard to the move that makes `x` more negative.
- If `x=0` but `y\ne0`, extend `y` in its existing sign.
- If both coordinates are zero, choose any one direction for every wildcard.

In each case, every underscore increases one coordinate's absolute value by exactly one and never decreases the other. After all `z` assignments, the distance is exactly

$$
\lvert x\rvert+\lvert y\rvert+z.
$$

Because this construction reaches the previously established upper bound, it is optimal.

The wildcards do not have to use different directions. The contract says they may be replaced independently, which permits assigning all of them to the same direction. Independence gives freedom; it does not impose variety.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At least one direction can be chosen so that each wildcard e... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the route order does not create an extra opportunity

Manhattan distance is measured only after all commands. Vector addition is commutative, so the final displacement from a collection of moves is independent of the order in which their vectors are added. A route might temporarily travel farther from the origin and later return, but temporary distances are irrelevant to the requested final value.

For example, fixed moves `U` and `D` cancel regardless of where underscores appear between them. Once all fixed commands are summarized as `x=0` on that axis, assigning all wildcards in one direction yields their full contribution.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"moves": "L_D_"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try all wildcard assignments:** With `z` under:** - **Try all wildcard assignments:** With `z` underscores there are `4^z` possible replacements. The triangle-inequality upper bound and matching construction collapse that exponential search to one count.
- **- **Dynamic programming over reachable coordinates:** - **Dynamic programming over reachable coordinates:** Tracking all positions after each command can require quadratic or larger state. Only the most distant final position is needed, and every wildcard can be made to contribute one to the fixed Manhattan norm.
- **- **Greedily choose while following the route:** O:** - **Greedily choose while following the route:** One may assign each underscore to increase the current distance at that moment, but temporary position is unnecessary. Summarizing fixed displacement first gives a simpler global argument.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `moves`. The loop reads all `n` characters and performs constant work for each one, so time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

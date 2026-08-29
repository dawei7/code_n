# Guided Example: Maximum Number of People That Can Be Caught in Tag

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"team": [0, 1, 0, 1, 0], "dist": 3}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a game of tag with your friends. In tag, people are divided into two teams: people who are "it", and people who are not "it". The people who are "it" want to catch as many people as possible who are not "it".

The objective is to compute `2` from `{"team": [0, 1, 0, 1, 0], "dist": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the task as ordered matching

Every person who is "it" can catch at most one zero, and every zero can be caught at most once. A pair is legal when their indices differ by at most `dist`. The goal is a maximum matching between two ordered lists of positions whose feasible ranges are intervals.

The exact source scans "it" people from left to right with loop index `i` and maintains pointer `j` to the earliest zero that has not been skipped or matched.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"team": [0, 1, 0, 1, 0], "dist": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Discard positions that can never help

Before matching an "it" position `i`, the while loop advances `j` while either:

- `team[j]` is one, so that position is not a catchable person; or
- `i - j > dist`, so the zero lies too far to the left.

A too-far-left zero cannot be caught by the current person or by any later "it" person, because later indices only increase the distance to that zero. Discarding it permanently is safe.

Previously caught zeroes are also absent because the code increments `j` immediately after every successful match.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Do not discard a zero that is too far right

After the cleanup, `j` is the earliest remaining zero. It might lie within distance of `i`, or it might be farther than `i + dist`.

If `abs(i - j) <= dist`, the pair is legal. The source increments `ans` and `j`, consuming that zero.

If the zero is too far right, the current "it" person cannot catch it, but a later "it" person may be closer. The code therefore leaves `j` unchanged and simply continues the outer scan. This asymmetry between too-far-left and too-far-right positions is essential.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"team": [0, 1, 0, 1, 0], "dist": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Collect zero and one positions first:** Two-pointer matching on those arrays is equally linear but uses $O(N)$ extra space.
- **Bipartite matching algorithm:** General-purpose and correct, but far heavier than necessary for interval-ordered neighbors.
- **For each "it," search from scratch:** Can revisit positions and degrade to $O(N^2)$.
- **Match a later zero before an earlier feasible zero:** May strand the earlier zero; the exchange proof supports earliest-first matching.
- **No zeroes:** The pointer skips all ones and the answer remains zero.
- **No "it" people:** The outer loop never attempts a match.
- **`dist` covers the whole array:** The answer is the smaller count of ones and zeroes.
- **Zero too far left:** Discard permanently because later "it" positions are even farther right.
- **Zero too far right:** Preserve it because a later "it" position may reach it.
- **Exact boundary distance:** Allowed because the comparison uses `<= dist`.
- **Alternating teams:** The greedy scan consumes nearby zeroes in order.
- **One-to-one rule:** Incrementing `j` after success prevents double-catching.
- **Input preservation:** The algorithm reads `team` and does not mark caught people in it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the team length. The outer loop examines all $N$ positions. Pointer `j` only moves forward from zero to at most $N$, so all while-loop advances total $O(N)$ across the entire execution. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

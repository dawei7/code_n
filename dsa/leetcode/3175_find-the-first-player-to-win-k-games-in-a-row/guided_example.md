# Guided Example: Find The First Player to win K Games in a Row

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"skills": [4, 2, 6, 3, 9], "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A competition consists of `n` players numbered from `0` to $n - 1$.

The objective is to compute `2` from `{"skills": [4, 2, 6, 3, 9], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compress the queue process into champion versus new challengers

The winner stays at the front. During the first pass through original players, current front champion faces players 1, 2, ..., in that order. A losing challenger goes behind everyone not yet seen, so it cannot affect who faces the front next during this pass.

Variable `i` is the original index of current champion, and `cnt` is that champion's consecutive win count.

For challenger `j`:

- if `skills[j]` is greater, challenger becomes champion and has just won one game, so `i=j` and `cnt=1`;
- otherwise, current champion wins again and `cnt` increments.

When `cnt == k`, this is the first time anyone reaches the threshold, so the loop stops.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"skills": [4, 2, 6, 3, 9], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only one scan is needed

If no player reaches the needed streak before every original challenger has appeared, the global maximum-skill player must now be champion. It defeated the previous champion when encountered and cannot ever lose afterward.

All later queue games therefore have that same winner, so the eventual competition winner is already known even if its current streak is below a very large $k$.

The code caps

`k = min(k, n - 1)`.

No nonmaximum player can win $n-1$ consecutive games without facing and losing to the unique global maximum. The maximum player is the answer for any threshold at least $n-1$. The cap allows the same scan logic and does not change the winning identity.

If the maximum appears late, its streak may still be below $n-1$ when the loop ends. Returning `i` remains correct because it is the maximum and will win forever.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why n minus one is the decisive threshold

Before the queue begins repeating opponents, at most $n-1$ games are needed for the front champion to face every other original player. Anyone who wins all $n-1$ of those comparisons must have beaten the global maximum and therefore must be the global maximum.

A nonmaximum champion can accumulate some wins, but the unique larger maximum is still among the unseen challengers or will return after being undefeated; the nonmaximum cannot establish a streak of $n-1$ against all other players.

Thus for any requested $k\ge n-1$, winner identity is determined solely by maximum skill, and reducing the numeric threshold does not change that identity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"skills": [4, 2, 6, 3, 9], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal deque simulation:** It may require $k$ games, which is impossible for $k$ up to $10^9$.
- **Find global maximum immediately:** Correct only for sufficiently large $k$; a weaker early champion may reach a small threshold first.
- **Track champion skill only:** The answer requires original index, so `i` must be retained.
- **k equals one:** Winner of the first game is returned.
- **k at least n-1:** The global maximum is eventual winner; capping is safe.
- **Maximum at index zero:** It wins every challenger and eventually reaches any threshold.
- **Maximum at last index:** Earlier players may win small thresholds before meeting it; otherwise it becomes final champion at the end.
- **Champion changes:** New champion count resets to one for the game just won.
- **Unique skills:** There are no drawn games.
- **First winner:** Immediate break preserves chronological firstness.
- **Losers moved to back:** They do not reappear before all unseen challengers have faced the champion.
- **Input preservation:** No physical queue operations or array mutations occur.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be number of players.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

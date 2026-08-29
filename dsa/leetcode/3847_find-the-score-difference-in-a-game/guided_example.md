# Guided Example: Find the Score Difference in a Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`, where $\text{nums}[i]$ represents the points scored in the $i^{\text{th}}$ game.

The objective is to compute `0` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent the active player with a sign

The requested result is:

$$
\text{first player's score}-\text{second player's score}.
$$

Instead of maintaining two totals, the source uses `k`:

- `k = 1` means the first player is active;
- `k = -1` means the second player is active.

Awarding `x` points changes the score difference by:

- `+x` for the first player;
- `-x` for the second player.

Both cases are expressed by:

`ans += k * x`.

The initial active player is the first, so `k` begins at 1.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the odd-score swap before awarding points

For each game value `x`, the first rule says an odd value swaps the players before the game is played.

Multiplying the sign by -1 swaps its meaning:

`k *= -1`.

The source performs this when `x % 2` is nonzero.

Even values leave `k` unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the sixth-game swap second

Game indices are zero-based, so the 6th, 12th, 18th, and later sixth games have indices 5, 11, 17, and so on.

These are exactly indices satisfying:

`i % 6 == 5`.

The source applies another `k *= -1` before scoring such a game.

This is placed after the odd-value condition, matching the stated rule order. Since both operations are the same sign flip, their algebraic effect would commute, but preserving the written order makes the simulation transparent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Maintain two score variables:** Track the active player as a Boolean and add to `score1` or `score2`. This is equally correct but uses a final subtraction; the sign directly maintains the requested quantity.
- **Precompute all active players:** Store which player handles every game, then sum scores. This wastes $O(N)$ space for a state that can be updated online.
- **Use if/elif for swaps:** This is wrong when an odd value occurs on a sixth game because both swaps must happen.
- **First game odd:** Player two becomes active before scoring, so the contribution is negative.
- **Odd sixth game:** Two swaps cancel and the previous active player scores.
- **Even sixth game:** Only the positional swap occurs.
- **Several odd games:** Each independently toggles the persistent active state.
- **Negative final difference:** It is valid and returned directly, as in the single odd-value example.
- **One game:** Only its parity rule can apply because index 0 is not a sixth-game index.
- **Game numbering:** The positional rule uses `i % 6 == 5` because the description's sixth games are one-based while the loop index is zero-based.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. The loop processes each game once with constant parity, index, sign, and addition operations. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

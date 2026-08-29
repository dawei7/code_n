# Guided Example: Score After Flipping Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]}`
- **Required output:** `39`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid`.

The objective is to compute `39` from `{"grid": [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The first bit of every row must be one in an optimum

Each row is interpreted as an `n`-bit binary number. The first column is the most significant bit, worth:

$$
2^{n-1}.
$$

All remaining bit weights together sum to:

$$
2^{n-2}+\cdots+2^0=2^{n-1}-1.
$$

Therefore, changing a row's leading bit from 0 to 1 gains more value than the maximum possible loss from toggling every lower bit in that row. Any optimal solution must make every first-column entry one.

Rows can be flipped independently, so the source flips exactly each row whose first bit is zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the forced row flips

For row `i` with `grid[i][0] == 0`, every entry is toggled through:

`grid[i][j] ^= 1`.

XOR with one converts zero to one and one to zero.

After this phase, the entire first column contains ones. Rows originally beginning with one remain unchanged because flipping them would make their most significant bit zero and cannot be optimal.

This fixes the row decisions. What remains is choosing column flips.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Columns can now be optimized independently

Flipping a column toggles that bit in every row but does not affect any other column. The total matrix score is the sum over columns of:

`number of ones in column * that column's binary weight`.

For column `j`, let `cnt` be its current number of ones. If left unchanged, it contributes `cnt` ones. If flipped, its zeros become ones, giving `m-cnt` ones.

The optimal count is:

`max(cnt, m - cnt)`.

No column choice affects another column, so taking the local maximum in every column gives the global maximum once row orientation is fixed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `39` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `39` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every subset of row and column flips:** There are `2^{m+n}` possibilities, unnecessary because bit significance and column independence force greedy choices.
- **Compute row flips virtually:** Treat cell `grid[i][j]` as toggled when its first bit is zero, avoiding input mutation. It has the same time and `O(1)` space.
- **All first bits already one:** No row is toggled; column optimization still applies.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. For an `m \times n` matrix, the row phase may toggle every cell once, taking `O(mn)` time. The column phase scans every cell once to count ones, also `O(mn)`. Total time is `O(mn)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

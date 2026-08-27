# Guided Example: Transform to Chessboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` binary grid `board`. In each move, you can swap any two rows with each other, or any two columns with each other.

The objective is to compute `2` from `{"board": [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify what row and column swaps cannot change

A chessboard has only two possible row patterns: an alternating row such as `0101` and its exact complement `1010`. Its columns have the same property.

Swapping columns rearranges every row in the same way. Therefore two rows that were identical remain identical, and two rows that were complements remain complements. A column swap cannot turn a third unrelated row pattern into one of the required two patterns.

The symmetric statement holds for columns under row swaps. Consequently a transformable board must already have:

- every row equal to the first row or its bitwise complement;
- every column equal to the first column or its bitwise complement;
- valid counts of the two row types and the two column types;
- valid zero/one counts within each line pattern.

These are invariants of the allowed operations, so an impossible board can be rejected before trying to count swaps.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode one line as a bit mask

The algorithm stores the first row in `rowMask` and the first column in `colMask`. Bit `i` records the value at index `i` of that line.

The low-`n`-bit mask `(1 << n) - 1` contains exactly `n` ones. XOR with it flips every board bit and no higher bit, so:

- `revRowMask = mask ^ rowMask` is the first row's complement;
- `revColMask = mask ^ colMask` is the first column's complement.

For every row `i` and column `i`, the nested loop builds `curRowMask` and `curColMask`. If either is neither its baseline nor its complement, no sequence of swaps can create a chessboard, and the method immediately returns `-1`.

At the same time, `sameRow` counts how many rows equal `rowMask`, and `sameCol` counts how many columns equal `colMask`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The algorithm stores the first row in `rowMask` and the firs... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why line-type quantities must be balanced

An alternating sequence of even length has exactly half of one type and half of the other. Thus, when `n` is even, the two complementary row patterns must each occur `n / 2` times, and so must the two column patterns.

For odd `n`, an alternating sequence begins and ends with the same type. One type occurs `(n + 1) / 2` times and the other occurs `n / 2` times. Either pattern may be the majority, but their counts must differ by exactly one.

The helper `f(mask, cnt)` checks both necessary balances:

- `ones = mask.bit_count()` measures the number of one bits inside the baseline line.
- `cnt` measures how many complete rows or columns use that baseline line rather than its complement.

For odd `n`, `abs(n - 2 * value) == 1` means the value is either floor or ceiling of half. For even `n`, both values must equal `n // 2`.

The first measure validates the pattern distribution along one dimension; the second validates how many complementary lines occur along the other dimension.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Tuple counters for rows and columns:** Count c:** - **Tuple counters for rows and columns:** Count complete line tuples, verify two complementary patterns, then count mismatches. It is conceptually direct but stores $O(n^2)$ tuple data unless carefully shared.
- **- **Try row and column permutations:** There are $:** - **Try row and column permutations:** There are $n!$ possibilities per dimension, far beyond the limit and unnecessary once the invariants are known.
- **- **Even dimension:** Both alternating starting bi:** - **Even dimension:** Both alternating starting bits are possible, so take the smaller of two swap counts.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the board dimension. Constructing the initial masks costs $O(n)$. Building every current row and column mask examines all $n^2$ cells, which dominates the running time. The helper uses a constant number of bit operations, so total time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

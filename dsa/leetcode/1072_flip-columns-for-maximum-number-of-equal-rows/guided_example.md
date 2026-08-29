# Guided Example: Flip Columns For Maximum Number of Equal Rows

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[0, 1], [1, 1]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `matrix`.

The objective is to compute `1` from `{"matrix": [[0, 1], [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Characterize rows that one shared flip set can make uniform

Flipping a column affects every row, so rows cannot choose flip sets independently. We need the largest group of rows for which one common column-flip pattern makes every row uniform.

For a particular row, there are only two ways it can become uniform:

- Make every final value zero.
- Make every final value one.

If a row begins `[0, 1, 0]`, making it all zero requires flipping exactly columns containing one. Making it all one requires flipping exactly the complementary columns containing zero.

Now compare two rows. They can both become uniform under the same flips exactly when they are either identical or exact bitwise complements. Identical rows react identically. Complementary rows remain complements after every shared column flip, so when one becomes all zero, the other becomes all one.

Rows with any other relationship cannot both be uniform: at some columns their equality relationship differs, so no shared flip vector can make both constant.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[0, 1], [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize a row and its complement to one key

The solution chooses a canonical representation whose first bit is always zero:



If the row starts with zero, it is converted directly to a tuple.

If it starts with one, every bit is flipped with XOR one. For binary values:

- `0 ^ 1` is one.
- `1 ^ 1` is zero.

The complemented row now starts with zero.

An original row and its exact complement produce the same normalized tuple. If one starts with zero, it is kept. Its complement starts with one and is flipped back to the first row.

Conversely, two rows producing the same normalized tuple must be identical or complements. Each normalization either leaves all bits unchanged or flips all bits. Reversing those possibilities shows the original rows differ by either no flips at all or a flip at every position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count equivalent row patterns

`cnt = Counter()` starts an empty frequency map. For every row:



adds one to its normalized pattern.

Each counter bucket therefore contains exactly one compatibility class: all rows that are identical to or complementary with one another. One shared column flip pattern can make every row in that class uniform.

To see the flip pattern, take the normalized key. Flip precisely the columns where the key contains one. Every row represented by the key becomes all zero or all one, depending on whether that row originally matched the key or its complement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[0, 1], [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **String pattern key:** Record whether each bit equals the row's first bit using characters such as `T` and `F`. It is equivalent to the normalized tuple and has the same bounds.
- **Compare every row pair:** Count identical or complementary rows for each reference row. This takes `O(M^2N)` time and repeats the same class work.
- **Encode rows as integers:** With manageable column counts, pack the normalized bits into one integer key. This can reduce object overhead while preserving the same conceptual normalization.
- **One row:** Its pattern frequency is one, and any row can be made uniform by choosing flips based on that row.
- **One column:** Every row is already uniform, all rows normalize to the one-bit zero key, and the answer is `M`.
- **All rows identical:** They share one key and can all be made uniform together.
- **All rows split between a pattern and its complement:** Both groups normalize to one key, so every row is counted.
- **Already uniform zero and one rows:** All-zero and all-one rows are complements and normalize together.
- **Different relative patterns:** They cannot share a successful flip set, even if they have the same number of ones.
- **Binary constraint:** XOR one is a complement only because every cell is zero or one.
- **Nonempty rows:** Accessing `row[0]` is safe under the matrix constraints.
- **Input preservation:** Tuples and complemented generators are new objects; the matrix rows are never modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let `M` be the number of rows and `N` the number of columns.
- **Auxiliary Space Complexity:** $O(MN)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

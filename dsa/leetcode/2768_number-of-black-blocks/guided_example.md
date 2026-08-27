# Guided Example: Number of Black Blocks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 3, "n": 3, "coordinates": [[0, 0]]}`
- **Required output:** `[3, 1, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `m` and `n` representing the dimensions of a **0-indexed** `m x n` grid.

The objective is to compute `[3, 1, 0, 0, 0]` from `{"m": 3, "n": 3, "coordinates": [[0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count only blocks that a black cell can affect

An `m` by `n` grid can be enormous, with up to about `10^10` cells, while the input contains at most `10^4` black coordinates. Enumerating every `2 x 2` block would ignore this sparsity and is infeasible.

There are exactly

$$
(m - 1)(n - 1)
$$

possible blocks because a top-left row can range from zero through `m - 2` and a top-left column from zero through `n - 2`. Most of these blocks contain no black cell. The exact solution counts the comparatively few blocks touched by at least one black coordinate and derives the untouched count by subtraction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 3, "n": 3, "coordinates": [[0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A cell belongs to at most four blocks

Suppose a black cell is at `(x, y)`. In a `2 x 2` block containing it, that cell can occupy one of four roles:

- top-left, making the block's top-left coordinate `(x, y)`;
- top-right, making the block's top-left coordinate `(x, y - 1)`;
- bottom-right, making the block's top-left coordinate `(x - 1, y - 1)`;
- bottom-left, making the block's top-left coordinate `(x - 1, y)`.

The exact code generates these four offsets compactly with

`pairwise((0, 0, -1, -1, 0))`.

Consecutive pairs from that sequence are `(0, 0)`, `(0, -1)`, `(-1, -1)`, and `(-1, 0)`. Adding each pair to `(x, y)` yields the four candidate top-left coordinates above.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose a black cell is at `(x, y)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Discard candidates outside the block grid

Not every candidate is real. A black cell on the top row cannot be a bottom cell of a block above the grid, and a cell on the far-right column cannot be a left cell of a block extending past the grid.

The condition

`0 <= i < m - 1 and 0 <= j < n - 1`

tests whether `(i, j)` is a legal block top-left coordinate. Only legal candidates are entered in the counter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 3, "n": 3, "coordinates": [[0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every block:** Inspecting four cells:** - **Enumerate every block:** Inspecting four cells for all `(m - 1)(n - 1)` blocks costs `O(mn)` and is impossible at the largest dimensions.
- **Materialize the whole grid:** A Boolean `m x n` matrix also costs `O(mn)` space despite the sparse black input.
- **Store black cells and query neighboring blocks:** One could build a black-coordinate set and inspect candidate blocks, but care is needed to deduplicate blocks. The counter accumulates and deduplicates in one structure.
- **No black coordinates:** The counter remains empty, all blocks belong to bucket zero, and the answer is `[(m - 1)(n - 1), 0, 0, 0, 0]`.
- **Corner black cell:** It belongs to exactly one block, and three generated candidates fail the boundary check.
- **Edge but non-corner cell:** It belongs to two blocks; the same general candidate filter handles this.
- **Interior black cell:** It belongs to four blocks.
- **Fully black block:** Four distinct input cells increment the same key, placing that block in `ans[4]`.
- **Shared block:** Neighboring black cells update one counter key rather than being counted as separate blocks.
- **Distinct-coordinate guarantee:** It prevents one black cell from incrementing the same block twice through duplicate input rows.
- **Minimum `2 x 2` grid:** There is exactly one possible block, and the counter value or untouched subtraction classifies it.
- **Huge grid with sparse coordinates:** Only touched keys are stored; the large zero count is represented by one integer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let `k` be `coordinates.length`. Each black coordinate generates exactly four candidates and performs a constant amount of boundary checking and expected-time hash-counter work. This costs `O(k)` expected time. The final loop visits at most four distinct blocks per coordinate, so it also costs `O(k)`. Computing the zero bucket is constant time. Total expected time is `O(k)`, independent of `mn`.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

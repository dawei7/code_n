# Guided Example: Maximum Number of Ones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"width": 3, "height": 3, "sideLength": 2, "maxOnes": 1}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Consider a matrix `M` with dimensions $width * height$, such that every cell has value `0` or `1`, and any **square** sub-matrix of `M` of size $sideLength * sideLength$ has at most `maxOnes` ones.

The objective is to compute `4` from `{"width": 3, "height": 3, "sideLength": 2, "maxOnes": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a repeating template satisfies every square

Take any `x` consecutive column indices. Their residues modulo `x` are all distinct and collectively equal zero through `x - 1`, regardless of the starting column. The same fact holds for any `x` consecutive row indices. Their Cartesian product therefore contains every residue pair exactly once.

Imagine choosing some template positions to be active and placing a one in every matrix cell whose residue pair is active. Every contiguous `x` by `x` square then contains exactly one copy of each active template position. If at most `maxOnes` positions are active, every constrained square has at most `maxOnes` ones automatically. This turns a large matrix-placement problem into choosing at most `maxOnes` positions from an $x^2$-cell template.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"width": 3, "height": 3, "sideLength": 2, "maxOnes": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Not every template position occurs equally often

When `width` or `height` is not a multiple of `x`, some residues appear one more time than others near the matrix boundary. Selecting a frequently repeated template position creates more total ones than selecting a less frequent one, while each constrained square still sees that selected residue exactly once.

The list `cnt` measures these multiplicities. It begins with $x^2$ zeros. The nested loops visit every actual matrix coordinate, compute its flattened residue index `k`, and increment `cnt[k]`. Afterward, `cnt[k]` equals the number of matrix cells that would become one if template position `k` were selected.

For instance, with width and height both three and `x = 2`, residue zero appears at coordinates using column residues zero and row residues zero. That residue pair occurs four times, while other pairs occur fewer times. With `maxOnes = 1`, selecting the frequency-four position places ones at the four corners and makes every two-by-two square contain one one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the most valuable allowed positions

Every selected template position consumes exactly one unit of the per-square allowance, because it appears once in every full `x` by `x` square. Its benefit is its multiplicity from `cnt`. All costs are identical, so the best choice is simply to take the `maxOnes` largest benefits.

The code sorts `cnt` in descending order and returns `sum(cnt[:maxOnes])`. If `maxOnes` is zero, the slice is empty and the sum is zero. If `maxOnes = x * x`, the slice includes every residue class and the sum is the entire matrix size, which corresponds to filling every cell with one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"width": 3, "height": 3, "sideLength": 2, "maxOnes": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compute residue frequencies arithmetically:** The number of coordinates with a given residue can be derived from quotient and remainder division in each dimension, avoiding the $O(wh)$ nested loop. This can reduce counting to $O(s^2)$ while preserving the same sorting step.
- **Min-heap of the best frequencies:** Keep only the largest `maxOnes` counts instead of sorting all $s^2$ entries. This may help when `maxOnes` is much smaller than $s^2$, but full sorting is simpler at these constraints.
- **Construct the full matrix:** Repeating the chosen template would produce a witness matrix, but the contract asks only for the maximum count, so allocating it is unnecessary.
- **`maxOnes = 0`:** No constrained square may contain a one. The empty sorted slice sums to zero.
- **`maxOnes = sideLength * sideLength`:** Every template position may be selected, so every matrix cell can be one and the result is `width * height`.
- **`sideLength = 1`:** There is one residue class. If `maxOnes` is one, its frequency is the whole matrix size; if it is zero, the answer is zero.
- **Dimensions equal to `sideLength`:** The whole matrix is one constrained square, every residue occurs once, and the answer is exactly `maxOnes`.
- **Dimensions not divisible by `sideLength`:** Residue frequencies differ. Sorting is essential because selecting the more frequent residues yields additional boundary cells at no extra per-window cost.
- **Width and height orientation:** The loops name the width coordinate `i` and height coordinate `j`. Swapping the axes would produce the same multiset of frequency products, so the final maximum is unchanged.
- **Flattened residue index:** Multiplying the first residue by `x` and adding the second gives a unique index from zero through $x^2-1$. Omitting the multiplication would mix distinct residue pairs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(wh+s^2\log s)$. Let $w$ be `width`, $h$ be `height`, and $s$ be `sideLength`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

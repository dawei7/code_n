# Guided Example: Find a Good Subset of the Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]}`
- **Required output:** `[0, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** `m x n` binary matrix `grid`.

The objective is to compute `[0, 1]` from `{"grid": [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Exploit the very small number of columns

There may be ten thousand rows, but each row has at most five binary entries. A binary row can therefore be represented by one of at most $2^n\le32$ bit masks.

For row `i`, the code starts `mask` at zero. For every column `j` with value `x`, it performs `mask |= x << j`. If `x=1`, bit `j` becomes one; if `x=0`, OR with zero changes nothing. The mask records exactly which columns contain ones.

Rows with identical bit patterns share a mask, so the dictionary `g` needs only one representative index per pattern.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A one-row good subset must be all zeros

For subset size $k=1$, the permitted sum in each column is:

$$
\left\lfloor\frac12\right\rfloor=0.
$$

Thus a single row is good exactly when it contains no ones, which is mask zero. The solution returns `[i]` immediately upon finding such a row. No answer can be smaller than a nonempty one-row subset.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Two rows are good exactly when their masks are disjoint

For $k=2$, each column may have sum at most one. This fails only if both chosen rows contain one in the same column.

Bitwise AND identifies shared one positions. Therefore masks `a` and `b` form a good pair exactly when:

`(a & b) == 0`.

The nested dictionary loops examine every pair of present patterns. When a disjoint pair is found, the stored representative row indices are sorted and returned to satisfy the output-order requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all row subsets:** Exponential in $m$ and impossible for ten thousand rows.
- **Check every original row pair:** Costs $O(m^2n)$; mask compression reduces the pair universe to at most 32 patterns.
- **Enumerate complementary submasks:** Can find a disjoint present mask in roughly $O(3^n)$ or related small-mask bounds, but is unnecessary for $n\le5$.
- **Zero row:** Return it immediately because a size-one subset is good.
- **Repeated nonzero mask:** One representative suffices; identical nonzero masks cannot form a disjoint pair.
- **Disjoint pair order:** Sorting the two indices satisfies the ascending requirement.
- **Single column:** A zero row works alone; otherwise two all-one rows are not good.
- **All-one rows:** No zero or disjoint pair exists, so return empty.
- **Bit direction:** Using bit `j` for column `j` is arbitrary but consistent; only shared-bit tests matter.
- **Column limit:** The guarantee $n\le5$ is essential to the structural reduction and tiny mask universe.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n)$. Let $m$ be the row count, $n\le5$ the column count, and $U\le2^n$ the number of distinct masks retained. Encoding all rows costs $O(mn)$ time. The exact nested loops inspect $U^2$ ordered mask pairs, costing $O(U^2)\subseteq O(4^n)$ time.
- **Auxiliary Space Complexity:** $O(2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

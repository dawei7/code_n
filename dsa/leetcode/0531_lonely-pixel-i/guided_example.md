# Guided Example: Lonely Pixel I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"picture": [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels, return *the number of **black** lonely pixels*.

The objective is to compute `3` from `{"picture": [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

A black pixel at coordinate `(i, j)` is lonely only when three conditions all hold:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"picture": [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the cell itself is `"B"`;
- row `i` contains exactly one black pixel;
- column `j` contains exactly one black pixel.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - the cell itself is `"B"`;
- row `i` contains exactly one b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution separates counting from classification. The first pass learns every row and column total. The second pass uses those totals to decide which black cells are lonely.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"picture": [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan a row and column for every black pixel:**:** - **Scan a row and column for every black pixel:** It uses constant extra storage but can take $O(RC(R+C))$ time in a dense picture.
- **Store black coordinates:** Counting only recorded coordinates can avoid a second full matrix scan, but the coordinate list may use $O(RC)$ space.
- **Modify the first row and column as counters:** It can reduce auxiliary space to $O(1)$ but complicates boundary handling and mutates the input.
- **Single black pixel:** Its row and column counts are both one, so the result is one.
- **All white pixels:** Every counter remains zero and no second-pass cell satisfies `x == "B"`.
- **One row:** A black pixel is lonely only if that row contains exactly one black pixel; its column then automatically contains one.
- **One column:** The symmetric rule applies using the column total and individual row totals.
- **White intersection of unique counts:** The explicit black-cell test prevents a false positive.
- **Two black pixels in one row:** Both fail the row-count condition even if their columns are otherwise empty.
- **Two black pixels in one column:** Both fail the column-count condition.
- **Several isolated diagonal pixels:** Each may be counted because loneliness is based on shared rows and columns, not diagonal adjacency.
- **Rectangular shape:** Separate row and column array lengths support non-square pictures directly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rows \cdot cols)$. Let $R$ be the number of rows and $C$ the number of columns. Each pass visits all $RC$ cells and performs constant work per cell. Two such passes still give $O(RC)$ time.
- **Auxiliary Space Complexity:** $O(rows + cols)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

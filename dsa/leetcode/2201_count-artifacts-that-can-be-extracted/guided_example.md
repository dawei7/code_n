# Guided Example: Count Artifacts That Can Be Extracted

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "artifacts": [[0, 0, 0, 0], [0, 1, 1, 1]], "dig": [[0, 0], [0, 1]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `n x n` **0-indexed** grid with some artifacts buried in it. You are given the integer `n` and a **0-indexed **2D integer array `artifacts` describing the positions of the rectangular artifacts where $\text{artifacts}[i] = [\text{r1}_{i}, \text{c1}_{i}, \text{r2}_{i}, \text{c2}_{i}]$ denotes that the $$i^{\text{th}}$$ artifact is buried in the subgrid where:

The objective is to compute `1` from `{"n": 2, "artifacts": [[0, 0, 0, 0], [0, 1, 1, 1]], "dig": [[0, 0], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Hash excavated coordinates

The set comprehension

`{(i, j) for i, j in dig}`

stores every dug row-column pair as a tuple.

Tuple equality compares both coordinates, so `(0,1)` and `(1,0)` remain distinct cells. Hash-set membership is expected $O(1)$.

The contract says dig entries are unique, but the set would safely deduplicate them even without that guarantee.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "artifacts": [[0, 0, 0, 0], [0, 1, 1, 1]], "dig": [[0, 0], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Unpack one artifact rectangle

Helper `check(a)` assigns `x1, y1, x2, y2` from the artifact description.

Rows in the footprint run from `x1` through `x2` inclusive. Columns run from `y1` through `y2` inclusive.

Both range stops add one because Python excludes the stop endpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Helper `check(a)` assigns `x1, y1, x2, y2` from the artifact... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate the rectangle's Cartesian product

The nested generator chooses every row `x` in the row interval and every column `y` in the column interval. This produces exactly all coordinates of the rectangular artifact.

For a one-cell artifact, both ranges contain one value. For a horizontal artifact, the row range has one value and columns vary. Vertical and two-dimensional rectangles follow the same code.

The constraint that an artifact covers at most four cells means this enumeration is constant-sized for each artifact.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "artifacts": [[0, 0, 0, 0], [0, 1, 1, 1]], "dig": [[0, 0], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean grid:** Mark an `n x n` matrix and ins:** - **Boolean grid:** Mark an `n x n` matrix and inspect artifacts. Membership is constant time but space grows as $O(n^2)$ instead of only dug cells.
- **Prefix-sum grid:** A two-dimensional prefix sum can query dug counts in rectangles quickly, useful for large artifacts but excessive when each covers at most four cells.
- **Map each cell to an artifact:** Count dug parts per artifact. The no-overlap guarantee makes this possible, but it requires indexing every artifact cell first.
- **Single-cell artifact:** It is extractable exactly when its one coordinate is in the set.
- **Partially dug artifact:** One absent coordinate makes `all` false.
- **All cells dug:** Every artifact check succeeds.
- **Extra dug cells:** Coordinates outside artifacts remain in the set but affect no check.
- **Unique dig entries:** No duplicate-count correction is needed; the set would handle duplicates anyway.
- **No artifact overlap:** One dug cell cannot represent parts of two artifacts under the contract.
- **Inclusive bottom-right corner:** Both ranges use endpoint plus one, ensuring it is tested.
- **At most four cells:** Per-artifact enumeration is constant bounded.
- **Short-circuit failure:** `all` may stop before checking later cells once extraction is impossible.
- **Grid size unused:** Valid-coordinate guarantees remove the need for a full-grid allocation.
- **Input preservation:** Artifact and dig arrays are only read.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a+d)$. Let $d$ be the number of dug cells, $a$ the number of artifacts, and let each artifact cover at most $q=4$ cells.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

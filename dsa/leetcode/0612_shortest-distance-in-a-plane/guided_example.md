# Guided Example: Shortest Distance in a Plane

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Point2D": [{"x": -1, "y": -1}, {"x": 0, "y": 0}, {"x": -1, "y": -2}]}}`
- **Required output:** `{"columns": ["shortest"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Point2D`

The objective is to compute `{"columns": ["shortest"], "rows": [[1]]}` from `{"tables": {"Point2D": [{"x": -1, "y": -1}, {"x": 0, "y": 0}, {"x": -1, "y": -2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generating distinct-point pairs

`Point2D AS p1` and `Point2D AS p2` are two logical copies of the same table. The join condition is:



It excludes a row paired with itself because identical points have equal $x$ and equal $y$, making both inequalities false. For two distinct coordinate pairs, at least one coordinate differs, so the OR is true.

The composite primary key guarantees coordinates are unique. Therefore, coordinate inequality is equivalent to distinct rows.

Every unordered pair appears twice: once as $(p_1,p_2)$ and once as $(p_2,p_1)$. Their distances are equal. This doubles constant work but does not change the minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Point2D": [{"x": -1, "y": -1}, {"x": 0, "y": 0}, {"x": -1, "y": -2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing distance

For each joined pair, the source evaluates:

$$
\sqrt{(p_1.x-p_2.x)^2+(p_1.y-p_2.y)^2}.
$$

`POW(..., 2)` squares each coordinate difference, `SQRT` converts squared distance to Euclidean distance, and `ROUND(..., 2)` produces the required two-decimal value.

The query could compare squared distances and apply one square root after finding the minimum because square root is increasing. The exact source computes full distance for every pair, which is simpler to read but does more numeric work.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Ordering and limiting

The computed column is the first selected expression and is aliased `shortest`. `ORDER BY 1` sorts by that rounded distance ascending. `LIMIT 1` returns one row containing the smallest rounded value.

Rounding occurs before ordering. Rounding to a fixed number of decimal places is monotone nondecreasing: if $a<b$, then rounded $a$ cannot become greater than rounded $b$ under ordinary SQL rounding. Two nearby distances may tie after rounding, but either tied row displays the same rounded value. Therefore, minimum of the rounded distances equals the rounded global minimum, and the returned numeric result remains correct.

Computing `MIN` on exact squared distances and rounding afterward would express the mathematical sequence more directly and avoid depending on this monotonicity observation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["shortest"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Point2D": [{"x": -1, "y": -1}, {"x": 0, "y": 0}, {"x": -1, "y": -2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["shortest"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate minimum squared distance:** `ROUND(SQRT(MIN(dx*dx+dy*dy)),2)` avoids sorting and computes square root once. It more directly supports $O(1)$ aggregate state.
- **Generate unordered pairs only:** Use a lexicographic condition such as `p1.x < p2.x OR (p1.x = p2.x AND p1.y < p2.y)` to halve pair rows.
- **Closest-pair divide and conquer:** In procedural code, sorting by coordinate and merging strips achieves $O(P\log P)$ time, but is much more complex than portable SQL.
- **Self-pairs:** Must be excluded or distance zero always wins.
- **Same $x$, different $y$:** OR condition keeps the pair because the $y$ inequality is true.
- **Same $y$, different $x$:** Symmetrically retained.
- **Duplicate coordinates:** Forbidden by the composite primary key; otherwise distinct rows at distance zero would be a legitimate minimum.
- **Only one point:** The join has no rows, so this exact query returns no row. The intended problem domain must provide at least two points for a shortest pair to exist.
- **Rounding ties:** Any tied pair produces the same displayed result, so `LIMIT 1` remains sufficient.
- **Round after minimum:** Preferable for mathematical clarity even though fixed-precision rounding is monotone.
- **Ordered-pair duplication:** Doubles constant work but not asymptotic complexity or result.
- **Physical-plan caveat:** `ORDER BY LIMIT 1` may be optimized as top-one, but a full materialized sort would violate the manifest’s constant-space assumption.
- **Any coordinate signs:** Squared differences handle negative coordinates correctly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $P$ be the number of points. The self-join produces $P(P-1)=\Theta(P^2)$ oriented pairs, and distance calculation is constant work per pair. Pair generation and evaluation therefore take $O(P^2)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

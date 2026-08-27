# Guided Example: Minimum Area Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of points in the **X-Y** plane `points` where $\text{points}[i] = [x_{i}, y_{i}]$.

The objective is to compute `4` from `{"points": [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the structure of an axis-aligned rectangle

Because every rectangle side must be parallel to an axis, its four corners have a rigid form:

- two distinct horizontal coordinates, `x1` and `x2`;
- two distinct vertical coordinates, `y1` and `y2`;
- points at all four combinations `(x1, y1)`, `(x1, y2)`, `(x2, y1)`, and `(x2, y2)`.

Therefore, a rectangle exists whenever the same pair of y-coordinates appears together in two different x-columns. Its area is the horizontal separation multiplied by the vertical separation.

The solution organizes the input around exactly this observation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group points into vertical columns

The dictionary `d` maps each x-coordinate to a list of all y-coordinates present at that x. For example, points `(1, 2)`, `(1, 5)`, and `(3, 2)` produce columns `d[1] = [2, 5]` and `d[3] = [2]`.

The outer loop processes x-coordinates in increasing order with `for x in sorted(d)`. Within each column, the y-values are also sorted.

Sorting the y-values serves two purposes. It lets the nested loops enumerate every unordered pair exactly once, with `y1 < y2`, and gives a canonical dictionary key `(y1, y2)`. The same geometric vertical segment is never represented sometimes as `(y1, y2)` and sometimes as `(y2, y1)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The dictionary `d` maps each x-coordinate to a list of all y... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What `pos` remembers

For a y-pair `(y1, y2)`, `pos[(y1, y2)]` stores the most recent x-coordinate to the left where both points `(x, y1)` and `(x, y2)` existed.

While processing the current column `x`, choosing `y1` and `y2` proves that the current column contains the right vertical side of a possible rectangle. If the pair is already in `pos`, the stored earlier column contains the matching left vertical side. All four required corners exist.

The resulting area is `(x - pos[(y1, y2)]) * (y2 - y1)`. Both differences are positive because x-columns are processed increasingly and the y-pair is ordered increasingly. The solution compares this candidate with `ans`.

After checking the candidate, it assigns `pos[(y1, y2)] = x`, even if the pair had appeared before.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Point-set diagonal test:** Put every point in :** - **Point-set diagonal test:** Put every point in a hash set, choose every pair as potential opposite corners, and test the other two corners. This also takes `O(N^2)` expected time and `O(N)` set space, but must reject equal x or y and may examine diagonal pairs that cannot improve the answer.
- **Store all x-values per y-pair:** It is correct but unnecessary. For a future right column, the closest previous x always gives the smallest width for that fixed height.
- **Enumerate pairs of x-columns:** Intersect their y-sets and choose two common y-values. This can work, but repeated set intersections may be expensive and the latest-pair map expresses the minimum-width logic directly.
- **No rectangle:** If no vertical y-pair repeats across two columns, `ans` remains infinity and the required result is zero.
- **Duplicate input points:** The contract says points are unique. Duplicates could cause repeated y-values within a column and zero-height pairs unless explicitly removed.
- **Two points in one column:** They create one candidate vertical segment but no rectangle until the same y-pair occurs at another x-coordinate.
- **More than two matching columns:** Updating `pos` to the latest column is essential because consecutive matching columns give the narrowest rectangle for future comparisons.
- **Several rectangles with equal minimum area:** The method stores only the numeric minimum, which is sufficient because coordinates do not need to be returned.
- **Coordinate value zero:** Zero is an ordinary valid coordinate. The algorithm uses dictionary membership rather than truthiness, so it handles stored x-coordinate zero correctly.
- **Axis alignment:** The y-pair method intentionally ignores rotated rectangles. Those do not satisfy this problem's side-orientation requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let `N` be the number of points, and let column `x` contain `k_x` points.
- **Auxiliary Space Complexity:** $O(N^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

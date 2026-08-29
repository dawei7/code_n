# Guided Example: Detect Squares

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["DetectSquares", "count"], "arguments": [[], [[4, 1]]]}`
- **Required output:** `[null, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a stream of points on the X-Y plane. Design an algorithm that:

The objective is to compute `[null, 0]` from `{"operations": ["DetectSquares", "count"], "arguments": [[], [[4, 1]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store point multiplicities by x-coordinate

`cnt[x][y]` is the number of times point $(x,y)$ has been added. The outer `defaultdict` groups points by vertical column, and each inner `Counter` maps y-coordinates to occurrence counts.

`add` increments rather than sets the count because duplicate points are distinct choices. This multiplicity directly affects how many squares can be formed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["DetectSquares", "count"], "arguments": [[], [[4, 1]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the opposite x-column

For query point $(x_1,y_1)$, any axis-aligned square has another horizontal corner $(x_2,y_1)$ with $x_2\ne x_1$.

The count method loops through every stored x-column `x2`. Difference

`d = x2 - x1`

is the signed horizontal displacement. The square side length is $\lvert d\rvert$, and positive area is guaranteed by skipping `x2 == x1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check both vertical directions

For a chosen opposite column, one square uses vertical coordinate `y1 + d`. Its three stored corners are:

- $(x_2,y_1)$;
- $(x_1,y_1+d)$;
- $(x_2,y_1+d)$.

The other uses `y1 - d` and the analogous two vertical corners.

Even when `d` is negative because `x2` lies left of the query, these two formulas still cover the squares on the two sides of the horizontal line. Their roles simply swap between visually above and below.

The signed formulas also guarantee equal side lengths without calling `abs`. The horizontal difference from `x1` to `x2` is `d`. The vertical difference to `y1+d` is the same signed amount, and to `y1-d` is its negation; both have magnitude $\lvert d\rvert$. The fourth corner combines the selected opposite x and y coordinates, so all edges are axis-aligned and equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["DetectSquares", "count"], "arguments": [[], [[4, 1]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store one global pair counter:** Query could enumerate y-levels or columns, but the nested column structure matches the square geometry directly.
- **Enumerate all stored point triples:** Cubic and ignores axis alignment until late.
- **Precompute every square on add:** Makes additions expensive and requires updating many query answers.
- **Duplicate points:** Multiply the number of distinct selection triples.
- **Query point not stored:** It can still form squares; only the other three points must be stored.
- **No points in query x-column:** Immediate zero because the vertical partner is missing.
- **Same x-column candidate:** Skipped to enforce positive side length.
- **Coordinates outside 0 through 1000 after adding `d`:** Counter lookup returns zero safely.
- **Opposite column left or right:** Signed `d` formulas cover both.
- **Squares above and below:** Both are counted separately.
- **Repeated count calls:** Do not change stored multiplicities.
- **Add complexity:** One nested counter increment is expected constant time.
- **Environment imports:** The exact source assumes `defaultdict` and `Counter` are available.
- **Query-time dimension:** `count` loops over distinct stored x-coordinates, not every added point. Repeated additions change multiplicities but do not lengthen this outer scan.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H)$. Let $H$ be the number of distinct stored x-coordinates and $P$ the number of distinct stored points. `add` takes expected $O(1)$ time.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

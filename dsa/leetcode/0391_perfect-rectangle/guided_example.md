# Guided Example: Perfect Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rectangles": [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `rectangles` where $\text{rectangles}[i] = [x_{i}, y_{i}, a_{i}, b_{i}]$ represents an axis-aligned rectangle. The bottom-left point of the rectangle is $(x_{i}, y_{i})$ and the top-right point of it is $(a_{i}, b_{i})$.

The objective is to compute `true` from `{"rectangles": [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An exact cover must satisfy both measure and boundary structure

The small rectangles form one perfect larger rectangle only if two independent kinds of evidence agree:

1. their total area equals the area of the smallest axis-aligned bounding rectangle;
2. their corners join exactly as a rectangular tiling’s corners must join.

Area alone is insufficient. An overlap adds area twice, while a gap adds no area; an overlap and gap of equal size could cancel numerically. Corner structure alone is also insufficient because it does not measure how much region is covered. The exact solution checks both.

It makes one pass through all rectangles, accumulating total area, expanding the bounding box, and counting every rectangle-corner coordinate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rectangles": [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the only possible outer rectangle

For a rectangle `[x, y, a, b]`, `(x, y)` is bottom-left and `(a, b)` is top-right. Across all inputs, the cover’s only possible outer bounds are:



The code initializes these from the first rectangle, then updates them with `min` and `max` for each rectangle. If an exact rectangular cover exists, its four outer corners must be

$$
(\texttt{minX},\texttt{minY}),
(\texttt{minX},\texttt{maxY}),
(\texttt{maxX},\texttt{maxY}),
(\texttt{maxX},\texttt{minY}).
$$

There is no other candidate enclosing rectangle: any cover must reach every extreme coordinate present in its pieces.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a rectangle `[x, y, a, b]`, `(x, y)` is bottom-left and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The area condition

Each rectangle contributes

$$
(a-x)(b-y)
$$

to `area`. Coordinates may be negative, but widths and heights are positive by the contract, so every contribution is positive.

After the scan, the bounding rectangle has area

$$
(\texttt{maxX}-\texttt{minX})
(\texttt{maxY}-\texttt{minY}).
$$

For a perfect cover, interiors of the pieces do not overlap and their union fills the bounding rectangle. Areas are then additive, so the two totals must be equal. If the sum is smaller, some bounding area is missing overall. If it is larger, some area is covered more than once overall. A mismatch immediately proves failure.

The comparison uses integer arithmetic, so there is no floating-point rounding concern.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rectangles": [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Corner parity set plus area:** Toggle each cor:** - **Corner parity set plus area:** Toggle each corner in a set: add it if absent and remove it if present. A perfect cover leaves exactly the four bounding corners. Together with area equality, this is the classic equivalent $O(r)$ approach. The exact source retains full counts and explicitly accepts only multiplicities two or four.
- **- **Sweep line:** Sort vertical events and maintai:** - **Sweep line:** Sort vertical events and maintain covered y-intervals while moving across x-coordinates. This can detect overlaps and gaps directly but is substantially more complex and usually costs $O(r\log r)$ time.
- **- **Grid marking:** Mark every unit cell or compre:** - **Grid marking:** Mark every unit cell or compressed coordinate region. Raw marking is impossible for large coordinate ranges, and coordinate compression still uses more machinery than the area-and-corner invariant.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of input rectangles.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

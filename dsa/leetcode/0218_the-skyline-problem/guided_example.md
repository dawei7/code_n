# Guided Example: The Skyline Problem

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"buildings": [[0, 2, 3], [2, 5, 3]]}`
- **Required output:** `[[0, 3], [5, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return *the **skyline** formed by these buildings collectively*.

The objective is to compute `[[0, 3], [5, 0]]` from `{"buildings": [[0, 2, 3], [2, 5, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A skyline can change only at a building boundary

Between two consecutive building edges, the set of rectangles covering the
ground does not change. Therefore the visible maximum height is constant on
that open horizontal interval. A key point can occur only at some building's
left edge, where a rectangle begins, or right edge, where one stops
contributing.

The exact solution collects both coordinates from every building in `lines`
and sorts that list. It deliberately keeps duplicate coordinates. Processing a
coordinate more than once is harmless because the output logic suppresses an
unchanged height; retaining duplicates avoids a separate set construction.
There are only $2n$ entries for $n$ buildings.

The input guarantee that `buildings` is already sorted by non-decreasing left
coordinate is essential to the `city` pointer. As the sweep visits boundary
coordinates from left to right, `city` identifies the first building not yet
inserted into the active priority queue.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"buildings": [[0, 2, 3], [2, 5, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What it means for a building to be active

A building `[left, right, height]` contributes at coordinate $x$ exactly when

$$
\texttt{left} \le x < \texttt{right}.
$$

The left edge counts, so every building whose left coordinate is at most the
current `line` must be inserted before measuring the height there. The right
edge does not count, so a building whose right coordinate is at most `line`
must be ignored before measuring.

The loop
`while city < n and buildings[city][0] <= line` inserts all newly started
buildings. Since the building list is left-sorted, once the first not-yet-added
building starts after `line`, every later one does too, and the loop can stop.
Each building is inserted exactly once, and `city` never moves backward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A building `[left, right, height]` contributes at coordinate... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use a min-priority queue as a max-height structure

Python's `PriorityQueue` returns the lexicographically smallest stored entry.
The source stores each building as
`[-height, left, right]`. A taller positive height has a more negative first
field, so the smallest entry corresponds to the greatest height. Thus
`-pq.queue[0][0]` is the current visible height once expired entries at the top
have been removed.

The `left` and `right` fields break ties between equal heights. Their exact tie
order does not affect the visible maximum; the right coordinate is also needed
to decide whether the top building has ended. The source peeks through
`pq.queue[0]`, the internal list used by `PriorityQueue`, rather than calling a
public peek method because that class does not expose one.

If no active building remains, the visible height is ground level 0.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 3], [5, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"buildings": [[0, 2, 3], [2, 5, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 3], [5, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`heapq` instead of `PriorityQueue`:** A plain :** - **`heapq` instead of `PriorityQueue`:** A plain heap list provides the same negative-height lazy-deletion algorithm with less synchronization overhead. `PriorityQueue` is thread-safe but the exact source peeks into its internal `.queue` list, so it already relies on implementation details.
- **Explicit start/end events with a multiset:** Add a height at every left edge and remove it at every right edge, then read the maximum. A balanced multiset supports arbitrary deletion but Python's standard library lacks a direct built-in version.
- **Divide and conquer:** Recursively compute skylines for building halves and merge two contour lists by x-coordinate while tracking both current heights. It also achieves $O(n\log n)$ time but requires careful equal-coordinate and redundant-height handling.
- **Coordinate compression with direct range updates:** Evaluate height on intervals between unique edges. A naive update touches many intervals per building and can degrade to $O(n^2)$ unless paired with a more advanced structure.
- **Several starts at one coordinate:** All are inserted before height measurement, so only their maximum can create the key point.
- **Several ends at one coordinate:** Expired top entries are repeatedly removed. A shorter expired entry may stay buried, but it cannot affect the current maximum and will be removed if it later surfaces.
- **A start and an end at the same coordinate:** The ending building is excluded and the starting building is included at that x, matching `[left, right)` coverage and avoiding a false intermediate gap.
- **One building:** Its left edge produces `[left,height]`; its right edge expires the only heap entry and produces `[right,0]`.
- **Nested buildings:** A shorter nested building never changes the contour while covered by a taller one. Lazy retention handles it without unnecessary output.
- **Equal-height touching or overlapping buildings:** The height-change check merges them into one continuous horizontal segment, as the note requires.
- **Gaps between groups:** When the previous active heap empties, a zero key point begins the ground segment. A later left edge raises the height again and creates another point.
- **Large coordinates and heights:** The algorithm compares Python integers and negates heights without overflow. It never allocates memory proportional to coordinate magnitude.
- **Input ordering:** The `city` pointer is correct because the reference guarantees non-decreasing left edges. With unsorted buildings, the method would need to sort them by left coordinate first.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of buildings. Collecting `lines` takes $O(n)$ time and
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Best Meeting Point

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` binary grid `grid` where each `1` marks the home of one friend, return *the minimal **total travel distance***.

The objective is to compute `6` from `{"grid": [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a median minimizes absolute distance

Suppose the sorted coordinates on one axis are

$$
a_0\le a_1\le\cdots\le a_{k-1}.
$$

Pair the smallest coordinate with the largest, the second smallest with the second largest, and so on. For a pair $a_i\le a_j$, any proposed meeting coordinate $z$ pays

$$
\lvert a_i-z\rvert+\lvert a_j-z\rvert.
$$

This sum is at least $a_j-a_i$. Equality holds whenever $z$ lies anywhere in the interval $[a_i,a_j]$. Moving outside that interval increases the sum because both distances then grow in the same outward direction.

To minimize every nested extreme pair simultaneously, choose $z$ in the middle interval. With an odd number of coordinates, that interval collapses to the single middle coordinate. With an even number, any coordinate between the lower and upper middle values is optimal. Selecting either middle value is therefore always valid.

Another way to see the same fact is to imagine shifting $z$ one step right. Every point to the left contributes one additional unit, while every point to the right contributes one fewer unit. Before the median, more points lie to the right, so moving right can improve the total. After the median, more points lie to the left, so moving right makes the total worse. The transition occurs at the median.

The mean does not have this property for absolute differences. A far-away coordinate can pull the mean away from most friends, while the median depends on how many coordinates lie on each side rather than how far an outlier lies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collecting the occupied coordinates

The source scans every cell with row index `i`, column index `j`, and value `v`. Whenever `v` is 1, it appends `i` to `rows` and `j` to `cols`. Each friend contributes exactly one coordinate to each list, so the two lists have the same length $k$.

The scan visits rows from top to bottom. Within each row, it visits columns from left to right. Because every row index from an earlier outer-loop iteration is no larger than every row index from a later iteration, `rows` is automatically collected in non-decreasing order. Repeated homes in the same row simply contribute repeated equal row coordinates, which is necessary because every friend contributes separately to the distance.

The column list is different. After finishing one row, the scan returns to column zero of the next row. For the example homes $(0,0)$, $(0,4)$, and $(2,2)$, the collected columns are `[0, 4, 2]`, which are not sorted. The exact source therefore calls `cols.sort()` before choosing the column median.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source scans every cell with row index `i`, column index... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selecting the two median coordinates

The source uses `len(rows) >> 1` as the median index. A right shift by one is integer division by two for the nonnegative list length, so this is the same index as `len(rows) // 2`.

For odd $k$, index $k//2$ is the unique middle element. For even $k$, it is the upper of the two middle elements. Choosing the upper median is valid because every point between the two middle coordinates minimizes the sum of absolute distances.

The statements

`i = rows[len(rows) >> 1]`

and

`j = cols[len(cols) >> 1]`

therefore choose an optimal meeting row and an optimal meeting column. Both values come from home coordinates and hence lie inside the grid, although the median proof would also permit intermediate coordinates in the even case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Collect columns in column-major order:** Scan :** - **Collect columns in column-major order:** Scan each column from left to right and each row within that column. Then `cols` is already sorted, eliminating `cols.sort()` and achieving $O(mn)$ time with $O(k)$ coordinate storage. This is the linear method described by the manifest, but it is not the exact source's traversal.
- **Pair extremes without selecting a median:** Once a coordinate list is sorted, add `arr[right] - arr[left]` while moving both pointers inward. This directly sums the unavoidable cost of each extreme pair and produces the same minimum.
- **Sort both coordinate lists:** It is correct but wastes work on `rows`, whose order is already guaranteed by the row-major scan.
- **Try every grid cell:** Computing distance from every candidate to every home costs $O(mnk)$ time and can reach $O(m^2n^2)$ when most cells contain homes.
- **Breadth-first search from every candidate:** Obstacles do not exist and Manhattan distance has a direct formula, so BFS adds queues and visited matrices without changing the distance result.
- **Use the arithmetic mean:** The mean minimizes squared distance, not the sum of absolute distances. An outlier can pull it away from the median and increase the required total.
- **Choose row and column from the same friend:** The optimal row and optimal column are independent. Their combination need not be one friend's home; requiring that restriction can miss valid optimal meeting points.
- **Even number of homes:** Any coordinate between the two middle values on an axis is optimal. The source deliberately chooses the upper middle value through index `k // 2`.
- **Repeated rows or columns:** Repetitions must remain in the lists because they represent different friends. Removing duplicates would give too little weight to crowded coordinates and could change the median.
- **Two adjacent homes:** For `[[1,1]]`, the row cost is zero. Either column 0 or 1 minimizes the horizontal cost at 1; the upper median selects column 1 and returns 1.
- **All homes in one row:** The median row is that shared row, so vertical distance is zero. Only column distances contribute.
- **All homes in one column:** The median column is that shared column, so horizontal distance is zero. Only row distances contribute.
- **Dense grid:** There can be $mn$ homes. Coordinate collection still uses $O(k)$ space, and each home contributes once to each axis sum.
- **At least two homes:** The source can also compute a one-home answer, but the contract guarantees two or more, so both coordinate lists are certainly nonempty when the median index is read.
- **Meeting point on an empty cell:** This is allowed. The problem minimizes travel to a point in the grid; it does not require that point to contain a home.
- **Manhattan distance specifically:** Axis separation relies on the sum of absolute coordinate differences. Euclidean distance would not permit the same independent median argument.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of grid rows, $n$ the number of columns, and $k$ the number of homes.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

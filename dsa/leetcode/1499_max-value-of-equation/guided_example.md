# Guided Example: Max Value of Equation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 3], [2, 0], [5, 10], [6, -10]], "k": 1}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where $\text{points}[i] = [x_{i}, y_{i}]$ such that $x_{i} < x_{j}$ for all $1 \le i < j \le \text{points.length}$. You are also given an integer `k`.

The objective is to compute `4` from `{"points": [[1, 3], [2, 0], [5, 10], [6, -10]], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Removing the absolute value

Points arrive in strictly increasing x-coordinate order. When an earlier point `i` is paired with the current point `j`, $x_i < x_j$, so

$$
\lvert x_i-x_j\rvert = x_j-x_i.
$$

The equation can be rearranged as

$$
y_i+y_j+x_j-x_i
=
(y_i-x_i)+(x_j+y_j).
$$

For a fixed current point, `x + y` is constant. The best eligible earlier point is therefore the one maximizing `y_i - x_i`, subject to `x - x_i <= k`.

The stored source represents the negative of that score in a min-heap. Each entry is `(x_i - y_i, x_i)`. The smallest first component corresponds to the largest `y_i - x_i`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 3], [2, 0], [5, 10], [6, -10]], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintaining eligibility

Before using the heap for current coordinates `x, y`, the loop checks its top entry. If `x - pq[0][1] > k`, that point is too far left and cannot form a valid pair now or with any later point. It is removed.

The while loop repeats because several expired points may rise to the top one after another. Once the heap is empty or its top point is within distance `k`, evaluation can proceed.

Expired entries that are not at the top may remain in the heap. This lazy deletion is safe. Only the top entry can influence the maximum calculation. If the top is valid, it already has the best score among every stored entry, so lower-priority expired entries are irrelevant. If an expired entry later becomes the top, the while loop removes it before use.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Computing the current best pair

When the heap is nonempty after expiration, its top supplies the minimum `x_i - y_i`. The source computes

`x + y - pq[0][0]`,

which equals

$$
x_j+y_j-(x_i-y_i)
=
y_i+y_j+x_j-x_i.
$$

That is precisely the original equation for this ordered pair. The value updates `ans` if it is the largest seen across all current points.

Only after evaluating pairs ending at the current point does the code push `(x - y, x)`. This order ensures that a point cannot pair with itself. It becomes a candidate only for later points, as required by $i<j$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 3], [2, 0], [5, 10], [6, -10]], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Monotonic deque:** Keep eligible points in decreasing order of `y_i-x_i` and increasing x order. Each point enters and leaves once, achieving the manifest's $O(N)$ time and $O(N)$ space.
- **Brute-force pairs:** Testing all earlier points for every current point costs $O(N^2)$ and ignores the rearranged separability.
- **Balanced search structure:** It can maintain scores with logarithmic operations like the heap, but usually adds implementation complexity.
- **Negative y-values:** Initializing with negative infinity is necessary because every valid equation value may be negative.
- **Distance exactly k:** The expiration test uses greater than k, so equality remains valid.
- **k equals zero:** Strictly increasing x-values allow no pair at distance zero; the existence guarantee therefore excludes such an effective test instance.
- **Several equal scores:** Any heap top with the minimum `x-y` gives the same optimal contribution.
- **Expired non-top entries:** They may remain temporarily but cannot affect the answer until reaching the top, when they are removed.
- **Self-pairing:** Pushing the current point after evaluation prevents using the same point twice.
- **Sorted input requirement:** Permanent expiration and the sign simplification rely on strictly increasing x-coordinates.
- **Missing imports:** A standalone file must provide `heappush`, `heappop`, and `inf`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$. Let $N$ be the number of points. Every point is pushed into the binary heap once. An entry is popped at most once. Each push or pop costs $O(\log N)$, and top inspection is constant time. Total time is therefore $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

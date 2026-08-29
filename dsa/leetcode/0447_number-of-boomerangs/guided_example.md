# Guided Example: Number of Boomerangs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[0, 0], [1, 0], [2, 0]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given `n` `points` in the plane that are all **distinct**, where $\text{points}[i] = [x_{i}, y_{i}]$. A **boomerang** is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` **(the order of the tuple matters)**.

The objective is to compute `2` from `{"points": [[0, 0], [1, 0], [2, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One distance counter for one pivot

For each point `p1`, create a fresh `Counter` named `cnt`. Its key is a distance from `p1`, and its value is the number of points already seen at exactly that distance. Then scan every point `p2` and compute `d = dist(p1, p2)`.

Before inserting `p2`, suppose `cnt[d] = t`. There are exactly `t` earlier endpoints at the same distance from `p1`. Pairing the new `p2` with each one creates `t` new unordered endpoint pairs centered at `p1`. The code adds `t` to `ans`, then increments `cnt[d]` so that `p2` is available to pair with later endpoints.

This incremental rule is another way to compute a combination. If a distance group eventually contains $m$ points, its successive contributions are

$$
0+1+2+\cdots+(m-1)=\binom{m}{2}.
$$

That is the number of unordered ways to select two endpoints from the group. The scan avoids a separate second pass over all counter values because it adds each new pair at the moment its later endpoint is encountered.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[0, 0], [1, 0], [2, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why doubling gives ordered tuples

Every unordered pair `{j, k}` around a fixed pivot corresponds to exactly two ordered tuples: `(i, j, k)` and `(i, k, j)`. No other ordering keeps the same pivot first. Therefore the number of ordered boomerangs is exactly twice the accumulated number of unordered endpoint pairs.

The expression `ans << 1` shifts the binary representation of the nonnegative integer `ans` one place left. For integers, this is exactly multiplication by two, so it converts the unordered-pair count into the required ordered-tuple count.

An equivalent direct formula for a distance group of size $m$ is $m(m-1)$: choose the second tuple position in $m$ ways and the third in $m-1$ ways. The implementation's incremental count obtains $\binom{m}{2}$ first and applies the factor of two only once at the end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A concrete trace

Consider points `[[0,0], [1,0], [2,0]]`. Use `[1,0]` as the pivot.

- The pivot itself has distance `0`; no earlier point has that distance, so it adds nothing and makes `cnt[0] = 1`.
- `[0,0]` has distance `1`; it is the first endpoint in that group, so it adds nothing and makes `cnt[1] = 1`.
- `[2,0]` also has distance `1`. There is already one point in that group, so it adds one unordered pair and makes `cnt[1] = 2`.

The other two pivots have no distance group containing two non-pivot points. Thus `ans` is `1`, and shifting it left gives `2`: `([1,0], [0,0], [2,0])` and `([1,0], [2,0], [0,0])`.

The iteration order of `points` does not affect the result. Within a group of size $m$, whichever point is seen second contributes one, whichever is seen third contributes two, and so on. Their sum is always $\binom{m}{2}$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[0, 0], [1, 0], [2, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every ordered triple:** Trying all distinct `(i, j, k)` tuples takes $O(n^3)$ time. Grouping endpoints by distance counts all choices for a pivot collectively and reduces this to $O(n^2)$.
- **Count full groups after the inner scan:** For each distance frequency $m$, adding $m(m-1)$ directly is equally valid. The exact solution instead accumulates unordered pairs online and doubles once at the end.
- **Use squared Euclidean distance:** The key `(x1 - x2) ** 2 + (y1 - y2) ** 2` avoids square roots and floating-point keys. It is often preferred in fixed-width languages, using a sufficiently wide integer type. The present solution uses `dist` but relies on the same grouping principle.
- **Use Manhattan distance:** This would change the problem. A boomerang is based on Euclidean distance, so points equal under Manhattan distance may not be geometrically equidistant.
- **One point:** Every distance group has size one, no endpoint pair exists, and the method returns zero.
- **Two points:** Each pivot has only one other endpoint, so no group can supply two distinct endpoints. The answer is again zero.
- **The pivot itself:** Its zero-distance group contains only itself because all input points are unique, so it never contributes a pair.
- **Several points on one circle around a pivot:** If $m$ points share that radius, they contribute $m(m-1)$ ordered boomerangs for that pivot, even if their coordinates or directions differ.
- **Same endpoint coordinates:** The contract forbids duplicate points. That guarantee ensures `j` and `k` are genuinely different points when two separate entries are selected and keeps the pivot's zero-distance group harmless.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of points. The outer loop selects each of the $n$ pivots, and for every pivot the inner loop examines all $n$ points. Distance computation in two dimensions, counter lookup, addition, and counter update are constant-time operations. Total expected time is therefore $O(n^2)$, where “expected” reflects the usual expected $O(1)$ behavior of hash-table operations.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

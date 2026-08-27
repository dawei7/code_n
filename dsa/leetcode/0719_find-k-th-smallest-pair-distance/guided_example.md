# Guided Example: Find K-th Smallest Pair Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 1], "k": 1}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **distance of a pair** of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

The objective is to compute `0` from `{"nums": [1, 3, 1], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search the answer value instead of constructing every pair

For `n` numbers there are `n(n - 1) / 2` index pairs. Building every absolute difference and sorting those differences would materialize a quadratic collection. The exact solution avoids that collection by binary-searching the distance value.

After sorting `nums`, the distance of a pair with earlier index `j` and later index `i` is simply `nums[i] - nums[j]`, because the later value is never smaller. Possible distances range from `0` through

`W = nums[-1] - nums[0]`.

The central question becomes: for a proposed distance `dist`, how many pairs have distance at most `dist`? If that count is at least `k`, then the kth-smallest distance is no greater than `dist`. If the count is less than `k`, the desired distance must be larger.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 1], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How `count(dist)` counts qualifying pairs

The helper considers every sorted position `i` as the right endpoint of a pair. Its value is stored as `b = nums[i]`. A prior value `nums[j]` forms a qualifying pair precisely when

`b - nums[j] <= dist`,

which is equivalent to

`nums[j] >= b - dist`.

The helper sets `a = b - dist` and calls `bisect_left(nums, a, 0, i)`. This returns the first index `j` in the already-sorted prefix `nums[0:i]` whose value is at least `a`. Therefore all prior indices from `j` through `i - 1` qualify, and there are exactly `i - j` of them.

Summing `i - j` across every right endpoint counts each unordered index pair exactly once. A pair is counted when its larger index is used as `i`, and it cannot be counted under any other right endpoint.

Duplicates are handled naturally. If `b` has earlier equal copies and `dist = 0`, the threshold is `b` itself. The left binary search locates the first equal copy, so all equal earlier values contribute zero-distance pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper considers every sorted position `i` as the right ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the counting function is monotone

If a pair has distance at most `d`, it also has distance at most any larger value. Consequently, `count(d)` never decreases as `d` grows.

This monotonicity creates a boundary in the distance domain:

- Before the boundary, fewer than `k` pairs qualify.
- At the boundary and afterward, at least `k` pairs qualify.

The first distance at which the count reaches `k` is exactly the kth element of the sorted multiset of pair distances. “Multiset” matters because different index pairs with the same distance occupy separate ranks, and the helper counts them separately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 1], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-pointer counting inside the answer search::** - **Two-pointer counting inside the answer search:** For each right endpoint, move one shared left pointer forward until the distance is at most the candidate. Both pointers move only forward, making one count `O(n)`. Combined with value binary search, this yields `O(n log n + n log(W + 1))` time and is the standard refinement that meets the tighter manifest-style bound.
- **- **Generate and sort every distance:** This is co:** - **Generate and sort every distance:** This is conceptually simple but creates `O(n^2)` distances and then spends `O(n^2 log n)` time sorting them. It becomes impractical as `n` grows.
- **- **Heap-based pair generation:** A heap can produ:** - **Heap-based pair generation:** A heap can produce distances in increasing order from sorted data without storing all pairs at once. It can be useful when `k` is very small, but its indexing logic is more involved and its running time depends directly on `k`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n + n \log W)$. Let `n` be the number of values and `W = max(nums) - min(nums)` after sorting.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Count Partitions With Max-Min Difference at Most K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [9, 4, 1, 3, 7], "k": 4}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`. Your task is to partition `nums` into one or more **non-empty** contiguous segments such that in each segment, the difference between its **maximum** and **minimum** elements is **at most** `k`.

The objective is to compute `6` from `{"nums": [9, 4, 1, 3, 7], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: DP definition

Using prefix lengths, `f[r]` is the number of valid partitions of the first `r` elements. The empty prefix has one valid way, so `f[0]=1`. This base lets a segment beginning at the array’s first element contribute one partition.

`g[r]` is the modular prefix sum:

$$
g[r]=\sum_{p=0}^{r} f[p].
$$

It also begins with `g[0]=1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [9, 4, 1, 3, 7], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Finding the earliest valid last-segment start

The loop uses one-based prefix endpoint `r` while actual array index is `r-1`. Variable `l` is a one-based candidate starting position, so the current window is `nums[l-1:r]`.

After inserting the new value into `sl`:

- `sl[0]` is the window minimum;
- `sl[-1]` is the window maximum.

While their difference exceeds `k`, the leftmost value `nums[l-1]` is removed and `l` advances.

When shrinking stops, `[l,r]` is valid. It is also the earliest valid start for this endpoint: every earlier start was removed only while its larger window violated the condition.

All later starts `l+1,\ldots,r` are valid too. Removing elements from a valid segment cannot increase its maximum-minus-minimum difference.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop uses one-based prefix endpoint `r` while actual arr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Partition recurrence

If the final segment starts at one-based position `s`, everything before it has length `s-1` and can be partitioned in `f[s-1]` ways.

Valid starts form continuous range `s=l,\ldots,r`, so:

$$
f[r]=\sum_{s=l}^{r} f[s-1]
=\sum_{p=l-1}^{r-1} f[p].
$$

Using prefix sums:

$$
f[r]=g[r-1]-g[l-2].
$$

When `l=1`, there is no prefix before `g[0]` to subtract, so the source uses zero. Adding `mod` before remainder prevents a negative intermediate representation.

Afterward,

`g[r]=(g[r-1]+f[r]) mod mod`

extends the prefix-sum table.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [9, 4, 1, 3, 7], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Monotonic minimum and maximum deques:** Each i:** - **Monotonic minimum and maximum deques:** Each index enters and leaves each deque once, reducing window maintenance to `O(n)` total and realizing the manifest summary.
- **Two heaps with lazy deletion:** They can maintain extrema but require more bookkeeping than deques or SortedList and still have logarithmic operations.
- **Quadratic DP:** Testing every possible final-segment start directly costs `O(n^2)` even if segment validity is known; prefix sums remove that inner summation.
- **k equals zero:** A segment is valid only when all its values are equal. Duplicate handling in SortedList preserves this condition.
- **Every segment valid:** `l` remains one, and the recurrence counts all `2^{n-1}` placements of cuts modulo the modulus.
- **Only singleton segments valid:** `l=r` at each endpoint, so `f[r]=f[r-1]` and exactly one partition exists.
- **Duplicate extrema:** Removing one copy does not change the extreme until its last occurrence leaves, which SortedList handles naturally.
- **Large values:** Only comparisons and subtraction matter; Python integers avoid overflow.
- **Non-empty segments:** Starts stop at `r`, so every final segment contains at least one element.
- **Empty-prefix base:** `f[0]=1` is essential for partitions whose first segment starts at index zero.
- **Modulo subtraction:** Adding the modulus before remainder keeps the stored count nonnegative.
- **Third-party structure:** The source assumes `SortedList` is available in the execution environment; a deque version avoids that dependency.
- **Monotonic left boundary:** `l` never moves backward as `r` advances. Once a start makes a window invalid, adding more elements on the right cannot reduce that already-observed range enough to make the removed start necessary again. This one-way movement is why total removals remain linear even though each ordered-multiset removal costs logarithmic time.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Each of `n` values is inserted once and removed at most once. `SortedList` insertion and removal cost `O(\log n)`, while minimum and maximum indexing and DP arithmetic are constant-time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

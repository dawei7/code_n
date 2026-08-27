# Guided Example: Longest Balanced Subarray II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 4, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `4` from `{"nums": [2, 5, 4, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Give each distinct value a signed contribution

A subarray is balanced when it has equally many distinct even and distinct odd values. Assign a sign to each value:

$$
\operatorname{det}(x)=
\begin{cases}
+1, & x\text{ is odd},\\
-1, & x\text{ is even}.
\end{cases}
$$

If each distinct value in a subarray contributes its sign exactly once, their sum is

$$
\#\text{distinct odd}-\#\text{distinct even}.
$$

The subarray is balanced exactly when this sum is zero. The challenge is that a value may occur many times, and whether it contributes to `nums[left:right + 1]` depends on whether at least one occurrence lies inside those boundaries.

The solution processes right endpoints from left to right and represents all possible left boundaries simultaneously. A lazy segment tree supports the range changes caused when a value's latest occurrence moves.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 4, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Describe a subarray by its boundary before the left endpoint

The source uses one-based positions for processed elements: iteration `i` represents original index `i - 1`. Let `j` be a boundary from zero through `n`. The subarray after boundary `j` and ending at `i` is the one-based interval

$$
[j+1,i],
$$

whose length is `i - j`.

After position `i` has been processed, let `last[x]` be the latest one-based occurrence of each distinct value `x` in the prefix `[1,i]`. Define a segment-tree leaf value

$$
T[j]
=
\sum_{\operatorname{last}[x]\le j}\operatorname{det}(x).
$$

In words, `T[j]` contains the signed contributions of values whose latest occurrence is at or before boundary `j`.

The variable `now` is the signed sum over every distinct value in the entire processed prefix:

$$
\texttt{now}
=
\sum_x\operatorname{det}(x).
$$

Subtracting the leaf value gives

$$
\texttt{now}-T[j]
=
\sum_{\operatorname{last}[x]>j}\operatorname{det}(x).
$$

A value has `last[x] > j` exactly when it occurs somewhere in `[j+1,i]`. Consequently, this difference is the signed distinct-value balance of that subarray. The subarray is balanced exactly when

$$
\texttt{now}-T[j]=0,
$$

or equivalently,

$$
T[j]=\texttt{now}.
$$

The problem for each right endpoint is therefore: find the smallest boundary `j` whose segment-tree value equals `now`. The smallest boundary gives the largest length `i - j`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source uses one-based positions for processed elements: ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a latest occurrence becomes a suffix addition

Suppose a value `x` currently has latest occurrence `p`. In the definition of `T[j]`, its sign is included precisely when `j >= p`. Thus one value with latest position `p` contributes `det(x)` to the entire leaf range `[p,n]`.

This explains the range updates in the exact source.

When `x` appears for the first time at position `i`:

- Set `last[x] = i`.
- Add `det(x)` to every leaf in `[i,n]`.
- Add `det(x)` to `now` because the set of distinct prefix values gained `x`.

When `x` has appeared before at old latest position `p`:

- Subtract `det(x)` from `[p,n]` to erase the old latest-position contribution.
- Subtract it temporarily from `now`.
- Change `last[x]` to `i`.
- Add `det(x)` to `[i,n]` for the new latest position.
- Add it back to `now`.

For a repeat, the two `now` changes cancel because `x` was already distinct in the prefix. The range effects do not cancel everywhere: leaves `p` through `i - 1` lose the contribution, while leaves from `i` onward lose and regain it. That is exactly right. A boundary between the old and new occurrence used to lie after the latest `x`, but after the new occurrence it lies before the latest `x`.

Leaves before `p` excluded the value both before and after, so they need no change.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 4, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quadratic expansion from every left endpoint:*:** - **Quadratic expansion from every left endpoint:** Maintaining a distinct set while extending every candidate is $O(n^2)$ and works for the smaller version, but it is too slow for `n = 10^5`.
- **Ordinary prefix sum of element parity:** Adding a sign for every occurrence counts elements, not distinct values. Repeated numbers would distort the balance. Moving the contribution to the latest occurrence is what makes each value count once for every candidate boundary.
- **Sliding window with two distinct counters:** Balance is not monotonic as a window grows or shrinks. An unmatched new odd can later be paired by an even, and removing a duplicate may do nothing, so there is no safe greedy rule for moving one boundary.
- **Store only minimum or only maximum:** Target existence requires knowing whether it lies inside the entire attained range. Both endpoints are necessary for the discrete intermediate-value test.
- **Use the min/max test without unit adjacent changes:** For an arbitrary sequence, minimum below and maximum above a target do not ensure exact equality. The query is valid specifically because neighboring `T` leaves differ only by `-1`, zero, or `+1`.
- **Search the right child first:** That would find the largest matching boundary and therefore the shortest balanced subarray ending at `i`. The source searches left first to maximize length.
- **A first occurrence:** There is no old range to remove. It changes `now` and installs its sign beginning exactly at its current position.
- **A repeated occurrence:** The value remains one distinct prefix value, so `now` must finish unchanged. Its last-position suffix contribution moves forward instead.
- **All values have one parity:** No nonempty subarray has equal nonzero distinct-group sizes. Queries fall back to boundary `i` and contribute length zero, leaving the answer zero.
- **Duplicates spanning a boundary:** A value is counted for `[j+1,i]` precisely when its latest occurrence exceeds `j`. Earlier copies do not need individual representation.
- **Balanced prefix:** Boundary zero has `T[0] = 0`. When `now = 0`, the query can return zero and record the full prefix length `i`.
- **Single-element input:** Its distinct balance is either plus one or minus one. Boundary one supplies the guaranteed target match, producing length zero and the correct answer.
- **Sign convention:** The code assigns plus one to odd and minus one to even, the reverse of another equally valid convention. Only equality to zero matters; the derivation must remain consistent with the exact source's signs.
- **Values up to `10^5`:** The tree is indexed by positions, not numeric values. Large values only become dictionary keys, so space depends on `n` and `U` rather than the maximum value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the array length and `U` the number of distinct values. Building the tree with `n + 1` zero leaves takes $O(n)$ time. Each array position causes one range addition when its current latest occurrence is installed and, for a repeated value, one additional range addition to erase the old contribution. Every range addition takes $O(\log n)$ time with lazy propagation.
- **Auxiliary Space Complexity:** $O(n+U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

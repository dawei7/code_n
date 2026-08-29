# Guided Example: Maximum Number of Consecutive Values You Can Make

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"coins": [1, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the $i^{\text{th}}$ coin is $\text{coins}[i]$. You can **make** some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

The objective is to compute `2` from `{"coins": [1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track a complete interval of constructible sums

The empty subset always makes zero. The solution maintains `ans` as the first nonnegative value that cannot yet be made from the processed coins. Equivalently, before each iteration, every value in the interval

$$
[0,\texttt{ans}-1]
$$

is constructible.

Initially no coin has been processed. Only zero is known to be constructible, so `ans = 1`. This variable serves two roles at the end: it is the first missing value, and because the constructible run is `0, 1, ..., ans - 1`, it is also the number of consecutive values in that run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"coins": [1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process coins from smallest to largest

The solution iterates through `sorted(coins)`. Sorting is essential because when a gap appears, the algorithm must know that every unprocessed coin is at least as large as the current one.

Consider the next coin value `v` while all sums through `ans - 1` are possible.

If `v <= ans`, using no copy of this new coin preserves all old sums `[0, ans - 1]`. Adding this coin to every old constructible sum produces every value in

$$
[v,\ v+\texttt{ans}-1].
$$

Because $v\leq\texttt{ans}$, this new interval begins no later than the first missing value. It overlaps or touches the old interval, so their union has no gap:

$$
[0,\texttt{ans}+v-1].
$$

The first missing value therefore advances by $v$, implemented as `ans += v`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Stop permanently when the next coin is too large

If `v > ans`, value `ans` cannot be made.

Processed coins can produce at most the already covered range ending at `ans - 1`. Any subset that uses `v` has sum at least `v` because every coin value is positive, and `v > ans`. Since the coins are sorted, every later unprocessed coin is at least `v` and also cannot help make the smaller missing value `ans`.

The gap is permanent, so the loop can `break` immediately. Values larger than the gap do not matter because the requested sequence must start at zero and remain consecutive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"coins": [1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Subset-sum dynamic programming:** It records many individual sums and can depend on the potentially large total coin value, while the interval invariant needs only one frontier.
- **Enumerate all subsets:** There are $2^n$ subsets and the constraints make enumeration impossible.
- **Process unsorted coins:** Breaking on a large coin would be unsafe if a smaller helpful coin appeared later; sorting makes the gap proof valid.
- **Maximum-heap order:** Large coins first reveal no useful information about the smallest missing value.
- **Coin exactly equal to `ans`:** Its new interval starts exactly where old coverage ends, so it extends the run without a gap.
- **Coin smaller than `ans`:** New and old intervals overlap, still yielding continuous coverage.
- **Coin larger than `ans`:** The current frontier is impossible and all later positive sorted coins are too large, so stopping is conclusive.
- **First coin greater than one:** Value one is immediately missing, so the answer remains one for the constructible value zero.
- **Repeated coins:** Every occurrence is processed separately and can extend coverage.
- **Single coin of value one:** Values zero and one are possible, so the answer is two.
- **Single larger coin:** Only zero belongs to the consecutive prefix, so the answer is one.
- **Positive-value guarantee:** The gap proof relies on adding an unprocessed coin never reducing a sum.
- **Meaning of the return value:** `ans` is the first missing integer and also the count of integers from zero through `ans - 1`.
- **Input preservation:** `sorted` returns a new list instead of reordering `coins`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of coins. Python's `sorted(coins)` creates and sorts a new list in $O(n\log n)$ time. The subsequent scan is $O(n)$, so total time is $O(n\log n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

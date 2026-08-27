# Guided Example: Create Maximum Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [3, 4, 6, 5], "nums2": [9, 1, 2, 5, 8, 3], "k": 5}`
- **Required output:** `[9, 8, 6, 5, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

The objective is to compute `[9, 8, 6, 5, 3]` from `{"nums1": [3, 4, 6, 5], "nums2": [9, 1, 2, 5, 8, 3], "k": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the problem into three decisions.

The output must preserve the relative order of digits taken from `nums1`, and it must separately preserve the relative order of digits taken from `nums2`. Digits from the two arrays may be interleaved. This suggests three layers:

1. decide how many of the $k$ output digits come from each array;
2. choose the lexicographically greatest subsequence of the required length from each array;
3. merge those two subsequences into the lexicographically greatest order that preserves both of their internal orders.

Lexicographic order is the right comparison because every candidate has exactly $k$ digits. The candidate with the larger digit at the first differing position represents the larger number. Later digits matter only when all earlier digits tie.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [3, 4, 6, 5], "nums2": [9, 1, 2, 5, 8, 3], "k": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate every feasible split.

Suppose `nums1` has length $m$ and `nums2` has length $n$. Let $x$ be the number of selected digits from `nums1`; then exactly $k-x$ digits must come from `nums2`. A split is feasible only when

$$
0 \le x \le m
$$

and

$$
0 \le k-x \le n.
$$

Combining these inequalities gives the inclusive range

$$
\max(0, k-n) \le x \le \min(k,m).
$$

These are precisely the values called `l` and `r` in the source. Starting at `0` unconditionally would ask `nums2` for too many digits in some cases; ending at `k` unconditionally could ask `nums1` for too many. The bounds avoid invalid choices without omitting any valid output. Every possible answer uses some definite number $x$ of positions from the first array, so checking the entire range guarantees that its split is considered.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose `nums1` has length $m$ and `nums2` has length $n$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose one array's best fixed-length subsequence with a monotonic stack.

The helper `f(nums, k)` must retain exactly `k` digits while preserving their order. Equivalently, from an input of length `n`, it may delete exactly `n - k` digits. The variable `remain` stores that deletion budget.

The result is represented by a fixed-length array `stk` and an integer `top`. Only indices from `0` through `top` are currently filled. For each incoming digit `x`, the helper repeatedly removes the last selected digit while all three conditions hold:

- a selected digit exists;
- that last digit is smaller than `x`;
- at least one deletion remains.

Why is removing that smaller digit safe? It replaces the earliest position at which the current partial subsequence can improve. A larger digit earlier in a number is more valuable than any arrangement of later digits. Because `x` occurs later in the original array, replacing the previous last digit with `x` still preserves order. The deletion budget check is essential: without it, the method might discard so many digits that fewer than `k` positions remain available.

After all profitable removals, the current digit is placed into the stack if fewer than `k` digits are selected. If the stack is already full, `x` is discarded and `remain` decreases. That `else` branch accounts for deletions that happen after the desired subsequence has already been filled.

For `nums = [3,4,6,5]` and requested length `2`, the initial deletion budget is `2`:

- select `3`;
- on `4`, remove the smaller `3`, spend one deletion, and select `4`;
- on `6`, remove the smaller `4`, spend the last deletion, and select `6`;
- with no deletions left, append `5`.

The result is `[6,5]`. It is better than every other length-two subsequence because its first digit is the greatest achievable first digit, and, subject to that choice, its second digit is greatest.

The stack does not remove an equal preceding digit. Replacing an earlier equal digit with a later copy cannot improve the current position and would leave fewer future digits available. Keeping the earlier equal occurrence is therefore at least as flexible.

The standard greedy reasoning can be applied at every pop: whenever a smaller chosen digit can legally be deleted in favor of the current larger digit, any candidate that keeps the smaller digit loses at their first differing position. When a digit cannot be popped, either it is at least as large as the current digit or no deletion budget remains. In the first case keeping it is lexicographically safe; in the second case deleting it would make an exact-length result impossible. Thus `f` returns the greatest subsequence of the requested length.

The helper also handles a requested length of zero. `stk` is empty, every input digit goes through the discard branch, and the returned subsequence is `[]`. This is necessary for splits that take all $k$ digits from only one source.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[9, 8, 6, 5, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [3, 4, 6, 5], "nums2": [9, 1, 2, 5, 8, 3], "k": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[9, 8, 6, 5, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare only the current heads:** This works w:** - **Compare only the current heads:** This works when the digits differ but fails on ties. With `[6,7]` and `[6,0,4]`, the suffixes show that the first `6` must be taken from the first array. Complete remaining-suffix order is necessary.
- **- **Enumerate all subsequences:** Generate every l:** - **Enumerate all subsequences:** Generate every length-$x$ subsequence for every split and try every merge. This is combinatorial and unnecessary; the monotonic stack proves that only the greatest fixed-length subsequence from each source can be relevant.
- **- **Precompute suffix ranks or longest common pref:** - **Precompute suffix ranks or longest common prefixes:** The repeated recursive comparisons cause the $O(k^2)$ merge term. More elaborate ranking or next-difference preprocessing can speed comparisons, but adds implementation complexity and must be rebuilt for each chosen pair of subsequences.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $m$ and $n$ be the input lengths. There are at most $k+1$, hence $O(k)$, feasible splits. For each split, the two calls to `f` scan their complete source arrays, costing $O(m+n)$ time.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

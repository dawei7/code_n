# Guided Example: Delayed Count of Equal Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 1], "k": 1}`
- **Required output:** `[2, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and an integer `k`.

The objective is to compute `[2, 0, 0, 0]` from `{"nums": [1, 2, 1, 1], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify the first eligible position exactly

For index `i`, a matching position must satisfy

$$
i+k<j.
$$

Since indices are integers, the first eligible index is

$$
j=i+k+1.
$$

The `+1` is essential. Position `i + k` is still excluded by the strict inequality.

The delayed count asks only how many eligible suffix values equal `nums[i]`. If a frequency table contains exactly the elements from `i + k + 1` through the end, the answer is one dictionary lookup.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 1], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan right to left so the eligible suffix grows by one

As `i` decreases by one, the eligibility boundary also decreases by one:

$$
(i-1)+k+1=i+k.
$$

The new index gains exactly one additional eligible position compared with the previous index. This makes a right-to-left frequency scan natural.

The source maintains `cnt` with the invariant:

> Immediately before assigning `ans[i]`, `cnt` contains the frequencies of values at every index from `i + k + 1` through `n - 1`, and no earlier index.

It restores this invariant by adding the new boundary value:

`cnt[nums[i + k + 1]] += 1`.

It then reads:

`ans[i] = cnt[nums[i]]`.

That lookup counts exactly the eligible positions whose value equals the current one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the correct starting index

An index has at least one eligible position only when

$$
i+k+1\le n-1.
$$

Rearranging gives

$$
i\le n-k-2.
$$

The loop therefore begins at `n - k - 2` and descends to zero:

`range(n - k - 2, -1, -1)`.

Every index greater than `n - k - 2` has an empty eligible suffix and must receive zero. The source initializes `ans = [0] * n`, so these trailing positions are already correct and do not need loop iterations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 1], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct nested counting:** For each `i`, scan from `i + k + 1` to the end. This is simple but costs $O(N^2)$ when `k` is small.
- **Positions list plus binary search:** Store sorted occurrence indices for each value, then binary-search the first index greater than `i + k`. This costs $O(N\log N)$ total and can answer arbitrary delayed queries.
- **Full suffix-frequency snapshots:** Building a map for every starting point supports lookup but can consume $O(N^2)$ copied state. The rolling Counter stores only the current suffix.
- **k equals zero:** Every equal occurrence strictly to the right is counted.
- **k equals n - 1:** No index has an eligible later position, the loop is empty, and all answers remain zero.
- **Strict inequality boundary:** Index `i + k` is excluded; adding `i + k + 1` is the correct first position.
- **Trailing indices:** Those with no eligible suffix retain the zero values created during answer initialization.
- **All values equal:** `ans[i]` equals the number of indices from `i + k + 1` through the end.
- **All values distinct:** Every Counter lookup for the current value returns zero.
- **One element:** The loop is empty for the only allowed `k = 0`, and the answer is `[0]`.
- **Missing Counter key:** It evaluates to zero naturally, matching “no eligible equal value.”
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. The loop runs $N-k-1$ times when that value is positive. Each iteration performs one expected $O(1)$ Counter increment and one expected $O(1)$ lookup. Worst-case time over allowed `k` is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

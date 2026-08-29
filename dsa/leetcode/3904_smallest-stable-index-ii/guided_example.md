# Guided Example: Smallest Stable Index II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 0, 1, 4], "k": 3}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and an integer `k`.

The objective is to compute `3` from `{"nums": [5, 0, 1, 4], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The repeated-work problem

At consecutive indices, the ranges overlap almost completely. Prefix $0..i+1$ differs from prefix $0..i$ by only one element. Suffix $i..n-1$ differs from suffix $i+1..n-1$ by only one element.

Recomputing `max(nums[:i + 1])` and `min(nums[i:])` independently would ignore that overlap. Across all indices, the total number of examined entries would grow quadratically.

The source summarizes each changing range with the recurrence that adds its one new endpoint.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 0, 1, 4], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Backward construction of every suffix minimum

Define

$$
R_i=\min_{i\le j<n}\texttt{nums}[j].
$$

The base case is $R_{n-1}=\texttt{nums}[n-1]$. For $i<n-1$,

$$
R_i
=
\min(\texttt{nums}[i],R_{i+1}).
$$

The list `right` stores these $R_i$ values. It is initially filled with the last array value, which establishes the correct final entry. The loop then moves backward, so `right[i + 1]` is already correct when `right[i]` is assigned.

After this pass, looking up the smallest value from any index through the end costs $O(1)$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Forward maintenance of the prefix maximum

Define

$$
L_i=\max_{0\le j\le i}\texttt{nums}[j].
$$

The forward recurrence is

$$
L_i=\max(L_{i-1},\texttt{nums}[i]).
$$

The scalar `left` holds this value. At the start of each loop iteration, it summarizes the previous prefix; after `left = max(left, x)`, it summarizes the current inclusive prefix.

The source begins with zero. That works because the contract guarantees nonnegative input values, so zero cannot incorrectly exceed a real prefix maximum. More generally, one could initialize from `nums[0]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 0, 1, 4], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Quadratic direct evaluation:** Compute a fresh prefix maximum and suffix minimum for each $i$. It matches the definition but cannot scale to $10^5$ elements.
- **Two full aggregate arrays:** Prefix maxima plus suffix minima make every score a constant-time lookup, but the source saves one array by maintaining the prefix online.
- **Segment tree:** Range maximum and minimum queries would cost $O(\log N)$ per index after preprocessing, making the solution slower and more complex than static linear passes.
- **Sparse table:** Constant-time range queries after $O(N\log N)$ preprocessing are unnecessary because only one fixed prefix and suffix per index are queried.
- **Single-element array:** Its score is always zero, making index 0 the answer for any nonnegative $k$.
- **Threshold equality:** A score exactly equal to $k$ qualifies.
- **Current element belongs to both ranges:** The update order and suffix recurrence both preserve the inclusive definition.
- **Score is not guaranteed monotone:** Prefix maxima never decrease and suffix minima never decrease as $i$ moves right, but their difference can move in either direction; binary search is unsafe.
- **Large values:** Values and $k$ up to $10^9$ fit comfortably in Python integers, and subtraction is exact.
- **Nonnegative initialization:** `left = 0` is valid only because the documented domain excludes negative values.
- **No qualifying index:** The source returns `-1` only after testing every exact score in ascending index order.
- **No input mutation:** The algorithm allocates its own suffix list and does not reorder or overwrite `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length. Filling `right`, computing its suffix recurrence, and scanning candidates each take linear time. The total is
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

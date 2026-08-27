# Guided Example: Maximum Total Subarray Value I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2], "k": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and an integer `k`.

The objective is to compute `4` from `{"nums": [1, 3, 2], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Bounding every subarray value

Let

$$
M=\max(\texttt{nums})
$$

and

$$
m=\min(\texttt{nums}).
$$

For any subarray `nums[l..r]`, its maximum cannot exceed the maximum of the entire array:

$$
\max(\texttt{nums}[l..r])\le M.
$$

Likewise, its minimum cannot be smaller than the global minimum:

$$
\min(\texttt{nums}[l..r])\ge m.
$$

Subtracting the second relationship from the first gives:

$$
\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r])
\le M-m.
$$

Thus no individual subarray can have value greater than the global range $M-m$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Attaining the global range

An upper bound is useful only if some legal subarray reaches it. The entire array is itself a nonempty subarray. It contains both an occurrence of $M$ and an occurrence of $m$, so its maximum is $M$, its minimum is $m$, and its value is exactly $M-m$.

A smaller subarray spanning an occurrence of the global minimum and an occurrence of the global maximum also attains this value, regardless of which one appears first. The source does not need to locate those indices because the whole array always supplies a simple witness.

Therefore, the maximum value of one selectable subarray is exactly:

$$
V=M-m.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An upper bound is useful only if some legal subarray reaches... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Using repetition to optimize exactly $k$ choices

Each of the $k$ chosen subarrays contributes at most $V$, so any total is bounded by:

$$
kV.
$$

The contract explicitly permits choosing the same pair of endpoints repeatedly. Select the entire array $k$ times. Every selection contributes $V$, giving total $kV$ and attaining the upper bound.

This removes all interaction among the $k$ choices. There is no need to find the second-best subarray, reserve endpoints, or prevent overlap. Repetition is legal, and the choices do not modify the array.

For `nums = [4, 2, 5, 1]`, the global maximum is $5$ and the global minimum is $1$, so $V=4$. With `k = 3`, selecting the entire array three times gives $3\cdot4=12$.

For `nums = [1, 3, 2]`, $V=3-1=2$. Selecting any value-two subarray twice produces total four. The examples use two different subarrays, but the rules would also permit selecting `nums[0..2]` twice.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subarrays:** Computing every sub:** - **Enumerate all subarrays:** Computing every subarray range takes at least $O(n^2)$ candidates and is unnecessary because the entire array already attains the global upper bound.
- **Find the best $k$ distinct subarrays:** That solves the harder follow-up version, not this contract. Here, identical endpoints may be selected repeatedly.
- **Locate the minimum and maximum indices:** Their positions are unnecessary. The entire array contains both values and is always a legal witness.
- **Single-pass extrema:** Tracking `low` and `high` together avoids the second scan but remains $O(n)$ time and $O(1)$ space. It is a valid alternative, not the exact source form.
- **One-element array:** The global maximum equals the global minimum, every subarray value is zero, and the answer is zero for every legal $k$.
- **All elements equal:** The same zero-range reasoning applies even when the array has many possible subarrays.
- **Minimum appears after maximum:** Endpoint order does not matter because the subarray spanning both positions includes both extrema.
- **Multiple global extrema:** Any subarray containing at least one global minimum and one global maximum attains the same best value.
- **Large `k`:** No additional search is required. Repetition turns the answer into direct multiplication, but the total should use sufficiently wide integer arithmetic.
- **Overlapping selections:** Overlap is explicitly allowed and selections do not consume elements. Choosing one subarray places no restriction on the next choice.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

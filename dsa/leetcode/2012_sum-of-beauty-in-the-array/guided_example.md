# Guided Example: Sum of Beauty in the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. For each index `i` ($1 \le i \le \text{nums.length} - 2$) the **beauty** of $\text{nums}[i]$ equals:

The objective is to compute `2` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace universal comparisons with extrema

Beauty two requires every value left of index `i` to be smaller than `nums[i]` and every value right of it to be larger.

The left condition is equivalent to

$$
\max(\text{left values})<\texttt{nums}[i],
$$

and the right condition is equivalent to

$$
\texttt{nums}[i]<\min(\text{right values}).
$$

Knowing one prefix maximum and one suffix minimum is therefore enough to replace two potentially linear scans at each index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute suffix minima

`right[i]` stores the minimum of `nums[i:]`. The array begins filled with the final value. Scanning from `n-2` down to zero applies

`right[i] = min(right[i + 1], nums[i])`.

By induction, `right[i+1]` is exactly the minimum strictly right of index `i`.

During the later scan, the source sets `r = right[i + 1]` so the current value is excluded from the right side.

There is no need to store a matching prefix-maximum array. The forward loop encounters left values in exactly the order needed, so one scalar can summarize them. The right side cannot be summarized the same way during a forward scan because its values have not yet been visited; that asymmetry explains why the implementation precomputes only suffix minima and rolls only the prefix maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `right[i]` stores the minimum of `nums[i:]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the left maximum incrementally

Variable `l` starts as `nums[0]`. Before testing index one, this is the maximum of all values strictly left of it.

After testing index `i`, the update `l = max(l, nums[i])` prepares the prefix maximum for index `i+1`. Updating after the test is essential; otherwise the current value would be included in its own left side.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix-max and suffix-min arrays:** Store both:** - **Prefix-max and suffix-min arrays:** Store both sides explicitly; still $O(N)$ time but uses another $O(N)$ array instead of rolling `l`.
- **Scan all left and right values per index:** Direct but takes $O(N^2)$ time.
- **Monotonic structures:** Unnecessary because static prefix and suffix extrema are simpler.
- **Strictly increasing array:** Every eligible index has beauty two, so total is $2(N-2)$.
- **Strictly decreasing array:** Every eligible index has beauty zero.
- **Duplicate boundary value:** Prevents beauty two because inequalities are strict.
- **Global condition succeeds:** Do not also add local beauty one.
- **Global fails but local succeeds:** Add exactly one.
- **Length three:** There is exactly one eligible middle index.
- **Large values:** Only comparisons and small beauty sums are used.
- **Update order:** Test with current excluded from `l`, then incorporate it.
- **Right index:** Use `right[i+1]`, not `right[i]`.
- **Input preservation:** The method creates a separate suffix array.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be array length. Building suffix minima takes $O(N)$ time, and the forward beauty scan takes $O(N)$ time. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

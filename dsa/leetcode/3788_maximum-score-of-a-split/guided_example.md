# Guided Example: Maximum Score of a Split

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, -1, 3, -4, -5]}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `17` from `{"nums": [10, -1, 3, -4, -5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute the minimum to the right of every boundary

For split index `i`, the prefix ends at `i` while the suffix begins at `i+1`. The score needs the minimum value in that entire suffix.

The source creates `suf` so that

$$
\texttt{suf}[i]=\min(\texttt{nums}[i],\ldots,\texttt{nums}[N-1]).
$$

It initializes every position with `nums[-1]` and then fills indices from `n-2` down to zero using

`suf[i] = min(nums[i], suf[i+1])`.

The last position is correct initially because a one-element suffix has that element as its minimum. If `suf[i+1]` is the minimum from `i+1` onward, comparing it with `nums[i]` gives the minimum from `i` onward. This backward recurrence establishes the whole array.

For `[4,2,7,1]`, initialization places 1 at the last position. Moving left produces `suf[2]=min(7,1)=1`, then `suf[1]=min(2,1)=1`, and finally `suf[0]=min(4,1)=1`. This trace shows that a distant minimum propagates through every earlier suffix that contains it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, -1, 3, -4, -5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build each prefix sum incrementally

The second loop scans valid split indices `0` through `n-2`. Before evaluating index `i`, it adds `nums[i]` to `pre`.

After this update,

$$
\texttt{pre}=\sum_{j=0}^{i}\texttt{nums}[j],
$$

which is exactly `prefixSum(i)`. The required suffix minimum is `suf[i+1]`, not `suf[i]`, because the split element belongs to the prefix.

The candidate is therefore

`pre - suf[i+1]`.

Each iteration updates `ans` with the larger of its current value and this candidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The second loop scans valid split indices `0` through `n-2`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep prefix and suffix roles separate

The score subtracts one suffix value—the minimum—not the suffix sum. The precomputation stores only minima, while `pre` stores only the cumulative prefix total.

For `[10,-1,3,-4,-5]`, suffix minima are `[-5,-5,-5,-5,-5]`. At split two, `pre=12` and the suffix beginning at three has minimum -5, giving $12-(-5)=17$.

At split three, the prefix becomes eight and the suffix minimum remains -5, giving 13. The running maximum correctly retains 17.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, -1, 3, -4, -5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Right-to-left constant-space scan:** With the :** - **Right-to-left constant-space scan:** With the total sum and a running suffix minimum, one can evaluate splits without storing every suffix minimum. That matches the manifest space claim but is not the exact source.
- **Recompute each suffix minimum:** Calling `min(nums[i+1:])` for every split can cost $O(N^2)$ and allocate repeated slices.
- **Use suffix sum instead of minimum:** The contract subtracts one minimum value, not the suffix total.
- **Use `suf[i]`:** That incorrectly allows the split element itself into the suffix minimum.
- **Initialize answer to zero:** All legal scores may be negative.
- **Two-element array:** There is one split; `pre=nums[0]` and `suf[1]=nums[1]`.
- **All positive values:** A later prefix can grow, but its shrinking suffix may also change the minimum; every split is still needed.
- **All negative values:** Subtracting a negative suffix minimum can raise the score, but the maximum may remain negative.
- **Repeated minima:** The recurrence preserves their value without needing positions.
- **Minimum at the final element:** It propagates left through every suffix containing it.
- **Large magnitudes:** Python arithmetic safely handles cumulative sums.
- **Input preservation:** Only `suf` and scalars are updated.
- **Source/manifest mismatch:** The exact file uses linear auxiliary storage.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Filling `suf` takes $O(N)$ time. Evaluating all $N-1$ split points also takes $O(N)$ time, so total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

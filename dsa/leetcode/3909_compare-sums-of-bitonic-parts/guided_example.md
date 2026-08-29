# Guided Example: Compare Sums of Bitonic Parts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **bitonic** array `nums` of length `n`.

The objective is to compute `1` from `{"nums": [1, 3, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recognizing where the peak occurs

For adjacent values `a = nums[i]` and `b = nums[i + 1]`:

- before the peak, strict increase gives $a<b$;
- at the peak boundary, $a>b$, with `a` equal to the peak.

Because the input is guaranteed bitonic, the first pair satisfying `a > b` identifies the transition. There is no plateau case $a=b$ under the contract.

The loop uses `pairwise(nums)`, which produces consecutive pairs in index order. It stops before processing the descending boundary pair.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the ascending sum

The variable `l` begins as `nums[0]`. For every increasing pair $(a,b)$ before the peak, `b` is the next value in the ascending part, so the source performs



If the increasing pairs processed so far end at index $t$, then

$$
\texttt{l}
=
\sum_{i=0}^{t}\texttt{nums}[i].
$$

When the last increasing pair $(\texttt{nums}[p-1],\texttt{nums}[p])$ is processed, the peak is added. The following pair $(\texttt{nums}[p],\texttt{nums}[p+1])$ is descending, so the loop breaks without adding a post-peak value.

Thus `l` equals $A$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deriving the descending sum from the total

The variable `r` starts as `sum(nums)`. During every increasing pair $(a,b)$, `a` is known to occur strictly before the peak, so it does not belong to descending part $p..n-1$. The source removes it:



Across all processed increasing pairs, the removed values are exactly

$$
\texttt{nums}[0],\texttt{nums}[1],\ldots,\texttt{nums}[p-1].
$$

The peak `nums[p]` is never removed, because it appears as `b` in the final increasing pair and then as `a` in the first descending pair, where the loop breaks before subtraction.

Therefore the remaining total is

$$
\texttt{r}
=
\sum_{i=p}^{n-1}\texttt{nums}[i]
=B.
$$

This careful update order is exactly what counts the peak once in each part.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Find the peak, then sum two slices:** This is straightforward but may allocate slice copies in Python; using index ranges avoids copies but still makes additional passes.
- **Track two sums from scratch:** Once the peak is known, another scan can compute both inclusive sums. The source folds peak detection and boundary adjustment into one pass after the total.
- **Binary-search the peak:** Bitonic structure permits $O(\log N)$ peak discovery, but both part sums still require prefix-sum preprocessing or linear work; it does not improve the complete one-query task.
- **Peak counted twice by definition:** It must remain in both `l` and `r`; subtracting it from the total at the break would be wrong.
- **Equal sums:** The source returns `-1` before checking either winner.
- **Peak near the beginning:** The first descending pair stops the loop with `l` containing only the peak-side prefix and `r` retaining the full descending part.
- **Peak near the end:** Most adjacent pairs are processed; the last value added to `l` is still preserved in `r` as the shared peak.
- **Strict bitonic guarantee:** The source uses only `a > b` as the stopping signal. Equal adjacent values would violate the contract and blur the peak boundary.
- **Positive values:** Positivity is not required for the invariant itself, but it is guaranteed by the problem.
- **Required helper:** Standalone execution needs `pairwise` from Python's `itertools` module.
- **Input preservation:** Neither summation nor pair iteration changes `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length. Computing `sum(nums)` scans all $N$ values once. `pairwise` then visits adjacent pairs only until the peak transition, at most $N-1$ pairs.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

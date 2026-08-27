# Guided Example: Absolute Difference Between Maximum and Minimum K Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 2, 2, 4], "k": 2}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `5` from `{"nums": [5, 2, 2, 4], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Expose both extreme groups by sorting

The exact source sorts `nums` in nondecreasing order. After sorting:

- `nums[:k]` contains the `k` smallest occurrences;
- `nums[-k:]` contains the `k` largest occurrences.

Occurrences matter. If a value appears several times near an extreme, each copy occupies a sorted position and may contribute separately.

The two groups are chosen independently. Their slices may overlap when `2*k > n`, which is allowed. Sorting still identifies each requested group correctly; overlap does not mean an occurrence must be removed from one group because it appears in the other.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 2, 2, 4], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Subtract smallest sum from largest sum

The source returns

`sum(nums[-k:]) - sum(nums[:k])`.

Although the statement asks for an absolute difference, this subtraction is already nonnegative. Pair the sorted smallest values `nums[0]` through `nums[k-1]` with the sorted largest values `nums[n-k]` through `nums[n-1]`. For every pair position $t$,

$$
\texttt{nums}[n-k+t]\ge\texttt{nums}[t],
$$

because the left index is no smaller than the right index when `k <= n`. Summing these inequalities proves that the largest-group sum is at least the smallest-group sum.

Therefore

$$
\left|\text{largest sum}-\text{smallest sum}\right|
=\text{largest sum}-\text{smallest sum},
$$

and no explicit `abs` call is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source returns

`sum(nums[-k:]) - sum(nums[:k])`.

Altho... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace duplicates and overlap correctly

For `[5,2,2,4]` with `k=2`, sorting gives `[2,2,4,5]`. The first slice sums to four, the last slice sums to nine, and the returned difference is five.

For `[1,2,3]` with `k=2`, the smallest group is `[1,2]` and the largest is `[2,3]`. The middle occurrence belongs to both independently chosen groups. The two sums are three and five, so the result is two.

When `k=n`, both slices are the entire sorted list. Their sums are equal and the result is zero.

Slice boundaries remain correct at every legal `k`. Negative indexing makes `-k` equal to `n-k`, the first position of the largest group. Because `k>=1`, neither requested slice is accidentally empty. Because `k<=n`, both boundaries stay inside the list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 2, 2, 4], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency array over values 1 through 100:** I:** - **Frequency array over values 1 through 100:** It can achieve the manifest's $O(N+V)$ time and $O(V)$ space, but it is not the exact implementation.
- **Two heaps or selection algorithms:** They can avoid a full sort for small `k`, at the cost of more complicated logic.
- **Use `abs` explicitly:** It is harmless but unnecessary because the largest `k`-sum cannot be smaller than the smallest `k`-sum.
- **Choose distinct values only:** The problem selects elements, so duplicate occurrences count separately.
- **Forbid overlap:** The two groups are independent and may share occurrences when `2*k>n`.
- **`k=1`:** The result is maximum value minus minimum value.
- **`k=n`:** Both sums use the whole array and the answer is zero.
- **Single-element array:** It is the `k=n=1` case and returns zero.
- **All values equal:** Both sums are identical for every legal `k`.
- **Many boundary duplicates:** Any tied occurrences can fill the extreme positions without changing the sums.
- **Positive values:** Positivity is not needed for the sorted-order proof; the same subtraction remains nonnegative even for generalized signed values.
- **Input mutation:** Callers needing the original order would have to sort a copy.
- **Source/manifest mismatch:** Complexity for this source must include full sorting and slice allocation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N+K)$. Sorting $N$ occurrences takes $O(N\log N)$ worst-case time. Each length-`k` slice is created and summed in $O(K)$ time, so the total is $O(N\log N+K)=O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

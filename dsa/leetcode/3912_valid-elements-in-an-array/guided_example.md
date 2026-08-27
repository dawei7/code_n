# Guided Example: Valid Elements in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 4, 2, 3, 2]}`
- **Required output:** `[1, 2, 4, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[1, 2, 4, 3, 2]` from `{"nums": [1, 2, 4, 2, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precomputing suffix maxima

The list `right` is defined by

$$
\texttt{right}[i]
=
\max(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The final suffix contains only the last value, giving the base case

$$
\texttt{right}[n-1]=\texttt{nums}[n-1].
$$

For an earlier index:

$$
\texttt{right}[i]
=
\max(\texttt{nums}[i],\texttt{right}[i+1]).
$$

The source computes this recurrence from right to left. Once complete, `right[i + 1]` is the maximum of every element strictly to the right of index $i$.

Using $i+1$ rather than $i$ is crucial. The condition compares `nums[i]` only with other elements to its right; including itself in the comparison would make strict `x > maximum` impossible.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 4, 2, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintaining the maximum strictly to the left

The variable `left` is updated after the current element is tested. At the start of iteration $i$, it therefore equals

$$
\max(\texttt{nums}[0],\ldots,\texttt{nums}[i-1])
$$

for $i>0$.

The condition `x > left` is exactly “the current value is strictly greater than every value to its left.”

The source initializes `left` to zero. Input values are positive, so the first value is always greater than this sentinel and is included automatically. After each decision:



extends the summary to include the current value for the next index.

Updating before the test would be wrong: `left` would then be at least `x`, preventing any strict left-record condition from succeeding.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `left` is updated after the current element is ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handling the last position safely

The last element is always valid, but it has no `right[i + 1]` entry. The source's condition is:



Python evaluates `or` from left to right and stops once a term is true. At the last index, `i == n - 1` is true, so `right[i + 1]` is never accessed. This both includes the required endpoint and avoids an out-of-range lookup.

For earlier positions, the third term compares `x` against the precomputed maximum strictly to its right.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 4, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 4, 2, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 4, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan both sides for every element:** This mirr:** - **Scan both sides for every element:** This mirrors the definition directly but costs $O(N^2)$ because the same ranges are repeatedly examined.
- **Two record-marker arrays:** Mark left records in one pass and right records in another, then emit their union. It also costs $O(N)$ space but stores more state than the source.
- **Use a right-to-left result set:** Combining valid indices in a set can lose ordering unless a final forward pass is added; the source emits in order directly.
- **Single element:** It is both first and last and is appended exactly once.
- **First element:** The positive-value contract and `left = 0` make it pass the left condition.
- **Last element:** The explicit index test includes it and short-circuits the unavailable suffix lookup.
- **Equal values:** Equality fails both strict comparisons; only endpoint rules may still make such occurrences valid.
- **Strictly increasing array:** Every element is a new left record, so all values are returned.
- **Strictly decreasing array:** Every element exceeds everything to its right, so all values are returned.
- **Interior global maximum:** It passes both directional conditions but is appended only once.
- **Positive-value assumption:** Initializing `left` to zero relies on all values being at least one. Negative inputs would require negative infinity or separate first-index handling.
- **Original order:** Appending during the forward scan guarantees the result is not sorted by value or discovery direction.
- **Input preservation:** Suffix information is stored separately; the original array remains unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. The backward suffix pass visits $N-1$ indices. The forward decision pass visits all $N$ indices.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

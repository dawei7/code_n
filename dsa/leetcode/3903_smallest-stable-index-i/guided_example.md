# Guided Example: Smallest Stable Index I

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

### Step 1: Why the suffix side is prepared first

When testing index $i$ during a left-to-right scan, the prefix `nums[0..i]` has already been seen, but the suffix `nums[i..n-1]` mostly lies ahead. The source stores the needed future information in `right`, where

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The last suffix contains only `nums[n-1]`, so

$$
\texttt{right}[n-1]=\texttt{nums}[n-1].
$$

For every earlier index, the suffix beginning at $i$ consists of `nums[i]` followed by the suffix beginning at $i+1$. Therefore

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i],\texttt{right}[i+1]).
$$

The backward loop evaluates exactly this recurrence from $n-2$ down to 0. When it finishes, every candidate index can retrieve its suffix minimum in constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 0, 1, 4], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintaining the prefix maximum

The variable `left` represents

$$
\max(\texttt{nums}[0..i])
$$

at the moment index $i$ is checked.

Before the scan, `left` is zero. This initialization is safe because every array value is nonnegative. At index $i$ with current value `x`, the update



extends the previous prefix by one element. After it executes:

- every earlier prefix element was already summarized by the old `left`; and
- `x` is the newly included endpoint.

Their maximum is exactly the current inclusive prefix maximum.

The update happens before the stability test because `nums[i]` belongs to both ranges in the definition. Testing first would accidentally use prefix `nums[0..i-1]` and omit the current element.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `left` represents

$$
\max(\texttt{nums}[0..i])... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Testing the exact instability score

At index $i$, the source now has:

$$
\texttt{left}
=
\max(\texttt{nums}[0..i])
$$

and

$$
\texttt{right}[i]
=
\min(\texttt{nums}[i..n-1]).
$$

Their difference is exactly the specified instability score. The condition



uses an inclusive comparison, so a score equal to $k$ is stable.

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

- **- **Recompute both ranges at every index:** This d:** - **Recompute both ranges at every index:** This direct method is easy to derive but costs $O(N^2)$ time because overlapping prefixes and suffixes are rescanned.
- **Prefix and suffix arrays:** Storing both aggregates also gives $O(N)$ time but uses two $O(N)$ arrays; the running variable removes the need for the prefix array.
- **Range-query structures:** Segment trees or sparse tables can answer maxima and minima, but they add complexity without improving this one-pass static problem.
- **Single element:** Both the prefix maximum and suffix minimum equal that value, so the score is zero and index 0 is stable for every allowed $k$.
- **Score equal to \(k\):** The index is stable because the comparison is `<=`, not strict.
- **Non-monotone scores:** The score need not change monotonically with $i$, so binary search on indices is not justified; scanning in order is safe.
- **Repeated values:** `min` and `max` naturally handle duplicates, and no special counting is required.
- **All zeros:** Every score is zero, so index 0 is returned.
- **Nonnegative-value assumption:** Initializing `left` to zero relies on all values being at least zero. With unrestricted negatives, initialization should use the first element or negative infinity.
- **No stable index:** Exhausting the ascending scan proves every candidate failed, so the method returns `-1`.
- **Input preservation:** Only `right` and scalar variables are changed; `nums` retains its original contents.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. Initializing `right` creates $N$ entries. The backward pass processes $N-1$ indices, and the forward pass processes at most $N$ indices.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

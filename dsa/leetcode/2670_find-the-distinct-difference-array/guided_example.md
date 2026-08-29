# Guided Example: Find the Distinct Difference Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5]}`
- **Required output:** `[-3, -1, 1, 3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of length `n`.

The objective is to compute `[-3, -1, 1, 3, 5]` from `{"nums": [1, 2, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute distinct suffix counts

At index $i$, the required suffix excludes `nums[i]` and begins at $i+1$.

The solution first builds array `suf` where:

$$
\texttt{suf[i]}
=
\#\text{ distinct values in }\texttt{nums[i..n-1]}.
$$

An extra entry `suf[n] = 0` represents the empty suffix after the last index.

This lets the second pass read the required suffix count as `suf[i + 1]` in constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build suffix values from right to left

Set `s` begins empty. For `i` descending from $n-1$ to zero:

- add `nums[i]` to the set;
- assign `suf[i] = len(s)`.

The set contains exactly the values from current index through the end.

Repeated occurrences do not increase set size, which is precisely the meaning of distinct count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the extra array entry avoids a special case

For final index $n-1$, the required suffix `nums[n..n-1]` is empty.

Reading `suf[n]` returns initialized zero. No conditional is needed inside the forward pass.

This sentinel-style entry makes the same formula valid at every index.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-3, -1, 1, 3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-3, -1, 1, 3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Suffix frequency map updated forward:** Start with all counts, remove current value, and track distinct suffix size while building prefix set; also $O(n)$.
- **Rebuild prefix and suffix sets per index:** Correct but $O(n^2)$.
- **Frequency arrays:** Values are bounded by 50, so fixed arrays can replace sets.
- **Single element:** Prefix distinct count is one, empty suffix count zero, result `[1]`.
- **All values distinct:** Prefix size rises while suffix size falls predictably.
- **All values equal:** Every nonempty prefix/suffix has distinct count one; final suffix is zero.
- **Empty suffix:** `suf[n]=0` handles the final index.
- **Negative difference:** It is valid and must not be clamped.
- **Repeated prefix value:** Set size remains unchanged.
- **Input preservation:** No mutation or sorting occurs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The backward and forward passes each visit $n$ elements. Expected set insertion is $O(1)$, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

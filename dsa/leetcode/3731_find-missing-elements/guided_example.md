# Guided Example: Find Missing Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 2, 5]}`
- **Required output:** `[3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` consisting of **unique** integers.

The objective is to compute `[3]` from `{"nums": [1, 4, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The surviving endpoints reveal the original range

The contract guarantees that the smallest and largest integers of the original consecutive range are still present. Therefore,

$$
L=\min(\texttt{nums})
\quad\text{and}\quad
H=\max(\texttt{nums})
$$

are exactly the original endpoints. Every required missing value lies strictly between them, because `L` and `H` themselves are present.

The input order is arbitrary, so neighboring array positions provide no useful range information. The source first computes `mn` and `mx` by scanning all values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a set for presence tests

The statement asks which values do not occur, not where existing values occur. Converting `nums` to `s = set(nums)` provides expected constant-time membership checks. Input values are guaranteed unique, but the set would preserve the same presence information even without that guarantee.

The list comprehension then examines

`range(mn + 1, mx)`.

Python's upper range endpoint is excluded, so this generates precisely

$$
L+1,L+2,\ldots,H-1.
$$

It keeps `x` exactly when `x not in s`.

The candidates are generated in strictly increasing order, so the returned list is automatically sorted. No separate output sort is required.

For `nums = [1,4,2,5]`, the endpoints are one and five. The scan tests two, three, and four. Only three is absent, producing `[3]`.

For `nums = [5,1]`, all interior candidates two, three, and four are absent, so all are returned. For `[7,8,6,9]`, each candidate seven and eight is present, so the comprehension produces an empty list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why this returns every and only missing range element

Take any value missing from the original range. It cannot be below `mn` or above `mx` because those are the range boundaries, and it cannot equal either endpoint because both survive. Thus it appears in `range(mn+1,mx)`. Because it is missing, the set test succeeds and includes it.

Conversely, every returned `x` lies strictly between the known endpoints and is absent from the input. The original array once contained every integer in this inclusive range, so such an `x` is genuinely one of the removed elements. Increasing enumeration provides the requested order.

The approach does not need to infer how many values were removed. The range scan naturally returns zero, one, or many missing values.

The endpoint guarantee also prevents ambiguity about values outside the scan. An absent integer smaller than `mn` or larger than `mx` was never part of the stated original range, so it must not be reported. Without the guarantee that both original endpoints survived, the current minimum and maximum might be interior survivors and the original range could not be reconstructed uniquely from `nums` alone. The source correctly uses that contract fact as the boundary of all work.

Because the input values are unique, the number of present integers in the range is exactly `n`. One could derive the number of missing values as `mx - mn + 1 - n`, but that number would not identify which values to return. The membership scan both identifies them and emits them in the required order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort and enumerate gaps:** Sorting followed by expanding every adjacent gap takes $O(n\log n+R)$ time and can use less explicit membership storage. The hash-set method avoids sorting and is linear expected time.
- **Boolean array over values:** With the bound 100, a fixed presence table works in $O(n+R)$ time. A set generalizes without allocating by the maximum value.
- **Check membership in the original list:** Each candidate would require an $O(n)$ scan, producing $O(nR)$ time. The set removes that repeated work.
- **Scan from zero or one:** The original range need not begin there. Only values between the surviving minimum and maximum belong in the answer.
- **Include endpoints in the candidate loop:** They are guaranteed present, so testing them is harmless but unnecessary. The exact range excludes both.
- **No missing integers:** Every membership test fails the filter and the list comprehension returns `[]` naturally.
- **All interior integers missing:** The returned list is the complete increasing interior range.
- **Input already sorted:** The method remains correct and does not rely on or exploit that incidental order.
- **Exactly two endpoint values:** Every integer strictly between them is missing, which the range comprehension returns.
- **Adjacent endpoints:** `range(mn+1,mx)` is empty, correctly showing that there is no integer available to be missing.
- **Uniqueness guarantee:** It ensures `n` reflects distinct survivors, but the presence-based logic would also tolerate duplicates.
- **Sorted output requirement:** Iterating the numeric range in increasing order satisfies it without a final sort.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+R)$. Let `n` be the input length and let
- **Auxiliary Space Complexity:** $O(n+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

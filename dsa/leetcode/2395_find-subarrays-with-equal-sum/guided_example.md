# Guided Example: Find Subarrays With Equal Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 4]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums`, determine whether there exist **two** subarrays of length `2` with **equal** sum. Note that the two subarrays must begin at **different** indices.

The objective is to compute `true` from `{"nums": [4, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every candidate is one adjacent pair

A length-two subarray beginning at index `i` contains `nums[i]` and `nums[i+1]`. Therefore, there are exactly $n-1$ candidate sums:

$$
\texttt{nums}[0]+\texttt{nums}[1],\;
\texttt{nums}[1]+\texttt{nums}[2],\;\ldots
$$

The task asks whether any sum occurs for two different starts. It does not require the subarrays to be disjoint. Adjacent candidates may overlap in one element, as in `[4,2]` and `[2,4]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan adjacent pairs lazily

`pairwise(nums)` yields each consecutive value pair `(a, b)` exactly once, in increasing start-index order. The code computes its sum with a walrus assignment:



This both stores the sum in `x` and tests whether an earlier pair produced it.

If the sum is already present, the earlier occurrence necessarily began at a different index because the current pair has not yet been inserted. The method can return true immediately; the question asks only for existence.

If not present, `vis.add(x)` remembers it for all later starts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a set is sufficient

The algorithm does not need to remember which earlier index produced a sum. Membership alone proves that at least one different start exists. It also does not need frequencies beyond one: once a second occurrence appears, the answer is already known.

Hash sets support expected constant-time membership and insertion for integer keys, turning a comparison against all earlier sums into one lookup.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested comparison of pair sums:** It uses no set but takes $O(n^2)$ time in the worst case.
- **Sort all pair sums:** Sorting can detect adjacent equal sums in $O(n\log n)$ time and $O(n)$ space, but hashing is faster on average.
- **Fixed frequency array:** Value sums range from $-2\cdot10^9$ to $2\cdot10^9$, making a direct domain array impractical.
- **Exactly two input elements:** There is only one length-two subarray, so the method stores one sum and returns false.
- **Overlapping subarrays:** They are allowed as long as starts differ.
- **Identical pair contents:** Different positions still count as different subarrays.
- **Different contents, equal sum:** The set detects them because only the sum matters.
- **Negative sums:** They are ordinary set keys.
- **Early return:** The first repeated sum is sufficient; later candidates cannot change the Boolean answer.
- **No repetition:** Exhausting the iterator proves every start has a distinct sum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The iterator produces $n-1$ pairs. Each performs one addition plus expected $O(1)$ hash-set lookup and, unless returning, insertion. Expected total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: 4Sum II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2], "nums2": [-2, -1], "nums3": [-1, 2], "nums4": [0, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that:

The objective is to compute `2` from `{"nums1": [1, 2], "nums2": [-2, -1], "nums3": [-1, 2], "nums4": [0, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count first-half sums, not merely distinct sums

The generator `a + b for a in nums1 for b in nums2` produces one sum for every index pair from the first two arrays. `Counter(...)` maps each numerical sum to the number of pairs that create it.

Frequency is essential. If three different `(i, j)` pairs all produce sum `5`, and one `(k, l)` pair produces `-5`, those are three different valid index tuples, not one. A plain set would remember only that `5` exists and would undercount duplicates.

Even equal values at different indices count separately. The nested generator iterates occurrences, so two identical elements in one array participate as distinct choices and correctly increase the counter.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2], "nums2": [-2, -1], "nums3": [-1, 2], "nums4": [0, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match each second-half pair with its complement

For every `c` from `nums3` and every `d` from `nums4`, the second-half sum is `c + d`. To make the total zero, the first-half sum must be `-(c + d)`. The lookup `cnt[-(c + d)]` returns exactly how many first-half index pairs have that required sum.

The outer `sum(...)` adds this count for all $n^2$ second-half pairs. Python's `Counter` returns zero for a missing key, so a pair with no complement contributes nothing and needs no conditional branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the first example

For `nums1 = [1,2]` and `nums2 = [-2,-1]`, the four first-half index pairs produce:

- `1 + (-2) = -1`
- `1 + (-1) = 0`
- `2 + (-2) = 0`
- `2 + (-1) = 1`

Thus the counter is `{-1: 1, 0: 2, 1: 1}`.

For `nums3 = [-1,2]` and `nums4 = [0,2]`, the second-half sums are `-1`, `1`, `2`, and `4`. Their required complements are `1`, `-1`, `-2`, and `-4`. The first two complements occur once each, while the latter two do not occur. The total is $1+1+0+0=2$.

These two matches correspond exactly to the two index tuples listed in the example.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2], "nums2": [-2, -1], "nums3": [-1, 2], "nums4": [0, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four nested loops:** It is conceptually direct but takes $O(n^4)$ time, which is unnecessary for the separable sum equation.
- **Three loops plus a frequency map for one array:** This reduces lookup cost but still requires $O(n^3)$ time. Pairing the arrays evenly gains another factor of $n$.
- **Sort both pair-sum lists:** Build all sums for each half, sort them, and use two pointers to count opposite values. It also uses $O(n^2)$ space but costs $O(n^2\log n)$ time because of sorting.
- **Store a set of sums:** A set loses multiplicities and is incorrect whenever different index pairs produce the same sum.
- **Counter both halves:** One can multiply `left[s] * right[-s]` for each distinct sum. It is correct but may store two quadratic maps; the exact solution stores only one and scans the other lazily.
- **All zeros:** Every one of the $n^4$ index tuples sums to zero. The first counter stores key zero with frequency $n^2$, and each of the $n^2$ second pairs adds that frequency, producing $n^4$.
- **Repeated values:** Frequencies in the counter preserve every distinct index choice, even when numerical values are identical.
- **No complement:** `Counter` returns zero for a missing key, so such a second-half pair adds nothing.
- **Negative and positive values:** Negation handles both symmetrically; no ordering assumptions are used.
- **Input arrays remain unchanged:** The algorithm only iterates over them and stores derived sums.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Each of the first two arrays has length $n$, so the first generator produces $n^2$ pair sums. Building the counter takes expected $O(n^2)$ time under expected constant-time hash-table operations.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

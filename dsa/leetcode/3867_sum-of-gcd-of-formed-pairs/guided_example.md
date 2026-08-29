# Guided Example: Sum of GCD of Formed Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 6, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `2` from `{"nums": [2, 6, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the derived array exactly as defined

The pairing does not use the original `nums` values directly. First, each index `i` produces a derived value

$$
P_i=\gcd(\texttt{nums}[i],M_i),
$$

where

$$
M_i=\max(\texttt{nums}[0],\ldots,\texttt{nums}[i])
$$

is the inclusive prefix maximum.

Computing `M_i` by rescanning `nums[0:i+1]` for every index would repeat work and take quadratic time. Prefix maxima have a simple rolling recurrence:

$$
M_i=\max(M_{i-1},\texttt{nums}[i]).
$$

The source stores the current value in `mx`. It starts at zero, which is below every positive input. At each `x`, it executes `mx = max(mx,x)` and then stores `gcd(x,mx)` in `prefix_gcd[i]`.

The update must occur before the GCD because the prefix maximum is inclusive: it includes the current element. When `x` establishes a new maximum, `mx=x` and the derived value is `gcd(x,x)=x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 6, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why one scalar maximum is enough

Future indices need only the greatest value seen so far, not which position supplied it or the complete prefix. Once `mx` is updated, smaller previous values can never become a later prefix maximum. This compresses the editorial's conceptual prefix-maximum array into one scalar while still producing the full derived array required for sorting.

For `nums=[2,6,4]`:

- index zero has `mx=2` and derived value `gcd(2,2)=2`;
- index one updates `mx=6` and produces six; and
- index two keeps `mx=6` and produces `gcd(4,6)=2`.

Thus `prefix_gcd=[2,6,2]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort because pairing is based on rank

The problem next requires the smallest unpaired derived value to pair with the largest unpaired value, then the second-smallest with the second-largest, and so on. These are rank-based positions, so the source sorts `prefix_gcd` in non-descending order.

After sorting an array `a` of length `N`, pair number `i` is

$$
(a[i],a[N-1-i]).
$$

Python's negative index `-i-1` is another spelling of `N-1-i`, so the generator computes

`gcd(prefix_gcd[i], prefix_gcd[-i - 1])`.

The range `range(n // 2)` produces exactly `\lfloor N/2\rfloor` pair indices. For each such `i`, the left index is strictly less than the right index, so no element is reused. When `N` is odd, the middle index `N//2` is not included and is correctly ignored.

Summing these GCD values gives the required answer. There is no optimization over alternative pairings: sorting and opposite-end pairing are mandated by the contract, and the source simulates them directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 6, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recompute every prefix maximum:** Calling `max(nums[:i+1])` per index takes `O(N^2)` total time. A rolling maximum updates in constant time.
- **Store the full prefix-maximum array:** This follows the editorial literally and remains `O(N)` space, but one scalar `mx` is enough while building the derived list.
- **Pair original values:** Incorrect. Sorting and pairing apply to `gcd(nums[i],M_i)` values, which may differ substantially from `nums[i]`.
- **Pair before sorting:** The required pairs depend on value rank, not original position. Sorting is semantically necessary.
- **Repeatedly pop the first and last list elements:** It simulates the wording, but popping index zero from a Python list shifts elements and can make pairing `O(N^2)`. Symmetric indexing avoids mutation.
- **Two explicit pointers:** Initialize left zero and right `N-1`, add their GCD, and move inward. This is equivalent to the generator and may be easier to port to languages without negative indexing.
- **New prefix maximum:** When `nums[i]` exceeds all earlier values, the derived value is the number itself because `gcd(x,x)=x`.
- **Value below the prefix maximum:** Its derived value is a divisor shared with that maximum and may be much smaller than either value.
- **Odd length:** Exactly the sorted middle element remains unpaired. `range(N//2)` omits it automatically.
- **Singleton array:** `N//2=0`, so `sum` receives an empty generator and returns zero, matching the no-pair rule.
- **Two elements:** One symmetric pair is formed after deriving and sorting both values.
- **Duplicate derived values:** Sorting keeps all copies, and each position participates according to multiplicity. Stability of the sort is irrelevant because equal values are indistinguishable for GCD.
- **Positive-input initialization:** `mx=0` is safe because every value is at least one. With a generalized domain containing negatives, initialization and maximum semantics would need adjustment.
- **GCD import:** The protected source requires `math.gcd` or an equivalent available name.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log V)$. Let `V=max(nums)`. Constructing the derived list performs `N` GCD computations. Euclid's algorithm takes `O(\log V)` time per call, giving `O(N\log V)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Check If It Is a Good Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [12, 5, 7, 23]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of positive integers. Your task is to select some subset of `nums`, multiply each element by an integer and add all these numbers. The array is said to be **good **if you can obtain a sum of `1` from the array by any possible subset and multiplicand.

The objective is to compute `true` from `{"nums": [12, 5, 7, 23]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the subset wording into integer coefficients

The task permits selecting some array elements, multiplying each selected value by an integer, and summing the products. Not selecting a value is equivalent to assigning it coefficient zero. Therefore, the question is whether integers \(c_1,c_2,\ldots,c_n\) exist such that

\[
c_1a_1+c_2a_2+\cdots+c_na_n=1.
\]

Coefficients may be negative, as the examples show. This is exactly the setting of Bézout’s identity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [12, 5, 7, 23]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Bézout’s identity

For integers \(a_1,\ldots,a_n\), the set of all integer linear combinations is precisely the set of multiples of

\[
g=\gcd(a_1,a_2,\ldots,a_n).
\]

In particular, some integer combination equals \(g\). Every integer combination is divisible by \(g\), because \(g\) divides every input.

Consequently, a combination can equal one if and only if the GCD of the whole array is one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Necessity

Suppose the array is good, so a combination equals one. Any common divisor of all array values divides every product \(c_i a_i\), and therefore divides their sum. The greatest common divisor must divide one. Since the inputs are positive and GCD is positive, it must be one.

This proves no array with GCD greater than one can be good. For `[3,6]`, every integer combination is divisible by three, so one is impossible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [12, 5, 7, 23]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit GCD loop with early exit:** Return true as soon as the running GCD reaches one. It preserves the worst-case bound and can be faster in practice.
- **Extended Euclidean algorithm:** Also produce the actual integer coefficients witnessing the sum. It is unnecessary because the contract asks only for a Boolean.
- **Subset enumeration:** Exponential and conceptually incomplete because coefficients are unbounded integers.
- **Array contains one:** The full GCD is immediately one, so the array is good.
- **Single element greater than one:** Only its multiples are obtainable, so the result is false.
- **All values even:** Their GCD is at least two, making one impossible.
- **Pairwise GCDs greater than one:** The full array can still have GCD one; for example, several numbers may collectively remove all common factors.
- **Negative coefficients:** They are essential to Bézout’s identity and permitted by the examples.
- **Nonempty list:** The contract guarantees at least one value, so `reduce` without an initializer is safe.
- **Required imports:** Missing `reduce` or `gcd` would be an environment error, not an algorithmic issue.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log M)$. Let \(n\) be the array length and \(M\) its maximum value. Euclid’s algorithm computes a GCD in \(O(\log M)\) arithmetic steps in the conventional bound. Folding across \(n\) values therefore takes \(O(n\log M)\) time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Split Array by Prime Indices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 4]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `1` from `{"nums": [2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Global primality table

`m = 10**5 + 10` is slightly larger than the maximum array length. `primes[i]` is intended to be true exactly when index `i` is prime.

The list begins as all true, after which indices 0 and 1 are explicitly marked false. For each integer `i >= 2` still marked prime, the nested loop marks:

`2i, 3i, 4i, ...`

as composite. Every marked number has divisor `i` and is therefore not prime.

Conversely, a composite number has a prime divisor smaller than itself. When that divisor is processed, the number is marked false. Thus every table entry is correct after preprocessing.

The loop starts at `i+i` rather than the more optimized `i*i`. This repeats some markings—for example, 6 is marked when processing both 2 and 3—but does not change correctness.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Representing the two sums without constructing arrays

Let:

- `A` contain values at prime indices;
- `B` contain values at every other index.

The requested quantity is:

$$
\left|\sum A-\sum B\right|.
$$

The generator expression contributes `x` when `primes[i]` is true and `-x` otherwise:

`x if primes[i] else -x`.

Summing these signed contributions gives exactly `sum(A) - sum(B)`. Applying `abs` produces the required nonnegative difference.

The source therefore never allocates arrays `A` and `B` and never needs to compute their sums separately.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why negative values still work

The sign in the generator represents which side of the subtraction an element belongs to; it is independent of the element's own sign.

If a non-prime-index value is `-5`, its contribution is `-(-5)=+5`. This is correct because subtracting `sum(B)` subtracts every B value, including negative ones.

Similarly, a negative value at a prime index contributes negatively to `sum(A)` exactly as ordinary summation requires.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sieve only through `len(nums)-1`:** It avoids precomputing unused indices for short calls but repeats setup for every invocation.
- **Prime sum plus total sum:** Compute `prime_sum` and `total`, then use `abs(2*prime_sum-total)`. This matches the manifest summary and is algebraically equivalent.
- **Test every index individually:** Trial division per index uses less persistent memory but can cost roughly `O(n\sqrt n)` time.
- **Construct `A` and `B`:** It is straightforward but wastes `O(n)` extra storage when only their sums matter.
- **Index 0:** It is not prime and always belongs to B.
- **Index 1:** It is also not prime.
- **Index 2:** It is the first prime index and belongs to A.
- **One-element input:** A is empty, B contains `nums[0]`, and the result is `abs(nums[0])`.
- **All prime-index values absent:** This occurs only for very short arrays; the signed formula still treats A's sum as zero.
- **Negative elements:** Group membership is unchanged, and the conditional sign correctly preserves subtraction algebra.
- **Zero elements:** They contribute zero regardless of group.
- **Equal group sums:** The signed total is zero and `abs` returns zero.
- **Repeated calls:** They reuse the same global primality table without mutation.
- **Input preservation:** The method streams over `nums` and never changes its values or order.
- **Missing `List` import:** Standalone execution must provide the annotation name.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = len(nums)` and let `M = 100010` be the fixed global sieve size.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

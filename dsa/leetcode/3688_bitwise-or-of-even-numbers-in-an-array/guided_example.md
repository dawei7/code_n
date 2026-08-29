# Guided Example: Bitwise OR of Even Numbers in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5, 6]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `6` from `{"nums": [1, 2, 3, 4, 5, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recognizing even numbers

An integer `x` is even exactly when it is divisible by two, which the source tests with:

`x % 2 == 0`

The generator visits every element of `nums`. It yields `x` only when this condition is true, so odd values never reach the OR operation.

The array values are positive under the contract, but the divisibility test would also classify zero and negative integers correctly. No sorting or frequency counting is needed because inclusion depends on each value independently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What bitwise OR accumulates

Bitwise OR considers corresponding binary positions. A result bit is one if at least one included even number has a one in that position.

For example:

$$
2=010_2,\qquad 4=100_2,\qquad 6=110_2.
$$

Their OR is:

$$
010_2\mathbin{\mathrm{OR}}100_2\mathbin{\mathrm{OR}}110_2=110_2=6.
$$

Once a bit becomes one in the running result, OR can never clear it. Every new even value can only preserve existing one-bits or add more of them.

The operation is associative and commutative, so the order in which even values are combined does not affect the answer. It is also idempotent:

$$
x\mathbin{\mathrm{OR}}x=x.
$$

Therefore, repeated occurrences should still be processed as array entries, but they do not require special handling and cannot change the result after their bits are already present.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How `reduce` performs the scan

`reduce(or_, iterable, 0)` begins with accumulator zero. For each value yielded by the generator, it applies `or_(accumulator, value)` and uses the result as the next accumulator.

The imported operator function `or_` performs the same integer operation as the `|` operator. For even values $e_1,e_2,\ldots,e_m$, the reduction computes:

$$
(((0\mathbin{\mathrm{OR}}e_1)\mathbin{\mathrm{OR}}e_2)\cdots)\mathbin{\mathrm{OR}}e_m.
$$

Zero is the identity element for OR:

$$
0\mathbin{\mathrm{OR}}x=x.
$$

That makes it the correct initializer. The first even value is preserved rather than altered, and the same initialization also defines the result when no even value exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit accumulator loop:** Initialize `answer = 0` and apply `answer |= x` for each even `x`. This has the same $O(n)$ time and $O(1)$ space and is the imperative equivalent of the exact source.
- **Build a filtered list:** `reduce(or_, [x for x in nums if x % 2 == 0], 0)` is mathematically identical but allocates up to $O(n)$ temporary space. The generator avoids that list.
- **Sort before combining:** OR is order-independent, so sorting adds $O(n\log n)$ work without changing the result.
- **Use arithmetic addition:** OR and addition are different when values share set bits. For example, $2\mathbin{\mathrm{OR}}6=6$, while $2+6=8$.
- **No even values:** The initializer remains unchanged, producing the required zero rather than an exception.
- **Exactly one even value:** Zero OR that value equals the value itself, so it is returned unchanged.
- **Repeated even values:** Duplicates are harmless because OR is idempotent. A set is unnecessary.
- **Even and odd values sharing bits:** Bits from odd numbers must not contribute. Filtering happens before reduction, so their binary representation is irrelevant.
- **Value zero outside the stated positive range:** Zero is even and would pass the filter, but OR-ing zero changes nothing. The legal constraints begin at one.
- **All values even:** Every array element reaches the reduction, and the result is the ordinary OR of the entire array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

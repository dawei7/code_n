# Guided Example: Check if Any Element Has Prime Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5, 4]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `true` from `{"nums": [1, 2, 3, 4, 5, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Frequency aggregation

The Counter maps every distinct array value to its occurrence count. Values such as zero are ordinary keys; whether a value is prime is irrelevant.

For example, if value four occurs twice, the relevant number is frequency two, which is prime.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Primality test

`is_prime(x)` rejects every count below two. Frequencies of one are therefore correctly nonprime.

For larger `x`, it tests integer divisors from two through `floor(sqrt(x))`. Every composite number has a factor in that range: if both nontrivial factors exceeded the square root, their product would exceed `x`.

The expression `all(x%i for i in range(...))` treats nonzero remainders as true. The first zero remainder makes `all` false. If no divisor exists, all remainders are nonzero and the count is prime.

For frequency two or three, the divisor range is empty and `all(empty)` is true, correctly recognizing both primes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Short-circuit result

`any(is_prime(x) for x in cnt.values())` stops at the first prime frequency. Since the requested result is Boolean, later counts cannot change true back to false.

If the generator finishes, every distinct value’s frequency was tested and none was prime, proving false.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precompute prime counts:** Since frequencies are at most 100, a small sieve can mark all possible prime frequencies once. This also yields linear time but is unnecessary for one call.
- **Hard-code primes through 100:** It works under current bounds but is less adaptable and obscures the definition.
- **Test array values for primality:** This answers the wrong question; only counts matter.
- **All frequencies one:** One is not prime, so false.
- **Frequency two:** It is the smallest prime and returns true.
- **Frequency zero:** Counter never stores absent values; zero is irrelevant.
- **Value zero:** Its frequency is tested normally.
- **Several prime frequencies:** Boolean short-circuit may stop after the first.
- **Composite square:** The inclusive square-root endpoint finds its square-root divisor.
- **Empty divisor range:** It correctly accepts two and three only after the `x<2` guard rejects zero and one.
- **Repeated large group:** Trial division stops early for many composites and remains within the linear aggregate bound.
- **Counter ordering:** It may change which prime group is discovered first, never the Boolean answer.
- **Input preservation:** Counting reads the list without mutation.
- **Floating square root:** Frequencies are at most 100, so integer conversion of `sqrt` is safe; an integer square root is preferable for unbounded values.
- **One dominant value:** If all `n` elements are equal, the answer is exactly whether `n` is prime. Counter produces one group, so the helper tests that condition directly without any special branch.
- **Mixed group sizes:** A composite frequency does not disqualify the array when another value has a prime frequency. The use of `any` expresses this existential requirement, whereas `all` would incorrectly demand every frequency be prime.
- **Why distinct value count is bounded:** Counter has one entry per value that actually occurs, so `d\le n`. This fact is required in the aggregate trial-division proof and also bounds storage even though allowed numeric values span zero through one hundred.
- **Trial division endpoint:** Testing through `int(sqrt(x))+1` includes an exact square root. Without the inclusive endpoint, a count such as four or nine could be misclassified as prime.
- **No need to identify the element:** The method returns only a Boolean. Counter keys are retained for grouping, but once frequencies exist, `any` consumes only their counts and does not reconstruct which key caused success.
- **Expected hash behavior:** Counter construction and value access use expected constant-time hashing. The `O(n)` statement follows the standard hash-table model; adversarial hash behavior is outside the conventional bound.
- **Early success and complexity:** Short-circuiting often saves work, but the worst-case analysis assumes every stored frequency is nonprime and therefore every group is inspected.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Counter construction is `O(n)` expected time. Aggregate primality work is `O(n)` by the bound above, so total expected time is `O(n)`.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Three Divisors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10000}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return `true`* if *`n`* has **exactly three positive divisors**. Otherwise, return *`false`.

The objective is to compute `false` from `{"n": 10000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count divisors strictly between one and $n$

For every integer $n>1$, both one and $n$ are positive divisors. Therefore $n$ has exactly three positive divisors precisely when there is exactly one additional divisor in the range from two through $n-1$.

The exact solution tests every integer in that range:

`n % i == 0 for i in range(2, n)`.

The remainder is zero exactly when `i` divides `n`. Each comparison produces a Boolean, and Python sums `true` as one and `false` as zero. The resulting sum is the number of proper positive divisors other than one. Comparing it with one directly implements the criterion above.

For $n=4$, the only candidate that divides it is two. The sum is one, so the method returns true. For $n=8$, both two and four divide it. The sum is two, so it returns false. For prime $n=7$, no candidate divides it and the sum is zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why excluding the endpoints is correct

Starting at two deliberately excludes divisor one, and the half-open `range(2, n)` deliberately excludes $n$. Those two divisors are automatic for every $n>1$ and would contribute the same baseline to almost every input. Counting only the possible middle divisors makes the final comparison simple.

$n=1$ is a special mathematical boundary because one and $n$ are the same divisor rather than two distinct divisors. The candidate range is empty, its sum is zero, and the method correctly returns false because one has only one positive divisor.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Connection to squares of primes

An integer has exactly three divisors if and only if it is the square of a prime. Divisors normally pair as $d$ and $n/d$. To have an odd number of divisors, one pair must collapse at $\sqrt n$, so $n$ must be a perfect square. If $n=p^2$ and $p$ is prime, the divisors are exactly $1,p,p^2$. If the square root were composite, additional factor divisors would exist.

The concrete source does not use this theorem. It reaches the same answer by explicit divisor counting, which is simpler but slower. The approach document must distinguish the implemented enumeration from a more optimized prime-square test.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prime-square theorem:** Compute the integer square root, require its square to equal $n$, and test that root for primality up to its square root. This takes $O(\sqrt[4]{n})$ trial divisions and matches the manifest's intended bound.
- **Count divisors only to $\sqrt n$:** Add divisor pairs, treating a square-root divisor once. This improves time to $O(\sqrt n)$ while remaining straightforward.
- **Early exit enumeration:** Stop as soon as two internal divisors are found. It improves many inputs in practice but remains $O(n)$ in the worst case.
- **$n=1$:** The empty candidate range sums to zero, so the answer is false.
- **Prime number:** It has only one and itself, giving no internal divisor and false.
- **Square of a prime:** Its prime root is the only internal divisor, giving true.
- **Square of a composite:** It has additional factor divisors and returns false.
- **Non-square composite:** Proper divisors occur in distinct complementary pairs, so there cannot be exactly one.
- **Boolean summation:** Python's numeric Boolean behavior makes the generator a divisor counter, not merely an existence test.
- **Upper constraint:** At $n=10^4$, the loop performs just under ten thousand modulo tests, which is practical even though it is asymptotically linear.
- **Exactly three, not at most three:** Both zero and two internal divisors return false; equality with one enforces the precise requirement.
- **No short-circuit:** `sum` examines the entire range even when the final answer is already known to be false.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The generator tests $n-2$ candidate integers when $n\ge2$. Each modulo and comparison is constant time in the standard bounded-integer model, so the exact running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

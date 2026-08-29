# Guided Example: Find Greatest Common Divisor of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 6, 9, 10]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return** ***the **greatest common divisor** of the smallest number and largest number in *`nums`.

The objective is to compute `2` from `{"nums": [2, 5, 6, 9, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow the requested values exactly

The problem does not ask for the greatest common divisor of every array element. It asks only for the greatest common divisor of the smallest value and the largest value. Middle values cannot change which two numbers must be supplied to the final computation.

The exact source therefore evaluates `max(nums)` and `min(nums)` and passes those two results to `gcd`. This one-line structure directly mirrors the contract.

For `[2, 5, 6, 9, 10]`, the extrema are 2 and 10. Values 5, 6, and 9 do not enter the gcd computation, even though one of them may have divisibility relationships with an endpoint.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 6, 9, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the extrema

Python's `max` scans the sequence and retains the greatest value seen. `min` performs another scan and retains the smallest. The source therefore makes two linear passes rather than combining both extrema in one hand-written loop. Two passes still cost linear time and keep the code exceptionally clear.

The length is at least two, so neither operation faces an empty sequence. All numbers are positive, so no sign normalization is needed.

Repeated extrema cause no difficulty. For `[3, 3]`, both calls return 3, and the requested computation becomes $\gcd(3,3)$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand what `gcd` computes

The greatest common divisor of positive integers $a$ and $b$ is the largest positive number dividing both with no remainder. The standard implementation uses Euclid's algorithm, based on

$$
\gcd(a,b)=\gcd(b,a\bmod b).
$$

To understand why, write $a=qb+r$, where $r=a\bmod b$. Any number dividing both $a$ and $b$ also divides $a-qb=r$. Conversely, any number dividing both $b$ and $r$ divides $qb+r=a$. The two pairs therefore have exactly the same common divisors and the same greatest one.

Each Euclidean step replaces the larger problem with one whose second value is a strictly smaller nonnegative remainder. Eventually that remainder becomes zero. At that point,

$$
\gcd(x,0)=x,
$$

because every positive divisor of $x$ divides zero and the greatest common divisor is $x$ itself.

The imported `gcd` function performs this well-established process, so the solution does not need to reimplement the loop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 6, 9, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the array:** The endpoints become the first and last values, but sorting costs $O(N\log N)$ time and may mutate the input.
- **One combined extrema loop:** It finds both values in one pass and has the same $O(N)$ asymptotic time, but the two built-ins are simpler.
- **Test every possible divisor:** Scanning down from the minimum can take $O(M)$ time, slower than Euclid's logarithmic behavior.
- **Take the gcd of all elements:** This answers a different question and can produce a smaller value than the gcd of only the extrema.
- **All values equal:** Minimum and maximum coincide, and the answer is that value.
- **Relatively prime extrema:** The Euclidean process ends at one.
- **One extreme divides the other:** The smaller extreme is the gcd.
- **Duplicate minimum or maximum:** Multiplicity does not change either selected value.
- **Unsorted input:** Built-in extrema scans do not assume any ordering.
- **Positive-value guarantee:** The returned gcd is positive and no absolute-value normalization is required.
- **Minimum length two:** Both extrema calls are always defined.
- **Input preservation:** `min`, `max`, and `gcd` do not alter `nums`.
- **Execution environment:** The exact solution relies on `gcd` already being available; standalone code would need `from math import gcd`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of elements and let $M=\max(\texttt{nums})$. `max(nums)` takes $O(N)$ time and `min(nums)` takes another $O(N)$ time. Euclid's algorithm takes $O(\log M)$ time in the usual bound, so total time is $O(N+\log M)$, which simplifies to $O(N)$ under the small fixed value constraint but matches the manifest's more informative form.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

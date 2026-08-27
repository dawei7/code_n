# Guided Example: Closest Prime Numbers in Range

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"left": 10, "right": 19}`
- **Required output:** `[11, 13]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

The objective is to compute `[11, 13]` from `{"left": 10, "right": 19}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate every prime through the right endpoint

To find the closest primes in `[left,right]`, the method first identifies all primes up to `right`. It uses a linear sieve, sometimes called Euler's sieve, even though the manifest summary calls it the Sieve of Eratosthenes.

`st[x]` records whether `x` is known composite. `prime` is a preallocated array that stores discovered primes in increasing order, and `cnt` is the number currently stored.

The outer loop visits integers `i=2` through `right` in ascending order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"left": 10, "right": 19}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize a new prime

If `st[i]` is false when `i` is reached, no smaller prime generated `i` as a composite product. Therefore, `i` is prime.

The code writes it to `prime[cnt]` and increments `cnt`. Ascending outer-loop order makes the stored prime list sorted.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `st[i]` is false when `i` is reached, no smaller prime ge... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark composites with their smallest prime factor

For each `i`, the inner loop multiplies it by stored primes `prime[j]` while the product remains at most `right`. The condition

`prime[j] <= right//i`

avoids overflow-prone direct boundary multiplication.

It marks `prime[j]*i` composite.

If `prime[j]` divides `i`, the loop breaks. This is the central linear-sieve rule. Continuing to larger primes would mark products whose smallest prime factor was already represented elsewhere. Stopping ensures every composite is generated once by the quotient paired with its smallest prime factor.

For example, 12 is marked as $2\cdot6$. When processing `i=6`, prime 2 divides it and the loop stops, so 12 is not redundantly approached through a larger prime.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[11, 13]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"left": 10, "right": 19}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[11, 13]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sieve of Eratosthenes:** Mark multiples from e:** - **Sieve of Eratosthenes:** Mark multiples from each prime's square in $O(R\log\log R)$ time; simpler but not the exact source.
- **Test each interval number independently:** Trial division can be much slower across a wide range.
- **Fewer than two primes:** Return `[-1,-1]`.
- **Prime 2:** It is handled normally as the first discovered prime.
- **`left=1`:** One is marked neither composite nor returned because the sieve begins at two.
- **Tie gaps:** Strict improvement preserves the smaller first prime.
- **Consecutive-pair scan:** Nonadjacent primes cannot be closest.
- **Overflow-safe product bound:** `prime[j]<=right//i` guards multiplication.
- **Preallocated prime array:** Only its prefix through `cnt` contains valid primes.
- **Manifest mismatch:** The break-on-divisor rule identifies Euler's linear sieve.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R=\texttt{right}$. The Euler sieve marks every composite in its canonical smallest-prime-factor way and runs in $O(R)$ time. Filtering and scanning primes add $O(R)$ worst-case work.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Distinct Prime Factors of Product of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 3, 7, 10, 6]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of positive integers `nums`, return *the number of **distinct prime factors** in the product of the elements of* `nums`.

The objective is to compute `4` from `{"nums": [2, 4, 3, 7, 10, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Factor the inputs without forming their product

A prime divides the product of all array values if and only if it divides at least one individual value. Therefore, the set of distinct prime factors of the product is the union of the prime-factor sets of the elements.

The product itself may be enormous and is unnecessary. The method factors each number independently and inserts discovered primes into one shared set `s`.

Set insertion automatically removes duplication:

- repeated copies of a factor within one number count once;
- the same factor appearing in several array elements still counts once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 3, 7, 10, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Trial-divide the current residual

For each array value, local `n` is a working residual and `i` begins at two.

While `i<=n//i`, the code checks whether `i` divides `n`. This condition is an overflow-safe version of $i^2\le n$.

When `n%i==0`:

1. `i` is inserted into the shared set;
2. every copy of `i` is divided out through the nested loop.

Removing all copies ensures future work considers only other prime factors and quickly shrinks the residual.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a discovered divisor is prime

Candidates are tested in increasing order. By the time `i` divides the residual, every smaller prime factor has already been completely removed.

If `i` were composite, it would have a smaller prime divisor, which would also divide the current residual. That smaller divisor should have been removed earlier, a contradiction. Thus every inserted trial divisor is prime.

The code increments through composite candidates too, but only actual divisors are added.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 3, 7, 10, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Smallest-prime-factor sieve:** Precompute factors through 1000 and factor each value faster when many inputs are processed.
- **Multiply first:** It preserves mathematical information but creates needless huge integers.
- **Prime input:** It is added as the final residual.
- **Prime power:** The prime is inserted once while all exponent copies are divided out.
- **Same prime across values:** Set insertion keeps it distinct.
- **Composite trial candidates:** They cannot divide after their smaller prime factors were removed.
- **Residual one:** Nothing remains to insert.
- **Overflow-safe loop guard:** `i<=n//i` avoids multiplying `i*i`.
- **Input list:** Local residual changes do not mutate it.
- **Distinct count:** Return set size, not the sum of factors or exponents.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n sqrt M)$. Let $N$ be the number of values and $M=\max(\texttt{nums})$. In the worst case, trial division checks $O(\sqrt M)$ candidates for one value, giving $O(N\sqrt M)$ time.
- **Auxiliary Space Complexity:** $O(p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

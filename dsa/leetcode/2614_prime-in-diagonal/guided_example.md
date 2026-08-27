# Guided Example: Prime In Diagonal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [[1, 2, 3], [5, 6, 7], [9, 10, 11]]}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 0-indexed two-dimensional integer array `nums`.

The objective is to compute `11` from `{"nums": [[1, 2, 3], [5, 6, 7], [9, 10, 11]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only two cells per row can matter

For an $n\times n$ matrix, row $i$ contributes these diagonal positions:

$$
(i,i)
\quad\text{and}\quad
(i,n-i-1).
$$

Every main-diagonal cell appears as `row[i]`, and every anti-diagonal cell appears as `row[n - i - 1]`. Scanning the rows once therefore visits every candidate without examining the remaining $n^2-2n$ off-diagonal cells.

The answer begins at zero. Whenever a visited candidate is prime, `max` keeps the larger of it and the best prime already seen. If no prime is ever found, zero remains, exactly as required.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [[1, 2, 3], [5, 6, 7], [9, 10, 11]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the primality helper must prove

An integer $x$ is prime only if $x\ge2$. The explicit `x < 2` check rejects one and any smaller value before trial division.

For $x\ge2$, the helper tests every integer divisor from two through $\lfloor\sqrt{x}\rfloor$. The expression

`all(x % i for i in range(2, int(sqrt(x)) + 1))`

is true exactly when every tested remainder is nonzero. A zero remainder means `i` divides $x$, so `all` stops and returns false.

For $x=2$ or $x=3$, the range is empty. Python's `all` of an empty iterable is true, correctly classifying both as prime after the lower-bound check.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An integer $x$ is prime only if $x\ge2$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why checking through the square root is enough

If $x$ is composite, then $x=ab$ for integers $a,b>1$. Both factors cannot exceed $\sqrt{x}$, because then their product would exceed $x$. Therefore, at least one factor is at most $\sqrt{x}$.

So if no integer from two through $\lfloor\sqrt{x}\rfloor$ divides $x$, no nontrivial factor pair exists and $x$ is prime. Testing larger possible divisors would duplicate information: every larger factor would be paired with a smaller one already checked.

The upper endpoint includes the square root. This matters for perfect squares such as 49; divisor seven must be tested to reject the number.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [[1, 2, 3], [5, 6, 7], [9, 10, 11]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Skip non-improving candidates:** Test primalit:** - **Skip non-improving candidates:** Test primality only when a diagonal value exceeds `ans`; smaller values cannot change the maximum.
- **Sieve of Eratosthenes:** Precompute primality through the largest candidate. This can help with many repeated tests but may allocate millions of booleans.
- **Test only odd divisors:** Handle two separately, then check three, five, and so on to halve trial work while preserving $O(\sqrt M)$ complexity.
- **Scan the whole matrix:** This wastes $O(n^2)$ cell visits and may incorrectly include an off-diagonal prime if the diagonal restriction is forgotten.
- **Value one:** It is not prime and is rejected by `x < 2`.
- **Value two:** The divisor range is empty, so it is correctly accepted.
- **Perfect square:** Inclusive square-root testing finds its root divisor.
- **Odd-size center:** The same cell is tested twice but cannot change the final maximum incorrectly.
- **No diagonal prime:** The initialized zero is returned.
- **Off-diagonal larger prime:** It is irrelevant and must never influence the result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\sqrt M)$. Let $n$ be the matrix dimension and let $M$ be the largest diagonal value tested. There are $2n$ helper calls, with one duplicate call at the center when $n$ is odd.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

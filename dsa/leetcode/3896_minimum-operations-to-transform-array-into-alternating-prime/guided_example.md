# Guided Example: Minimum Operations to Transform Array into Alternating Prime

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `3` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The fixed global prime sieve

Before the `Solution` class is created, the module allocates `is_prime` for every integer from 0 through `MX = 200000`. It initially assumes all entries are prime, then explicitly marks 0 and 1 as non-prime.

For every candidate divisor $i$ through $\lfloor\sqrt{\texttt{MX}}\rfloor$, if $i$ is still marked prime, the sieve marks

$$
i^2,\ i^2+i,\ i^2+2i,\ldots
$$

as composite.

Starting at $i^2$ is sufficient. A smaller composite multiple $i\cdot q$ has $q<i$ and was already marked when processing a smaller prime factor. After the sieve finishes, `is_prime[x]` gives the correct status of every value in the fixed range.

The module then builds the sorted list `primes` by collecting every index whose flag remains true.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the ceiling 200000 is enough

Input values are at most $10^5$. An even-indexed value may need to move upward to the next prime, so preprocessing only through $10^5$ would require an argument about what happens just beyond that boundary.

For every integer $x>1$, Bertrand's postulate guarantees a prime $p$ with

$$
x<p<2x.
$$

For $x\le10^5$, such a prime is below 200000. The special input $x=1$ reaches prime 2 directly. Thus the list contains a prime at or above every allowed input, and `bisect_left` always returns a valid list position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Input values are at most $10^5$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Even indices: move to the next prime

At an even index, the element must become prime. Because decrements are forbidden, the only candidates are primes $p\ge x$. Each candidate costs $p-x$ increments, so the smallest feasible prime also has the smallest cost.

The source computes



The returned index `j` identifies the first prime not smaller than `x`. The contribution is `primes[j] - x`.

If `x` is already prime, the left-biased search finds `x` itself and the contribution is zero. If `x` is composite, it finds the next larger prime and returns the exact distance to it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Input-sized sieve:** Sieve only through a prov:** - **Input-sized sieve:** Sieve only through a proven bound above the current maximum input. This may reduce work for small arrays but requires computing a safe next-prime ceiling.
- **Next-prime lookup table:** A reverse pass can store the next prime for every value, reducing even-index queries from binary search to $O(1)$ at the cost of another $O(U)$ array.
- **Per-value trial division:** Testing successive numbers avoids global storage, but repeated primality tests can be much slower across $10^5$ elements.
- **Even index already prime:** `bisect_left` returns that same value, so its cost is zero.
- **Odd index already composite:** The source leaves it unchanged, which is optimal because zero operations are possible.
- **Odd index equal to 1:** One is non-prime by definition, so it needs no operation.
- **Odd index equal to 2:** One increment reaches 3, still prime; two increments reach 4, so this is the only prime odd-position value costing two.
- **Odd index holding an odd prime:** Adding one makes an even number greater than 2, hence a composite, so one operation is sufficient.
- **Largest allowed input:** The preprocessing ceiling contains a later prime for every $x\le10^5$; the binary-search index cannot run beyond `primes` under the contract.
- **Index parity is zero-based:** Positions 0, 2, 4, and so on require primes; reversing the parity would solve a different problem.
- **Fixed preprocessing mismatch:** The source's setup cost depends on 200000 rather than the observed input maximum, despite the manifest's $M$ notation.
- **Required library name:** Standalone execution needs `bisect_left` from Python's `bisect` module to be available.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. The checked-in source has a global preprocessing phase and a method-call phase. Their costs should not be merged without identifying the bound each one uses.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

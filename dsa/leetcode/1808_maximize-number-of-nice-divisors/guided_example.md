# Guided Example: Maximize Number of Nice Divisors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"primeFactors": 5}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `primeFactors`. You are asked to construct a positive integer `n` that satisfies the following conditions:

The objective is to compute `6` from `{"primeFactors": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate prime factorization into an integer-product problem

Write the constructed number as

$$
N=p_1^{a_1}p_2^{a_2}\cdots p_r^{a_r},
$$

where the $p_i$ are distinct primes and every exponent $a_i$ is positive. The number of prime factors counted with multiplicity is

$$
a_1+a_2+\cdots+a_r.
$$

A nice divisor must be divisible by every distinct prime factor of $N$. For prime $p_i$, its exponent in a nice divisor can be any value from 1 through $a_i$. That gives $a_i$ choices independently. Therefore the number of nice divisors is

$$
a_1a_2\cdots a_r.
$$

The actual prime values do not matter. Only their exponents matter. The task becomes: split at most `primeFactors` units into positive integers whose product is as large as possible.

Using all available units is optimal. Increasing any exponent by one cannot decrease the product, and when there are useful splits it increases it. Thus the exponent sum can be treated as exactly $P=\texttt{primeFactors}$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"primeFactors": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why parts of size three dominate

This is the classic integer-break product structure. Suppose a part $x\geq5$ appears. Replacing it by 3 and $x-3$ changes its product contribution from $x$ to

$$
3(x-3).
$$

For $x\geq5$, $3(x-3)>x$. Therefore no optimal partition contains a part at least five; repeatedly splitting off threes improves the product.

Parts of one are also undesirable. A remainder pattern `3 + 1` has product 3, while replacing it by `2 + 2` preserves the sum four and raises the product to 4.

The only useful final parts are consequently threes, plus either one two or one four to handle the remainder.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the three possible remainders

Let $P=3q+r$.

- If $r=0$, use $q$ parts of 3. The product is $3^q$.
- If $r=1$, do not use $q$ threes and a one. Replace one 3 and the 1 by 2 and 2. The product is $4\cdot3^{q-1}$.
- If $r=2$, use one part of 2 and $q$ parts of 3. The product is $2\cdot3^q$.

For $P<4$, the source returns $P$ directly. With one, two, or three available factors, using a single exponent $P$ gives $P$ nice divisors, and no split has a larger product.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"primeFactors": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over every factor count:** It would take at least $O(P)$ work and is impossible for $P$ up to $10^9$.
- **Greedily use twos only:** Three has better product per consumed sum, since $3^{1/3}>2^{1/2}$.
- **Leave a remainder one:** `3 * 1` is worse than `2 * 2`, so the remainder-one correction is essential.
- **Use a part four:** It is equivalent in product to two twos and is represented by the factor 4.
- **`P = 1`:** One exponent gives one nice divisor.
- **`P = 2`:** A single exponent two gives two, tying the split `1 + 1`.
- **`P = 3`:** A single exponent three gives three, better than splits involving one.
- **`P = 4`:** The first nontrivial correction gives four rather than three.
- **Remainder zero:** Use only threes.
- **Remainder two:** One two complements all threes.
- **Prime choices:** Distinct prime values do not affect the divisor-choice product.
- **At most versus exactly:** All available factor multiplicity can be used without reducing the optimum.
- **Modulo timing:** Compute the optimal form first, then its residue; never compare modular residues to choose a partition.
- **Large exponent:** Three-argument `pow` avoids constructing the enormous full integer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log P)$. Let $P$ be `primeFactors`. Branch selection is constant work. Modular exponentiation uses exponentiation by squaring and takes $O(\log P)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

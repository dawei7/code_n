# Guided Example: Unit Conversion II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"conversions": [[0, 1, 2], [0, 2, 6]], "queries": [[1, 2], [1, 0]]}`
- **Required output:** `[3, 500000004]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` types of units indexed from `0` to $n - 1$.

The objective is to compute `[3, 500000004]` from `{"conversions": [[0, 1, 2], [0, 2, 6]], "queries": [[1, 2], [1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The intended relative-factor idea

Choose unit zero as a common reference. Define `F[u]` as:

the number of units of type `u` equivalent to one unit of type zero.

If these factors are known, a query from unit `A` to unit `B` is a ratio. One unit zero equals `F[A]` units of `A`, so one unit `A` equals `1/F[A]` units of zero. Converting onward to `B` gives:

`F[B] / F[A]`.

Modulo prime `MOD = 10^9+7`, division becomes multiplication by an inverse:

`answer(A,B) = F[B] * inverse(F[A]) mod MOD`.

This is the formula used by the protected query loop:

`res[y] * pow(res[x], mod - 2, mod) % mod`.

Fermat's little theorem gives `a^(MOD-2) mod MOD` as the inverse of nonzero `a`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"conversions": [[0, 1, 2], [0, 2, 6]], "queries": [[1, 2], [1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How a forward conversion propagates a factor

Conversion `[s,t,w]` means:

one unit `s` equals `w` units `t`.

If one unit zero equals `F[s]` units `s`, substituting the conversion gives:

`F[t] = F[s] * w`.

The source stores directed adjacency `s -> t` with weight `w` and recursively passes:

`mul * w % mod`.

Starting from `F[0] = 1`, this correctly computes all reference factors when every unit is reachable from zero following only the listed forward directions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the ratio formula is correct when all factors are valid

Suppose `F[A] = p` and `F[B] = q` as exact rational conversion quantities relative to zero. Then:

one zero unit = `p` A units = `q` B units.

Dividing both equalities by `p` shows:

one A unit = `q/p` B units.

All input factors are between one and `10^9`, strictly below `MOD`. In the finite field modulo this prime, every factor is nonzero, and a product of nonzero factors remains nonzero. Therefore a correctly computed `F[A]` has a modular inverse.

The ratio also handles reverse and cross-branch queries without explicitly walking their paths. Shared factors from zero to a common ancestor cancel algebraically.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 500000004]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"conversions": [[0, 1, 2], [0, 2, 6]], "queries": [[1, 2], [1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 500000004]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct bidirectional iterative traversal:** Add reciprocal weighted edges, track the parent, and compute every reference factor without recursion. This is the direct repair.
- **Walk the tree separately for every query:** Correct but can cost `O(nQ)`. Common reference factors reduce each query to one ratio.
- **Lowest common ancestor with path products:** Useful in more general dynamic settings, but unnecessary when all factors relative to one root can be precomputed.
- **Use ordinary integer fractions:** Exact rational numerators and denominators can grow rapidly. Modular factors and inverses match the required output.
- **Add reverse edges without a parent/visited check:** That creates immediate two-node recursion cycles. Bidirectional traversal must avoid returning to the parent.
- **Conversion oriented toward zero:** This is legal and is exactly the case the protected source misses.
- **Outward-only tree:** The factor logic works, subject to the recursion-depth defect.
- **Deep chain:** The recursive source may fail even with correct outward orientation.
- **Query from a unit to itself:** The correct answer is one; an unvisited zero factor makes the protected result wrong.
- **Factor one:** Forward and reverse factors are both one.
- **Cross-branch query:** The ratio `F[B]/F[A]` correctly cancels the shared root path when factors are valid.
- **Nonzero inverse guarantee:** Listed factors are less than the prime modulus, so valid path factors never become zero modulo `MOD`.
- **Zero in res:** It signals an unvisited node in this source, not a legitimate conversion factor.
- **Manifest mismatch:** The advertised bidirectional construction is absent from `solution.py` and must not be assumed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Under the stronger, unstated assumption that all nodes are forward-reachable, building adjacency and DFS take `O(n)` time, and each of `Q` modular inverse queries uses `pow` with exponent `MOD-2`. Since `MOD` is a fixed constant for problem analysis, this is treated as `O(1)` per query, giving `O(n+Q)` total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Maximum Prime Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 9, 5, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `3` from `{"nums": [4, 2, 9, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**The farthest prime indices must be the first and last ones.** Let the indices containing prime values be:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 9, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

For any two prime positions $p_a$ and $p_b$, their distance is at most $p_r-p_1$. Therefore, the maximum is obtained by the leftmost prime and the rightmost prime. If there is only one prime, both chosen indices may be that same position and the distance is zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

The source implements exactly this observation with an outer scan from the left and, only after finding the first prime, an inner scan from the right.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 9, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prime lookup set:** Precompute the 25 primes at most 100 and test membership in constant time. This makes the fixed-domain nature explicit.
- **Sieve of Eratosthenes:** Useful for a much larger bounded value domain, but excessive for 100.
- **Collect every prime index:** Then subtract first from last; correct but uses $O(n)$ space unnecessarily.
- **One prime occurrence:** The reverse scan reaches the same index and returns zero.
- **Prime at both ends:** The method returns `n - 1`, the largest possible distance.
- **Values zero or one:** Rejected before trial division.
- **Values two and three:** Empty divisor ranges correctly produce true.
- **Perfect square composite:** The inclusive upper bound tests its square-root divisor.
- **Repeated prime values:** Each occurrence is a separate eligible index.
- **Nested loop appearance:** Only one reverse scan occurs because it is inside the first successful outer iteration and returns.
- **Guaranteed prime:** Ensures both scans terminate with a return.
- **Index versus value:** Primality belongs to `nums[index]`, while distance belongs to indices.
- **Floating square root:** Values are at most 100, so `int(sqrt(x))` is exact for the needed small integers.
- **No input mutation:** The array is only read.
- **Generalized bound:** Without the value cap, trial division exposes the $O(\sqrt V)$ factor hidden by the manifest's constant domain.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $V=\max(\texttt{nums})$. One primality test uses at most $O(\sqrt V)$ trial divisions. The two directional scans perform $O(n)$ tests in total, giving $O(n\sqrt V)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

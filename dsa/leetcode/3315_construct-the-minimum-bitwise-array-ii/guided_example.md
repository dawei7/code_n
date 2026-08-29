# Guided Example: Construct the Minimum Bitwise Array II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 5, 7]}`
- **Required output:** `[-1, 1, 4, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` consisting of `n` prime integers.

The objective is to compute `[-1, 1, 4, 3]` from `{"nums": [2, 3, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

**Reverse the effect of OR-ing consecutive integers.** Adding one to an integer $a$ finds its least significant zero-bit, sets that bit to one, and resets all lower one-bits to zero. When $a$ is OR-ed with $a+1$, those reset lower bits are restored by $a$, while the formerly zero bit is supplied by $a+1$. Higher bits stay unchanged. In short, `a | (a + 1)` equals $a$ with its lowest zero changed to one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For a given prime $x$, we need to choose where that changed bit was zero in $a$. Since every prime other than two is odd, $x$ ends with at least one one-bit. Let bits $0$ through $t-1$ be the maximal trailing run of ones in $x$, with bit $t$ the first zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Clearing any one of those trailing-one positions in $x$ creates a valid $a$. If position $p<t$ is cleared, then $p$ is the lowest zero of $a$: bits below it remain one. Incrementing sets bit $p$ and clears the lower bits; OR restores every one in $x$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, 1, 4, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, 1, 4, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Mask-based while loop:** Scan powers of two while the corresponding bit is one and update the candidate to `x - mask`. The last candidate before the first zero is the same minimum.
- **Brute force:** Testing every smaller integer is unacceptable near $10^9$, which is why version II requires the bit insight.
- **Closed-form low-bit manipulation:** Specialized bit tricks can isolate the trailing-one boundary in constant word operations, but they are less transparent and Python integers are not fixed-width machine words conceptually.
- **Value two:** No solution exists because the OR is always odd, so `-1` is mandatory.
- **Odd prime with one trailing one:** Clearing bit zero produces the even predecessor immediately below it, as with $5\mapsto4$.
- **Mersenne-like prime:** A long all-ones representation finds its first zero just above the top bit and clears the top one, as with $31\mapsto15$.
- **Minimality direction:** Clearing a higher eligible bit subtracts more and therefore makes the result smaller; choosing the first trailing bit would be valid but not minimal.
- **Hard-coded 32-bit scan:** It is safe for $10^9$ but would be an artificial limitation if constraints allowed integers with bit 32 or higher.
- **Operator precedence:** Explicit parentheses would make both the zero-bit test and shifted XOR easier for beginners to audit.
- **Composite odd values:** The bit construction actually works for odd composites too, although the contract supplies primes.
- **Even values other than two:** They would also be impossible because their least significant bit is zero, but the prime constraint makes two the only such input.
- **No mutation:** The source appends outputs rather than overwriting `nums`, so caller-visible input order and values remain intact.
- **Version I comparison:** The algorithm is identical, but the larger $10^9$ limit makes logarithmic bit inspection materially important here.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log M)$. With $M=\max(\texttt{nums})$, locating the first zero takes $O(\log M)$ bit tests per number in a generalized analysis, for $O(n\log M)$ total time. The source actually performs no more than 31 tests per number under its fixed loop and constraints.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

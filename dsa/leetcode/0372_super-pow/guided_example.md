# Guided Example: Super Pow

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": 2, "b": [3]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Your task is to calculate $a^b$ mod `1337` where `a` is a positive integer and `b` is an extremely large positive integer given in the form of an array.

The objective is to compute `8` from `{"a": 2, "b": [3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Expand the decimal exponent by place value.

If the exponent digits are

$$
[e_{d-1},e_{d-2},\ldots,e_1,e_0],
$$

where $e_0$ is the last array element, then the represented exponent is

$$
B=e_0\cdot10^0+e_1\cdot10^1+\cdots+e_{d-1}\cdot10^{d-1}.
$$

Exponent rules give

$$
a^B
=a^{e_0\cdot10^0}
 a^{e_1\cdot10^1}
 \cdots
 a^{e_{d-1}\cdot10^{d-1}}.
$$

This product lets the algorithm handle each digit independently. A digit never exceeds nine, and the base for its place can be advanced by raising the previous place base to the tenth power.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": 2, "b": [3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why modular reduction can happen after every operation.

For modulus $M=1337$,

$$
(x\bmod M)(y\bmod M)\bmod M=(xy)\bmod M.
$$

Likewise, replacing a base by its remainder does not change the remainder of any nonnegative power. The method may therefore reduce every digit contribution and every place-value base immediately. Intermediate numbers stay below the modulus instead of growing to thousands of digits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For modulus $M=1337$,

$$
(x\bmod M)(y\bmod M)\bmod M=(xy)\b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning of the two changing variables.

Let the original input base be $A$. Before processing decimal place $p$:

- `ans` is congruent to $A$ raised to the value contributed by the already processed lower $p$ digits.
- the current variable `a` is congruent to $A^{10^p}$ modulo `1337`.

Initially no exponent digits have contributed, so `ans = 1`, the multiplicative identity. The current base is $A=A^{10^0}$, satisfying the invariant for place zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": 2, "b": [3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Most-significant-digit streaming:** Process di:** - **Most-significant-digit streaming:** Process digits left to right with `ans = pow(ans, 10, mod) * pow(a, digit, mod) % mod`. Appending digit `e` changes exponent prefix $P$ to $10P+e$. This matches the manifest summary and uses $O(1)$ auxiliary space without reversing.
- **- **Euler or Chinese remainder analysis:** Since $:** - **Euler or Chinese remainder analysis:** Since $1337=7\cdot191$, one can reason about exponent cycles modulo each prime factor and combine results. This is mathematically interesting but requires careful handling when the base is not coprime to 1337.
- **- **Convert all digits to one integer:** Python co:** - **Convert all digits to one integer:** Python could technically hold it, but constructing and exponentiating by that giant value is unnecessary and does not generalize to fixed-width environments.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of exponent digits. The loop performs $d$ iterations. Both modular exponents are bounded by ten, and the modulus is fixed, so each iteration takes $O(1)$ time in the usual word-arithmetic model. Total time is $O(d)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

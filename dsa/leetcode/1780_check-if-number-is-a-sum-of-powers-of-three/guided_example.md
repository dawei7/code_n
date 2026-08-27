# Guided Example: Check if Number is a Sum of Powers of Three

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 59049}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return `true` *if it is possible to represent *`n`* as the sum of distinct powers of three.* Otherwise, return `false`.

The objective is to compute `true` from `{"n": 59049}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate distinct powers into ternary digits

Every nonnegative integer has a unique base-three representation:

$$
n=d_0 3^0+d_1 3^1+d_2 3^2+\cdots,
$$

where each digit $d_i$ is zero, one, or two.

Representing `n` as a sum of distinct powers of three means each power may be selected zero times or one time. Therefore the representation is possible exactly when every ternary digit is zero or one. A digit two would require using that power twice.

The exact solution extracts ternary digits from least significant to most significant and rejects the first digit greater than one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 59049}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract one digit with remainder

`n % 3` is the least significant base-three digit. The source checks:

`if n % 3 > 1`.

Because a remainder modulo three can only be zero, one, or two, “greater than one” means exactly digit two. In that case no sum of distinct powers can equal the original number, so the method returns false immediately.

If the digit is zero, the current power is omitted. If it is one, the current power is included once. Neither case violates distinctness.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `n % 3` is the least significant base-three digit.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Move to the next power

After accepting the current digit, `n //= 3` discards it. Integer division shifts the ternary representation right by one place, making the next digit the new remainder.

For example, decimal 12 has ternary representation 110:

- `12 % 3 = 0`, so $3^0$ is not used; division gives four.
- `4 % 3 = 1`, so $3^1$ is used; division gives one.
- `1 % 3 = 1`, so $3^2$ is used; division gives zero.

No digit two appears, and $12=3+9$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 59049}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert to a ternary string:** It makes digits:** - **Convert to a ternary string:** It makes digits visible but allocates $O(\log n)$ space.
- **Backtracking over powers:** Include or exclude every power, producing exponentially more search than direct unique representation.
- **Greedy subtract largest power:** It can work with careful checks, but ternary digits state the condition more directly.
- **n equal to a power of three:** Its representation has one digit one and otherwise zeros, so it passes.
- **n equal to two:** The first remainder is two and it fails.
- **n equal to one:** The single remainder is one and it passes as $3^0$.
- **Several selected powers:** Multiple digit-one positions are allowed because exponents are distinct.
- **Ternary zero digit:** It simply means skip that power.
- **Ternary two digit:** It means the same power would be needed twice and causes immediate failure.
- **Positive-input guarantee:** The official input excludes zero, though the loop would return true for zero as the empty sum.
- **Uniqueness of representation:** It prevents alternative carry arrangements from avoiding a digit two.
- **Early exit:** The method stops at the first impossible digit.
- **Local mutation:** Dividing `n` does not alter an external object.
- **Fixed bound:** It explains the manifest's constant-time label while the general algorithm is logarithmic.
- **Loop progress:** Integer division by three removes the ternary digit just inspected, so positive `n` strictly decreases and the scan must terminate.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. For a generalized positive input `n`, each iteration divides it by three, so the loop runs $\lfloor\log_3 n\rfloor+1$ times. Exact time is $O(\log n)$ and auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

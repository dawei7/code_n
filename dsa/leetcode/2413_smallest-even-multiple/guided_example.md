# Guided Example: Smallest Even Multiple

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **positive** integer `n`, return *the smallest positive integer that is a multiple of **both** *`2`* and *`n`.

The objective is to compute `10` from `{"n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The requested number is a least common multiple

A number that is a multiple of both `2` and `n` is a common multiple. The smallest positive one is:

$$
\operatorname{lcm}(2,n).
$$

Because one input is the fixed prime number two, the least common multiple depends only on whether `n` already contains a factor of two.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case one: `n` is even

If `n % 2 == 0`, then `n` is divisible by two. It is obviously also divisible by itself. Therefore, `n` is a positive common multiple of two and `n`.

No smaller positive multiple of `n` exists. Positive multiples of `n` are:

$$
n,2n,3n,\ldots
$$

and the first is `n`. Hence, returning `n` is minimal.

For `n = 6`, six is divisible by both six and two, so there is no reason to double it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `n % 2 == 0`, then `n` is divisible by two.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case two: `n` is odd

If `n` is odd, `n` itself is not divisible by two. The positive multiples of `n` are `n, 2n, 3n, ...`. A product of odd `n` and multiplier `m` is even exactly when `m` is even.

The smallest positive even multiplier is two. Therefore, `2n` is the first multiple of `n` that is also even, and it is the smallest common multiple.

For `n = 5`, five fails the even requirement, while ten is divisible by both two and five. No positive multiple of five lies strictly between five and ten.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **General `lcm` helper:** Compute `2*n // gcd(2,:** - **General `lcm` helper:** Compute `2*n // gcd(2,n)`. It is correct but more machinery than a parity branch.
- **Enumerate multiples:** Test `n, 2n, 3n, ...` until finding an even one. It stops within two trials but obscures the direct proof.
- **`n = 1`:** One is odd, so the answer is two.
- **`n = 2`:** It is already a multiple of both inputs, so the answer is two.
- **Any even `n`:** Return it unchanged, including powers of two and even composites.
- **Any odd `n`:** Exactly one factor of two is needed, so return `2n`.
- **Zero:** It is not an allowed input and not a positive answer.
- **No sorting or iteration:** The result depends only on parity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The function performs one modulo check and at most one multiplication. Time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

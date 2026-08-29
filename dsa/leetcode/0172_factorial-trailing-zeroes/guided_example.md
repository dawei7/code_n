# Guided Example: Factorial Trailing Zeroes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *the number of trailing zeroes in *`n!`.

The objective is to compute `0` from `{"n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count factors that create tens

A decimal trailing zero is produced by a factor of ten, and:

$$
10=2\cdot5.
$$

Therefore the number of trailing zeros in $n!$ is the number of pairs of prime
factors two and five in its complete factorization.

There are always more factors of two than factors of five in a factorial:
every second number contributes a two, while only every fifth number
contributes a five; higher powers of two are also more frequent than
corresponding powers of five. The scarce factor is five, so counting all
factors of five gives the answer.

The method never calculates the enormous factorial itself.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count first factors of five

Every multiple of five contributes at least one factor five. The number of
multiples of five from one through `n` is:

$$
\left\lfloor\frac{n}{5}\right\rfloor.
$$

This count includes 5, 10, 15, 20, 25, and so on. However, it counts 25 only
once even though $25=5^2$ contributes two factors. Additional terms are needed
for these repeated factors.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count extra factors from higher powers

Every multiple of 25 contributes a second factor five, so add
$\lfloor n/25\rfloor$. Every multiple of 125 contributes a third factor, so
add $\lfloor n/125\rfloor$. Continue for every power of five:

$$
\left\lfloor\frac{n}{5}\right\rfloor+
\left\lfloor\frac{n}{25}\right\rfloor+
\left\lfloor\frac{n}{125}\right\rfloor+\cdots.
$$

Once a power exceeds `n`, its quotient and every later quotient are zero.

The selected source generates the same series by repeatedly replacing `n`
with `n // 5` and adding that quotient to `ans`. After one division the value
is $\lfloor n/5\rfloor$; after two it is $\lfloor n/25\rfloor$, and so on.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit powers of five:** Maintain `power = 5`, add `n // power`, and multiply the power by five. It computes the same series without changing local `n`.
- **Compute the factorial:** Produces enormous integers and does far more work than necessary.
- **Inspect every multiple of five:** Count repeated factors in each multiple; correct but takes $O(n)$ total time.
- **Count both twos and fives:** Correct but redundant because twos are never the limiting factor.
- **`n = 0`:** Returns zero because $0!=1$.
- **`n < 5`:** No factor five appears, so the answer is zero.
- **Power of five:** Inputs such as 25 contribute an extra count at each applicable power.
- **Nonnegative guarantee:** `while n` and floor division rely on the specified domain.
- **Integer division:** `//` is essential; fractional division does not count multiples.
- **No factorial storage:** The algorithm's memory stays constant even when `n!` has many digits.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Each iteration divides `n` by five. The number of positive quotients is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

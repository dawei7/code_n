# Guided Example: Alternating Digit Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 886996}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`. Each digit of `n` has a sign according to the following rules:

The objective is to compute `0` from `{"n": 886996}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read digits in the same direction as the sign rule

The most significant digit must be positive, the next negative, and signs continue alternating.

Converting `n` to `str(n)` lists decimal digits from most significant to least significant. `enumerate` assigns index zero to the first digit, index one to the second, and so on.

Thus index parity directly determines the required sign:

- even index: positive;
- odd index: negative.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 886996}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate the alternating sign

The factor

`(-1)**i`

equals one when `i` is even and negative one when `i` is odd:

$$
(-1)^0=1,\quad
(-1)^1=-1,\quad
(-1)^2=1,\ldots
$$

Multiplying this factor by digit `int(x)` gives the digit with its prescribed sign.

The generator expression produces those signed values, and `sum` adds them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace `n=521`

`str(521)` is `"521"`. Enumeration yields:

- index 0, digit 5: $(-1)^0\cdot5=+5$;
- index 1, digit 2: $(-1)^1\cdot2=-2$;
- index 2, digit 1: $(-1)^2\cdot1=+1$.

The sum is $5-2+1=4$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 886996}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Arithmetic right-to-left recurrence:** Repeatedly extract a digit and update `answer=digit-answer`; it can use $O(1)$ space.
- **Explicit sign variable:** Start at one and multiply it by $-1$ after every digit.
- **Single digit:** Return it positively.
- **Even number of digits:** The least significant digit is negative.
- **Odd number of digits:** The least significant digit is positive.
- **Result zero:** Opposite signed contributions may cancel completely.
- **Positive input:** There is no minus-sign character to skip.
- **No leading zeroes:** Index zero is the true most significant digit.
- **Generator scope:** Terms are not materialized as a list.
- **Manifest mismatch:** The exact implementation allocates and scans a string.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits. Converting `n` to a string and scanning it both cost $O(d)$ time.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

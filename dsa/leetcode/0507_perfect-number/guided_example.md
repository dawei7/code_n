# Guided Example: Perfect Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 28}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank">**perfect number**</a> is a **positive integer** that is equal to the sum of its **positive divisors**, excluding the number itself. A **divisor** of an integer `x` is an integer that can divide `x` evenly.

The objective is to compute `true` from `{"num": 28}` while avoiding redundant calculations and unnecessary overhead.

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

A perfect number equals the sum of its positive divisors excluding itself. Testing every candidate from one through `num - 1` is unnecessary because divisors occur in complementary pairs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 28}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If `i` divides `num`, then `num // i` also divides it, and

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `i` divides `num`, then `num // i` also divides it, and... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
i\left(\frac{\textit{num}}i\right)=\textit{num}.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 28}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Test every smaller integer:** It directly foll:** - **Test every smaller integer:** It directly follows the definition but takes $O(num)$ time instead of exploiting divisor pairs.
- **Prime factorization formula:** The sum-of-divisors function can be derived from prime exponents, also using square-root factorization. It is more machinery than needed for one equality test.
- **Euclid–Euler perfect-number table:** Within a fixed numeric range, compare against generated even perfect numbers. This is fast but relies on a deeper theorem and a bounded domain rather than direct verification.
- **`num = 1`:** It is not perfect because excluding itself leaves no divisors. The explicit guard prevents the initial one from causing a false positive.
- **Prime number:** No candidate divides, so `s` remains one and cannot equal a prime greater than one.
- **Perfect square:** Its square-root divisor is added once through `i != num // i`.
- **Exclude the number itself:** Starting at factor two after pre-adding one avoids ever adding the pair `(1, num)`.
- **Overflow-safe boundary:** `i <= num // i` avoids evaluating `i * i` in a bounded integer type.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{\textit{num}})$. The candidate `i` runs from two through `floor(sqrt(num))`, performing constant-time division and remainder operations under the standard integer model. Time is $O(\sqrt{\textit{num}})$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

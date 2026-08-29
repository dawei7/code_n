# Guided Example: Sum of Square Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"c": 2147395600}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a non-negative integer `c`, decide whether there're two integers `a` and `b` such that $a^{2} + b^{2} = c$.

The objective is to compute `true` from `{"c": 2147395600}` while avoiding redundant calculations and unnecessary overhead.

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

**Restrict the search to nonnegative square roots.** The problem allows integers `a` and `b`, but signs do not affect squares: `(-a)^2 = a^2`. If any integer solution exists, a solution with both values nonnegative also exists. Each value is at most $\lfloor\sqrt c\rfloor$, because a larger square would already exceed `c`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"c": 2147395600}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution searches this bounded square grid with two pointers:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `a = 0` starts at the smallest possible first value;
- `b = int(sqrt(c))` starts at the largest possible second value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"c": 2147395600}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Loop one value and test with `isqrt`:** For every `a`, compute `c - a*a` and check whether its exact integer square root squares back. This is also $O(\sqrt c)$ and straightforward.
- **Hash set of squares:** Store every square up to `c` and test complements. It uses $O(\sqrt c)$ extra space without improving the time bound.
- **Fermat's two-square theorem:** Factor `c` and ensure every prime congruent to 3 modulo 4 has an even exponent. It is elegant but relies on deeper number theory.
- **`c = 0`:** Both pointers start at 0, and `0^2 + 0^2 = 0` returns true.
- **Perfect square:** A representation with the other value 0 is found, such as `0^2 + 3^2 = 9`.
- **Equal values:** The condition `a <= b` includes pairs such as `1^2 + 1^2 = 2`.
- **Negative integers:** They need not be searched because changing signs leaves squares unchanged.
- **Pointer crossing:** It means every unordered candidate has been tested or eliminated; it is the correct failure condition.
- **Floating square root:** It is safe for the stated range, but `isqrt` is preferable for exactness on arbitrarily large integers.
- **Large upper bound:** The scan still uses constant memory even when it performs about $\sqrt c$ iterations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt c)$. Let $m=\lfloor\sqrt c\rfloor$. Pointer `a` can increase at most $m+1$ times, and `b` can decrease at most $m+1$ times. Every loop iteration moves at least one pointer, so there are $O(m)=O(\sqrt c)$ iterations.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Smallest Number With Given Digit Product

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000000000000000000}`
- **Required output:** `"555555555555555555888888"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **positive** integer `n`, return *a string representing the **smallest positive** integer such that the product of its digits is equal to* `n`*, or *`"-1"`* if no such number exists*.

The objective is to compute `"555555555555555555888888"` from `{"n": 1000000000000000000}` while avoiding redundant calculations and unnecessary overhead.

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

**Factor the target into decimal digits.** A result digit can be one through nine. Digits zero cannot appear when the required product `n` is positive because they would make the product zero. Digit one does not help factor a value greater than one and only makes a multi-digit result longer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000000000000000000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The useful factor digits are therefore two through nine. The method repeatedly extracts the largest possible one, beginning at nine and ending at two.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why larger composite digits are valuable.** Numeric magnitude is determined first by digit count: every positive number with fewer digits is smaller than every number with more digits, provided there are no leading zeros. Packing several small prime factors into one large digit minimizes the number of digits.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"555555555555555555888888"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000000000000000000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"555555555555555555888888"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prime-factor count construction:** Count twos, threes, fives, and sevens, reject any other prime, then pack exponents into digits nine, eight, six, and four. This can make the optimality argument more explicit but requires careful case ordering.
- **Breadth-first search over numbers:** Generating candidate decimal strings grows exponentially and is unnecessary.
- **Target one:** Return digit one; an empty string is not a positive integer representation.
- **Prime target two through seven:** The one-digit target itself is the smallest answer.
- **Prime factor above seven:** No decimal digit can supply it, so negative one is required.
- **Repeated factors:** The while loop records as many copies as needed.
- **Digit one in a larger answer:** It never changes the product and only makes the number longer, so it is omitted.
- **Digit zero:** It would force product zero and cannot occur for positive target.
- **Ascending final order:** It minimizes the number among all permutations of the chosen digit multiset.
- **Minimum digit count first:** A lexicographically attractive longer representation can never beat a shorter positive integer.
- **Large output:** String construction avoids integer overflow or parsing concerns.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Every successful division by a digit at least two reduces `n` by a constant factor. The number of successful divisions is $O(\log n)$ and equals the output digit count up to constants.
- **Auxiliary Space Complexity:** $O(\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

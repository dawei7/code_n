# Guided Example: Account Balance After Rounded Purchase

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"purchaseAmount": 9}`
- **Required output:** `90`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Initially, you have a bank account balance of **100** dollars.

The objective is to compute `90` from `{"purchaseAmount": 9}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate the rounded purchase from the remaining balance.** The account begins with one hundred dollars. The purchase amount must first be rounded to the nearest multiple of ten, with a value ending in five rounded upward. If the rounded purchase is $x$, the required answer is simply $100-x$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"purchaseAmount": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The implementation searches for $x$ explicitly rather than using the arithmetic formula described in the Optimal manifest. It initializes `diff = 100` as a safely large best distance and `x = 0` as the current chosen multiple. It then examines every multiple of ten from one hundred down to zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Enumerate every legal rounded value.** The loop `for y in range(100, -1, -10)` produces

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `90` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"purchaseAmount": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `90` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Add-five formula:** Compute `rounded = ((purchaseAmount + 5) // 10) * 10` and return `100 - rounded`. This directly exploits decimal rounding and is shorter, but it is not the exact implemented method.
- **Use quotient and remainder:** Divide by ten, round the quotient up when the remainder is at least five, and multiply back. This makes the tie rule explicit without enumerating candidates.
- **Floating-point `round`:** Python's built-in rounding uses ties-to-even in relevant forms, not the required always-up rule. It can therefore give the wrong result for amounts ending in five.
- **Amount ending in zero:** The exact matching candidate has distance zero and is selected.
- **Final digit one through four:** The lower multiple is uniquely closer, so the balance reflects rounding down.
- **Final digit five:** Adjacent multiples tie; descending enumeration plus strict improvement retains the higher one.
- **Final digit six through nine:** The higher multiple is uniquely closer.
- **Purchase amount zero:** It rounds to zero and leaves the entire one-hundred-dollar balance.
- **Purchase amount one hundred:** It rounds to one hundred and leaves zero.
- **Changing traversal direction:** An ascending loop would need a non-strict update on ties, or another explicit rule, to continue rounding upward.
- **Changing `<` to `<=`:** With the present descending order, this would make the lower equal-distance multiple overwrite the higher one and violate the tie rule.
- **Inputs outside zero through one hundred:** The candidate set would no longer cover every possible nearest multiple, so the proof and constant bound depend on the stated range.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop always performs exactly eleven iterations. Each iteration uses a subtraction, absolute value, comparison, and at most two assignments. Therefore, with the stated purchase range, running time is $O(1)$. It is also $\Theta(1)$ because the exact code runs all eleven iterations even when the first candidate is already an exact match.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

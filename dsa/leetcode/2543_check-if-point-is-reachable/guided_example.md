# Guided Example: Check if Point Is Reachable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"targetX": 6, "targetY": 9}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There exists an infinitely large grid. You are currently at point `(1, 1)`, and you need to reach the point `(targetX, targetY)` using a finite number of steps.

The objective is to compute `false` from `{"targetX": 6, "targetY": 9}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The greatest common divisor captures reachability

The exact criterion is:

$$
\gcd(\texttt{targetX},\texttt{targetY})
\text{ is a power of two}.
$$

The method computes the gcd and applies the standard power-of-two bit test.

Understanding why requires tracking what the permitted coordinate operations can do to common prime factors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"targetX": 6, "targetY": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Subtraction preserves the gcd

For all integers `x` and `y`:

$$
\gcd(x,y-x)=\gcd(x,y),
$$

and symmetrically

$$
\gcd(x-y,y)=\gcd(x,y).
$$

Any common divisor of `x` and `y` divides their difference, and any common divisor of `x` and `y-x` also divides `(y-x)+x=y`. The sets of common divisors are identical.

Therefore, the two subtraction moves never change the gcd.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For all integers `x` and `y`:

$$
\gcd(x,y-x)=\gcd(x,y),
$$
... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Doubling can introduce only factor two

Consider replacing `x` by `2x`. Any odd prime dividing both `2x` and `y` already divides `x` and `y`, so it was already present in the old gcd.

The only new prime factor that doubling can introduce into the gcd is 2. The same reasoning applies when doubling `y`.

Starting from `gcd(1,1)=1`, no odd prime can ever appear in the coordinate gcd. Any reachable positive target must have gcd

$$
1,2,4,8,\ldots,
$$

a power of two. This proves necessity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"targetX": 6, "targetY": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeatedly divide gcd by two:** Remove factors:** - **Repeatedly divide gcd by two:** Remove factors of two and test whether the remainder is one; equivalent but longer than the bit trick.
- **Grid search:** The state space is infinite and infeasible.
- **Gcd one:** It is $2^0$ and always passes.
- **Equal target coordinates:** Reachable exactly when that common coordinate is a power of two.
- **Odd gcd above one:** It contains an odd factor and fails.
- **One coordinate equal to one:** Gcd is one, so the target is reachable.
- **Positive-input guarantee:** It prevents gcd zero.
- **Subtraction moves:** They preserve gcd exactly.
- **Doubling moves:** They cannot introduce odd common primes.
- **Operator precedence:** The expression tests `(x&(x-1))==0`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(log(min(x, y)))$. Euclid's gcd algorithm takes
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

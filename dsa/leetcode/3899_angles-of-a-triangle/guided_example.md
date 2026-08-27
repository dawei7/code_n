# Guided Example: Angles of a Triangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sides": [3, 4, 5]}`
- **Required output:** `[36.86989764584402, 53.13010235415598, 90.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer array `sides` of length 3.

The objective is to compute `[36.86989764584402, 53.13010235415598, 90.0]` from `{"sides": [3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why one triangle inequality is enough after sorting

Three positive lengths form a non-degenerate triangle exactly when every side is strictly less than the sum of the other two:

$$
a+b>c,\qquad a+c>b,\qquad b+c>a.
$$

Since $a$ and $b$ are positive and $c$ is the largest:

- $a+c>b$ holds automatically because $c\ge b$ and $a>0$;
- $b+c>a$ also holds automatically because both $b$ and $c$ are positive and at least as large as $a$ where relevant.

Only

$$
a+b>c
$$

can fail. The source rejects when `a + b <= c`.

Equality is correctly rejected. If $a+b=c$, the three segments lie on one straight line and enclose zero area. The problem asks for a triangle with positive area, so this degenerate case must return an empty array just like the case $a+b<c$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sides": [3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recovering the first two angles with the law of cosines

For a triangle with side $a$ opposite angle $A$, the law of cosines states

$$
a^2=b^2+c^2-2bc\cos A.
$$

Rearranging gives

$$
\cos A=\frac{b^2+c^2-a^2}{2bc}.
$$

Applying inverse cosine yields $A$ in radians, and `degrees` converts it to degrees:

$$
A=
\operatorname{degrees}\!\left(
\arccos\!\frac{b^2+c^2-a^2}{2bc}
\right).
$$

The source uses the analogous formula for the angle opposite side $b$:

$$
B=
\operatorname{degrees}\!\left(
\arccos\!\frac{a^2+c^2-b^2}{2ac}
\right).
$$

All denominators are nonzero because the input sides are positive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a triangle with side $a$ opposite angle $A$, the law of ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the third angle is obtained by subtraction

The interior angles of every Euclidean triangle sum to $180^\circ$. Once $A$ and $B$ are known, the source sets

$$
C=180-A-B.
$$

This avoids a third inverse-cosine call. It also enforces the angle-sum identity in the returned floating-point values, apart from the ordinary rounding already present in $A$ and $B$.

For sides 3, 4, and 5:

$$
A=\arccos\!\left(\frac{4^2+5^2-3^2}{2\cdot4\cdot5}\right)
\approx36.86990^\circ,
$$

$$
B=\arccos\!\left(\frac{3^2+5^2-4^2}{2\cdot3\cdot5}\right)
\approx53.13010^\circ,
$$

and

$$
C=180^\circ-A-B=90^\circ.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[36.86989764584402, 53.13010235415598, 90.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sides": [3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[36.86989764584402, 53.13010235415598, 90.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compute all three cosine angles:** This is sym:** - **Compute all three cosine angles:** This is symmetric and direct, but performs one extra inverse-cosine call; the source uses the exact $180^\circ$ sum for the third angle.
- **Heron's formula plus trigonometry:** Area can help recover angles, but it adds more operations and can be less numerically direct than the law of cosines.
- **Avoid input mutation:** Using `a, b, c = sorted(sides)` would preserve the caller's list while keeping the same algorithm and bounds.
- **Degenerate equality:** Sides such as `[2,2,4]` satisfy $a+b=c$ and must return `[]` because their area is zero.
- **Clearly impossible triangle:** If $a+b<c$, the longest side cannot be connected by the shorter two, so the method returns `[]`.
- **Equilateral triangle:** Equal sides produce three angles of approximately $60^\circ$ in already sorted order.
- **Isosceles triangle:** Equal sides produce equal opposite angles; non-decreasing order permits equality.
- **Right triangle:** For a Pythagorean triple, the largest angle $C$ is approximately $90^\circ$.
- **Very narrow valid triangle:** A side triple just satisfying $a+b>c$ has one angle close to $180^\circ$, but still represents positive area and must not be rejected.
- **Positive-side guarantee:** Zero-length sides would make a cosine denominator invalid, but the constraints exclude them.
- **Floating-point tolerance:** Results should be compared approximately, not by exact decimal equality.
- **Required library names:** Standalone execution needs `acos` and `degrees` from Python's `math` module.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The input always contains exactly three values. Sorting three elements takes constant time and constant auxiliary space. The validation performs one addition and comparison, and the angle calculation performs a fixed number of arithmetic and mathematical-library operations.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

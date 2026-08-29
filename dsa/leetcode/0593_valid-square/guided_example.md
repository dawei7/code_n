# Guided Example: Valid Square

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"p1": [0, 0], "p2": [1, 1], "p3": [1, 0], "p4": [0, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the coordinates of four points in 2D space `p1`, `p2`, `p3` and `p4`, return `true` *if the four points construct a square*.

The objective is to compute `true` from `{"p1": [0, 0], "p2": [1, 1], "p3": [1, 0], "p4": [0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Squared distances avoid square roots

For three points $a$, $b$, and $c$, the helper computes:

$$
d_1=\lVert a-b\rVert^2,\qquad
d_2=\lVert a-c\rVert^2,\qquad
d_3=\lVert b-c\rVert^2.
$$

For coordinates, squared distance is

$$
(x_1-x_2)^2+(y_1-y_2)^2.
$$

Taking square roots is unnecessary. Equal lengths have equal squared lengths, and the Pythagorean relation for a right triangle is already written in squared form. Integer arithmetic is exact and avoids floating-point rounding.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"p1": [0, 0], "p2": [1, 1], "p3": [1, 0], "p4": [0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognizing a right isosceles triangle without knowing the right vertex

In a right isosceles triangle, the two legs have equal positive length, and the hypotenuse’s squared length is the sum of the two squared leg lengths. The right angle could be at any of the three input points, so `check` considers three cases:

- `d1 == d2 and d1 + d2 == d3`: edges from $a$ to $b$ and $a$ to $c$ are equal legs;
- `d2 == d3 and d2 + d3 == d1`: edges meeting at $c$ are equal legs;
- `d1 == d3 and d1 + d3 == d2`: edges meeting at $b$ are equal legs.

Each case also ends with the common squared leg value, such as `and d1`. In Python, zero is false and a positive integer is true. This rejects coincident points and zero-length “sides.” `any(...)` converts the truthiness of the three candidate expressions into one Boolean result.

For ordinary clarity, `and d1 != 0` would express the same nondegeneracy condition more explicitly. The exact code’s shorter form is valid.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a square makes every check pass

Choose any three vertices of a square. One of them is the corner where two square sides meet; those two sides have equal positive length and form a right angle. The remaining connection joins opposite corners of that three-vertex selection and is a square diagonal. Its squared length is twice a side’s squared length. Thus, one of `check`’s three arrangements succeeds.

Omitting each of the square’s four vertices still leaves such a triangle, so all four helper calls return true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"p1": [0, 0], "p2": [1, 1], "p3": [1, 0], "p4": [0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the four points:** Lexicographic order gives a known side/diagonal arrangement that can be checked. Sorting four items is still $O(1)$, but the geometric indexing proof is less immediately obvious.
- **Six-distance multiset:** Compute all pairwise squared distances. A square has four equal positive small values and two equal values twice as large. This is often the simplest order-independent alternative.
- **Three possible vertex cycles:** Fix one point and explicitly test the three ways to pair the remaining points as adjacent/opposite. Constant work, but more arrangement-oriented.
- **Vector dot products:** Choose a candidate corner and require two equal nonzero adjacent vectors with dot product zero, then verify the fourth point. Requires testing possible corners.
- **Rhombus:** Four equal sides alone are insufficient; unequal diagonals or non-right angles must cause rejection.
- **Rectangle:** Equal diagonals alone are insufficient; unequal side lengths must cause rejection.
- **Duplicate points:** A zero squared leg makes the relevant triple fail, so no zero-area square is accepted.
- **Rotated square:** Distance relations do not depend on axis alignment, so diamonds are accepted.
- **Negative coordinates:** Differences and squares work identically.
- **Arbitrary input order:** Every triple and every possible right-angle position is checked, so ordering is irrelevant.
- **Truthy distance idiom:** `and d1` rejects zero but returns an integer within the list expression; `any` intentionally interprets it as Boolean.
- **Avoid square roots:** Squared distances preserve all equalities and Pythagorean relations exactly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. There are always exactly four points, four helper calls, three distance calculations per call, and a fixed number of comparisons. Therefore, time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

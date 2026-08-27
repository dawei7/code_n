# Guided Example: Largest Triangle Area

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]}`
- **Required output:** `2.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of points on the **X-Y** plane `points` where $\text{points}[i] = [x_{i}, y_{i}]$, return *the area of the largest triangle that can be formed by any three different points*. Answers within $10^{-5}$ of the actual answer will be accepted.

The objective is to compute `2.0` from `{"points": [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Try every choice of three points

A triangle is determined by three points. The input contains at most 50 points, so examining every triple is easily small enough:

$$
50^3=125{,}000
$$

ordered selections. The exact solution uses three loops over `points`. It therefore visits every ordered triple `(P_1, P_2, P_3)`, computes its area, and retains the largest area seen in `ans`.

The loops also include selections in which two loop variables refer to the same input point. Those selections have area zero and cannot incorrectly increase the maximum. They also visit each three-distinct-point triangle in several orders. Repetition costs only a constant factor and lets the implementation avoid index bookkeeping while preserving the `O(n^3)` bound.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn the three points into two vectors

Suppose the selected points are

$$
P_1=(x_1,y_1),\quad P_2=(x_2,y_2),\quad P_3=(x_3,y_3).
$$

Using `P_1` as a shared starting point, the code constructs two side vectors:

$$
\vec{u}=P_2-P_1=(x_2-x_1,\ y_2-y_1)
$$

and

$$
\vec{v}=P_3-P_1=(x_3-x_1,\ y_3-y_1).
$$

The variables `u1, v1` store the horizontal and vertical components of the first vector, while `u2, v2` store those of the second. Despite the compact variable names, both vectors begin at the same vertex. That shared origin is essential for using their cross product to measure the triangle.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the selected points are

$$
P_1=(x_1,y_1),\quad P_2=... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the determinant gives twice the area

For two two-dimensional vectors `(u_1,v_1)` and `(u_2,v_2)`, the magnitude of their scalar cross product is

$$
\left|u_1v_2-u_2v_1\right|.
$$

Geometrically, this is the area of the parallelogram spanned by the vectors. The two vectors form two adjacent sides of that parallelogram, and the diagonal between their endpoints divides it into two congruent triangles. Therefore, the selected triangle's area is half the absolute determinant:

$$
\operatorname{area}
=\frac{\left|u_1v_2-u_2v_1\right|}{2}.
$$

The code calculates exactly this expression as `abs(u1 * v2 - u2 * v1) / 2`.

The absolute value is necessary because the determinant is signed. Listing the points counterclockwise produces one sign, while listing them clockwise produces the opposite sign. Area cannot be negative, and the magnitude is identical for either order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate index combinations:** Loops restrict:** - **Enumerate index combinations:** Loops restricted to `i < j < k` compute each distinct triangle exactly once and avoid repeated-point selections. This reduces the constant factor but uses the same determinant formula and has the same `O(n^3)` asymptotic complexity.
- **- **Shoelace formula:** Applying the three-vertex :** - **Shoelace formula:** Applying the three-vertex shoelace formula produces the same determinant expression after algebraic simplification. The shared-origin vector form makes the geometric reason for halving especially clear.
- **- **Base times height:** Computing a side length a:** - **Base times height:** Computing a side length and its perpendicular height requires square roots or line-distance formulas and more floating-point work. The cross product gives twice the area directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. Let `n` be the number of points. Each of the three loops has `n` iterations, so the area calculation runs `n^3` times. Every calculation performs a constant number of coordinate subtractions, multiplications, one subtraction, an absolute value, a division, and a maximum comparison. The time complexity is therefore `O(n^3)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

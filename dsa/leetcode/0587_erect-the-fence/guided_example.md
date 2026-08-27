# Guided Example: Erect the Fence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]}`
- **Required output:** `[[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `trees` where $\text{trees}[i] = [x_{i}, y_{i}]$ represents the location of a tree in the garden.

The objective is to compute `[[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]` from `{"trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The cross product as a turn test

For indices `i`, `j`, and `k`, the helper loads points $a$, $b$, and $c$ and computes

$$
(b_x-a_x)(c_y-b_y)
-
(b_y-a_y)(c_x-b_x).
$$

This is the two-dimensional cross product of vectors $\overrightarrow{ab}$ and $\overrightarrow{bc}$. It has the same sign as $\overrightarrow{ab}\times\overrightarrow{ac}$ because subtracting $\overrightarrow{ab}$ from the second vector does not change the cross product.

- positive means the path $a\to b\to c$ turns counterclockwise;
- negative means it turns clockwise;
- zero means the three points are collinear.

The scans pop while the value is *strictly negative*. Keeping zero is deliberate: a middle tree lying straight along a fence edge must remain in the output. Using `<= 0` would remove collinear edge points and solve a different convex-hull-corners problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why sorting makes two monotone chains possible

`trees.sort()` orders coordinate lists first by $x$, then by $y$. The input list is modified in place. Once ordered, a left-to-right scan can construct the boundary from the lexicographically smallest point toward the largest without jumping backward in $x$.

If there are fewer than four distinct points, every point is on the boundary: one point is the hull, two form a segment, and three form either a triangle or a line. The early return avoids unnecessary machinery and preserves the original order for that case.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `trees.sort()` orders coordinate lists first by $x$, then by... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Building the first chain

The stack stores indices into sorted `trees` and begins with index 0. For each later point `i`, the algorithm examines the last two stack points and `i`. While they make a clockwise turn, the middle stack point cannot lie on the required outer chain: the new point exposes it as being inward. Popping restores the convex-turn condition. Every point can be pushed once and popped at most once during this pass.

When a point is popped, `vis` is reset to false. After processing `i`, `vis[i]` becomes true and `i` is appended. At the end of the first scan, true entries identify points currently belonging to that chain. The initial point’s marker remains false intentionally so it can close the second chain later.

The value `m = len(stk)` records where the first chain ends in the combined stack. This boundary protects first-chain entries while constructing the return chain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"trees": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Jarvis march:** Repeatedly choose the most cou:** - **Jarvis march:** Repeatedly choose the most counterclockwise next point and explicitly include collinear points. It uses $O(hn)$ time for $h$ hull points and can be attractive when $h$ is very small.
- **Graham scan:** Sort by polar angle around an anchor and maintain a turn stack. Handling all collinear points on the final ray requires special care.
- **Quickhull:** Recursively split points by their distance from candidate edges. Average behavior can be good, but worst-case time is quadratic and collinear-boundary inclusion needs attention.
- **Pop on `<= 0`:** Incorrect here because it removes points collinear on fence edges. Strict `< 0` is the key inclusion rule.
- **All points collinear:** Every tree is on the perimeter and must be returned, not just the two endpoints.
- **Fewer than four points:** Every distinct point is necessarily a boundary point, so the early return is correct.
- **Duplicate positions:** The contract guarantees uniqueness. Duplicates would complicate visitation and output deduplication.
- **Vertical edges:** Lexicographic sorting breaks equal-$x$ ties by $y$, and the cross product handles vertical directions without division or slope infinities.
- **Input mutation:** The exact solution sorts `trees` in place. Copy before sorting if callers require original order preservation.
- **Any output order:** Hull traversal order is acceptable; no final sorting is required.
- **Visibility bookkeeping:** A point popped from the first chain must have its marker reset so it can still belong to the second chain.
- **Closing endpoint:** The starting point is appended at the end of the reverse scan and then removed once, preventing a duplicate coordinate in the answer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the number of trees. Lexicographic sorting takes $O(n\log n)$ time. In each scan, a point is pushed at most once and popped at most once, so the total stack work is $O(n)$ per pass. Sorting dominates, yielding $O(n\log n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

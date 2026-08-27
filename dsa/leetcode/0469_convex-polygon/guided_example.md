# Guided Example: Convex Polygon

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[0, 0], [0, 5], [5, 5], [5, 0]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of points on the **X-Y** plane `points` where $\text{points}[i] = [x_{i}, y_{i}]$. The points form a polygon when joined sequentially.

The objective is to compute `true` from `{"points": [[0, 0], [0, 5], [5, 5], [5, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn orientation from a cross product

For consecutive boundary points

$$
A=P_i,\qquad B=P_{i+1},\qquad C=P_{i+2},
$$

the code forms vectors from `A`:

$$
\overrightarrow{AB}=(x_1,y_1),\qquad
\overrightarrow{AC}=(x_2,y_2).
$$

Their scalar two-dimensional cross product is

$$
\operatorname{cross}(\overrightarrow{AB},\overrightarrow{AC})
=x_1y_2-x_2y_1.
$$

- A positive result means the direction from `AB` toward `AC` is counterclockwise.
- A negative result means it is clockwise.
- Zero means `A`, `B`, and `C` are collinear, so this step makes no left or right turn.

It is also common to cross `AB` with `BC`. The code's `AC` formulation has the same result because `AC = AB + BC`, and crossing a vector with itself contributes zero:

$$
AB\times AC=AB\times(AB+BC)=AB\times BC.
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[0, 0], [0, 5], [5, 5], [5, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remember the last genuine turn

`pre` stores the most recent nonzero cross product. It begins at zero because no orientation has yet been established.

For each `cur`:

- If `cur == 0`, ignore it. A collinear boundary point does not contradict either clockwise or counterclockwise travel.
- If `cur != 0` and `cur * pre < 0`, the signs are opposite, so the polygon contains both turn directions and is not convex.
- Otherwise, store `cur` in `pre` as the current established direction.

When `pre` is still zero, `cur * pre` is zero rather than negative, so the first noncollinear turn simply establishes the sign.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pre` stores the most recent nonzero cross product.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why modulo indexing closes the polygon

The input lists each vertex once but the polygon also has an edge from the final point back to the first. Indices `(i + 1) % n` and `(i + 2) % n` wrap around automatically.

For `i = n - 2`, the triple is the second-last point, last point, and first point. For `i = n - 1`, it is the last point, first point, and second point. Thus turns at the closing boundary are checked just like interior list positions. Omitting them could miss a concave corner near the list boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[0, 0], [0, 5], [5, 5], [5, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compute a convex hull:** Compare the hull with:** - **Compute a convex hull:** Compare the hull with all input vertices. This costs $O(n\log n)$ and is unnecessary because vertices already arrive in boundary order.
- **Check every diagonal:** Verifying that all other vertices lie on one side of every edge can take $O(n^2)$ time; consecutive-turn signs capture the same property for a simple ordered polygon.
- **Use dot products:** Dot products measure angles and lengths but do not directly encode clockwise versus counterclockwise orientation.
- **Clockwise input:** All nonzero cross products are negative and the polygon is still accepted.
- **Counterclockwise input:** All nonzero cross products are positive and accepted.
- **Collinear consecutive points:** Zero turns are ignored, allowing points along a straight convex edge.
- **Closing corners:** Modulo indices ensure the last-to-first transitions are checked.
- **Self-intersection outside the contract:** Local turn checks alone should not replace a simplicity test for arbitrary vertex lists.
- **Three vertices:** Any valid nondegenerate simple triangle has one consistent orientation and is convex.
- **Repeated points:** The source guarantees uniqueness; duplicates could create zero-length edges and would require separate validation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of vertices. The loop processes exactly $n$ triples. Each iteration performs a constant number of indexed reads, subtractions, multiplications, and comparisons, so time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

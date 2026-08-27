# Guided Example: Flood Fill

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]], "sr": 1, "sc": 1, "color": 2}`
- **Required output:** `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an image represented by an `m x n` grid of integers `image`, where $\text{image}[i][j]$ represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a **flood fill** on the image starting from the pixel $\text{image}[sr][sc]$.

The objective is to compute `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]` from `{"image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]], "sr": 1, "sc": 1, "color": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Flood fill changes one connected component, not every matching pixel

The starting pixel has an original color `oc = image[sr][sc]`. The fill must recolor exactly the pixels that can be reached from that start by repeatedly moving up, right, down, or left through pixels of color `oc`.

A pixel elsewhere in the image may have the same numeric color yet remain unchanged if no four-directional path of original-color pixels connects it to the start. Diagonal contact alone is not a connection.

The exact solution performs a depth-first search from the starting coordinate. The image itself records which connected pixels have already been visited: as soon as DFS enters one, it changes that pixel to the requested `color`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]], "sr": 1, "sc": 1, "color": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the original color must be saved first

The search decision for a neighbor is whether its value equals the color the component had before filling. Once the first pixel is changed, reading `image[sr][sc]` would no longer reveal that value. Saving it in `oc` before starting preserves the criterion for the entire traversal.

Every recursive call compares possible neighbors with this same `oc`. The target `color` is used only for marking and output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The search decision for a neighbor is whether its value equa... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate the four directions compactly

The tuple

`dirs = (-1, 0, 1, 0, -1)`

works with adjacent pairs. `pairwise(dirs)` yields

`(-1, 0), (0, 1), (1, 0), (0, -1)`.

These are precisely up, right, down, and left. There are no diagonal pairs. For a current pixel `(i, j)`, adding a pair `(a, b)` produces neighbor `(i + a, j + b)`.

Before reading a neighbor, the solution verifies that its row and column lie inside the image. This prevents negative indices from wrapping around in Python and prevents indices beyond the bottom or right edges.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]], "sr": 1, "sc": 1, "color": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search with a queue:** Recolor o:** - **Breadth-first search with a queue:** Recolor on enqueue and process neighbors iteratively. It has the same `O(mn)` worst-case time and space and avoids recursion-depth limits.
- **- **Explicit visited set:** Track coordinates sepa:** - **Explicit visited set:** Track coordinates separately instead of using the changed color. This works even when colors match but uses extra storage. The early equality check makes it unnecessary here.
- **- **Scan every matching pixel globally:** This is :** - **Scan every matching pixel globally:** This is incorrect because equal-colored pixels in disconnected components must remain unchanged.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let `m` be the row count and `n` the column count. Every pixel in the filled component is entered at most once because recoloring removes it from future `oc` checks. Each entry examines four neighbors, a constant amount of work.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

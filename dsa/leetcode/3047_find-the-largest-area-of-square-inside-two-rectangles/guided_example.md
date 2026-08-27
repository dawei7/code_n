# Guided Example: Find the Largest Area of Square Inside Two Rectangles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bottomLeft": [[1, 1], [2, 2], [3, 1]], "topRight": [[3, 3], [4, 4], [6, 6]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There exist `n` rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays `bottomLeft` and `topRight` where $\text{bottomLeft}[i] = [a_{i}, b_{i}]$ and $\text{topRight}[i] = [c_{i}, d_{i}]$ represent the **bottom-left** and **top-right** coordinates of the $$i^{\text{th}}$$ rectangle, respectively.

The objective is to compute `1` from `{"bottomLeft": [[1, 1], [2, 2], [3, 1]], "topRight": [[3, 3], [4, 4], [6, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

**A square must fit inside a rectangle intersection.** For rectangles $R_1$ and $R_2$, their overlap—if it has positive area—is another axis-aligned rectangle. Its horizontal interval begins at the larger left boundary and ends at the smaller right boundary. Therefore its width is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bottomLeft": [[1, 1], [2, 2], [3, 1]], "topRight": [[3, 3], [4, 4], [6, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Ensure every candidate decision satisfies the required const... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bottomLeft": [[1, 1], [2, 2], [3, 1]], "topRight": [[3, 3], [4, 4], [6, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested index loops:** They compute the same pa:** - **Nested index loops:** They compute the same pairs and can avoid `combinations`' tuple pool, reaching genuine $O(1)$ extra space.
- **Plane sweep:** It is useful for more complex overlap queries but unnecessary for $N\le1000$ and pairwise square maximization.
- **Check only intersection area:** A large narrow rectangle may have large area but support only a small square; the relevant value is the smaller dimension.
- **Disjoint rectangles:** A negative width or height makes `e <= 0`, so the pair contributes nothing.
- **Edge or point contact:** Zero overlap dimension cannot contain a positive-area square and is rejected.
- **One rectangle contained in another:** Their overlap is the smaller rectangle; the formula handles it directly.
- **More than two overlapping rectangles:** Any feasible square is witnessed by a pair, so pair enumeration is sufficient.
- **Equal best areas:** Only the numeric maximum is requested, so no pair identity must be retained.
- **Large coordinates:** Differences and squaring fit comfortably in Python integers.
- **Input preservation:** Neither corner array is sorted or changed.
- **Manifest mismatch:** CPython's combinations pool makes exact peak space linear, despite constant per-pair state.
- **Axis alignment:** Rectangle edges are axis-aligned, and the source assumes the fitted square uses those same axes. The smaller overlap dimension is therefore the limiting side without any rotation calculation.
- **Why area is computed after side maximization:** Maximizing positive side length also maximizes its square because $e^2$ is increasing for $e>0$. Comparing areas or sides would select the same pair.
- **No need to construct square coordinates:** Once positive overlap width and height are known, placing a side-$e$ square at the overlap's bottom-left corner witnesses feasibility. Only its area is requested.
- **Unordered pair generation:** Intersecting rectangle $i$ with $j$ is identical to intersecting $j$ with $i$, so `combinations` avoids duplicate geometric work without losing candidates.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. For $N$ rectangles, `combinations` emits $N(N-1)/2=O(N^2)$ pairs. Each uses constant arithmetic, so time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

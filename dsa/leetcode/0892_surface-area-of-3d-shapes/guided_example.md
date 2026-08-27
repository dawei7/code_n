# Guided Example: Surface Area of 3D Shapes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2], [3, 4]]}`
- **Required output:** `34`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` `grid` where you have placed some `1 x 1 x 1` cubes. Each value $v = \text{grid}[i][j]$ represents a tower of `v` cubes placed on top of cell `(i, j)`.

The objective is to compute `34` from `{"grid": [[1, 2], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

Each positive grid cell represents a vertical tower. The solution first counts the exposed surface of every tower as if it were isolated, then subtracts faces hidden where neighboring towers touch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Surface of one isolated tower.** A tower of height $v>0$ is a $1\times1\times v$ rectangular column. It has one exposed top face, one exposed bottom face, and four vertical sides of area $v$ each. Its isolated surface area is therefore

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Surface of one isolated tower.** A tower of height $v>0$ i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

This formula already excludes faces between cubes stacked inside the same tower. Thinking of the tower as one column is simpler than beginning with $6v$ cube faces and subtracting its $v-1$ internal horizontal contacts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `34` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `34` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count six faces per cube:** Subtract two faces:** - **Count six faces per cube:** Subtract two faces for every adjacent cube pair, including vertical pairs. This is correct but can take time proportional to the total number of cubes rather than $n^2$.
- **Check all four neighboring cells:** It can work only if each shared contact is divided or carefully deduplicated. The top-and-left rule is simpler.
- **Use `abs(v - w)` for internal boundaries:** Height difference describes exposed side above the shorter tower, but a complete formula must also handle outer boundaries and other sides. Isolated area minus shared contacts is less error-prone.
- **Projection area:** Projection counts shadows, not exposed faces. It is a different problem and cannot replace surface-contact accounting.
- **All zeros:** No tower enters the positive branch, so area is zero.
- **One cube:** The formula gives $2+4=6$, including its bottom.
- **One tall tower:** Area is $2+4v$.
- **Equal adjacent towers:** Their entire common side of height $v$ is hidden, so $2v$ is subtracted.
- **Unequal adjacent towers:** Only the lower shared height is hidden; the taller excess remains exposed.
- **Hole surrounded by towers:** Each side facing the zero cell remains exposed because `min(v,0)=0` causes no subtraction.
- **Grid boundary:** Missing neighbors cause no subtraction, retaining outward faces.
- **Bottom surfaces:** They are always part of each positive tower's initial two horizontal faces, as required.
- **No double-counting:** Each horizontal adjacency is handled by its lower or right endpoint exactly once.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the square grid dimension. The nested loops visit all $n^2$ cells. Each positive cell performs a constant number of arithmetic operations and at most two neighbor comparisons.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

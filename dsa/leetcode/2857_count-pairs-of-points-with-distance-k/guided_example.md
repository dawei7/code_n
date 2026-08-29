# Guided Example: Count Pairs of Points With Distance k

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"coordinates": [[1, 2], [4, 2], [1, 3], [5, 2]], "k": 5}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **2D** integer array `coordinates` and an integer `k`, where $\text{coordinates}[i] = [x_{i}, y_{i}]$ are the coordinates of the $i^{\text{th}}$ point in a 2D plane.

The objective is to compute `2` from `{"coordinates": [[1, 2], [4, 2], [1, 3], [5, 2]], "k": 5}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn the distance equation into a lookup.** For two points $(x_1,y_1)$ and $(x_2,y_2)$, define

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"coordinates": [[1, 2], [4, 2], [1, 3], [5, 2]], "k": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
a=x_1\mathbin{\mathrm{XOR}}x_2
\quad\text{and}\quad
b=y_1\mathbin{\mathrm{XOR}}y_2.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Both quantities are non-negative integers, and the required distance condition is simply $a+b=k$. Because `k` is at most `100`, every possible split can be enumerated: choose $a$ from `0` through `k`, and then $b$ must be `k - a`. There are only `k + 1` splits.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"coordinates": [[1, 2], [4, 2], [1, 3], [5, 2]], "k": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Brute-force pairs:** Test all $\binom n2$ pairs directly in $O(n^2)$ time and $O(1)$ extra space. It is simple but far too slow for `50000` points.
- **Why not enumerate coordinate bits:** The small quantity is `k`, not the coordinate range. Splitting `k` into $a+b$ gives only at most `101` cases even though coordinates reach $10^6$.
- **Duplicate coordinates:** The counter stores multiplicity, so separate earlier indices at the same coordinate are all counted. This is essential for `k = 0`.
- **Zero target distance:** Only identical points qualify, and the single split `(0, 0)` handles the case without special branching.
- **Repeated candidate concern:** XOR is bijective when one operand is fixed, so distinct `a` values yield distinct required `x1` values and cannot double-count one earlier point.
- **Ordering requirement:** Inserting the current point after querying is crucial. Inserting first would incorrectly permit pairing a point with itself when `k = 0`.
- **Large answer:** Use a wide integer type outside Python because the count of pairs can be about $1.25\times10^9$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n(k+1)$. Let $n$ be the number of points. The outer loop runs $n$ times and the inner loop runs exactly $k+1$ times. Each iteration performs constant-many integer XOR operations and one expected constant-time hash-table lookup. The expected running time is therefore $O(n(k+1))$, conventionally written $O(nk)$ when emphasizing the parameter `k`. Because `k <= 100`, this is effectively linear in the input size under the stated constraints, but retaining `k` in the bound explains the algorithm's mechanism.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

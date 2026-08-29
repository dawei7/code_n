# Guided Example: Sort the Jumbled Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mapping": [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], "nums": [991, 338, 38]}`
- **Required output:** `[338, 38, 991]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `mapping` which represents the mapping rule of a shuffled decimal system. $\text{mapping}[i] = j$ means digit `i` should be mapped to digit `j` in this system.

The objective is to compute `[338, 38, 991]` from `{"mapping": [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], "nums": [991, 338, 38]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map a nonzero integer from right to left

Helper `f(x)` uses `divmod(x, 10)` to remove one decimal digit at a time. It returns:

- the quotient, which becomes the remaining unprocessed prefix;
- the remainder `v`, which is the current last digit.

The digit is replaced with `mapping[v]`. Variable `k` is its decimal place value: one for units, ten for tens, one hundred for hundreds, and so on.

The statement `y = k * v + y` inserts the mapped digit into the same positional place in the new integer. Multiplying `k` by ten prepares for the next original digit.

For an original number with digits $d_pd_{p-1}\ldots d_0$, the constructed value is

$$
\sum_{q=0}^{p}10^q\cdot\texttt{mapping}[d_q].
$$

That is exactly the integer obtained by digit replacement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mapping": [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], "nums": [991, 338, 38]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle original zero separately

The decimal representation of zero contains one digit, zero. The normal `while x` loop would execute zero times and incorrectly leave mapped value zero regardless of `mapping[0]`.

The special return `mapping[0]` applies the rule to that single digit. This matters because zero may map to any digit from zero through nine.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Let numeric construction discard mapped leading zeros

If an original leading digit maps to zero, its high-place contribution is zero. The resulting integer naturally has no visible leading zero.

For the example mapping, 338 becomes digit sequence `007`. Arithmetic construction produces numeric value seven, which is exactly how the mapped value should compare.

Lower internal or trailing positions are still preserved through their powers of ten. Only leading zeros disappear, as they do in ordinary integer notation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[338, 38, 991]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mapping": [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], "nums": [991, 338, 38]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[338, 38, 991]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **String conversion:** Convert each number to text, replace characters through `mapping`, then parse the result. It is easy to visualize but creates temporary strings.
- **Stable sort with key only:** Python's stable `sorted(nums, key=f)` would preserve equal-key order automatically and avoid explicit indices, though `f` might be recomputed only once by Python's key decoration.
- **Counting sort by mapped value:** The numeric key range approaches $10^9$, so a direct counting array is impractical.
- **Original value zero:** It maps to `mapping[0]`, not automatically to zero.
- **Mapped leading zeros:** They disappear in numeric comparison, so `007` and `07` both equal seven.
- **Equal mapped keys:** Original indices preserve the required relative order.
- **Duplicate original numbers:** Each occurrence has its own index and remains a separate output element.
- **Identity mapping:** Keys equal originals, producing ordinary non-decreasing numeric order.
- **Mapping is not applied to output:** The final lookup returns original values.
- **Maximum digit length:** Values below $10^9$ have at most nine decimal digits.
- **Place-value update:** `k *= 10` is necessary to reconstruct digits in their original positions while scanning backward.
- **Input preservation:** `nums` and `mapping` are read only; `x` inside `f` is a local integer.
- **Tuple ordering:** The second component matters only when mapped keys tie.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of input values and $D$ the maximum decimal digit count. Mapping all numbers takes $O(nD)$ time. Sorting $n$ pairs takes $O(n\log n)$ comparisons, each comparing constant-size integers and indices under the usual model.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Count the Hidden Sequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"differences": [1, -3, 4], "lower": 1, "upper": 6}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of `n` integers `differences`, which describes the **differences **between each pair of **consecutive **integers of a **hidden** sequence of length $(n + 1)$. More formally, call the hidden sequence `hidden`, then we have that $\text{differences}[i] = hidden[i + 1] - \text{hidden}[i]$.

The objective is to compute `2` from `{"differences": [1, -3, 4], "lower": 1, "upper": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build prefix offsets rather than absolute values

Let the first hidden value be $h$. Define prefix offsets by $p_0=0$ and $p_{i+1}=p_i+\texttt{differences}[i]$. Then every hidden element is $\texttt{hidden}[i]=h+p_i$.

This formula automatically preserves every required consecutive difference because

$$
(h+p_{i+1})-(h+p_i)=p_{i+1}-p_i=\texttt{differences}[i].
$$

The exact loop stores the current prefix offset in `x`. It initializes `x = mi = mx = 0` so that the first sequence offset $p_0=0$ is included. For every difference `d`, it performs `x += d`, then updates `mi = min(mi, x)` and `mx = max(mx, x)`.

No other property of all prefix offsets is needed. Shifting by $h$ preserves their relative positions, so only the smallest and largest determine whether the complete sequence fits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"differences": [1, -3, 4], "lower": 1, "upper": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Translate all element bounds into one interval for h

Every hidden value must be at least `lower`. The tightest lower constraint comes from the smallest offset:

$$
h+mi\ge lower,
$$

so $h\ge lower-mi$.

Every hidden value must also be at most `upper`. The tightest upper constraint comes from the largest offset:

$$
h+mx\le upper,
$$

so $h\le upper-mx$.

Therefore valid first values are exactly the integers in the inclusive interval $[lower-mi,\;upper-mx]$. Its integer count is

$$
(upper-mx)-(lower-mi)+1
=(upper-lower)-(mx-mi)+1.
$$

This is the expression returned by the exact solution.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret the span

The quantity `mx - mi` is the width required by the forced sequence shape. The allowed range has width `upper - lower`. If the required shape is wider, no shift can fit. If it fits, the leftover width tells how far the shape may slide, and adding one counts both endpoints.

The call `max(calculated_count, 0)` handles the impossible case without a separate early return. A negative raw count means the valid-start interval is empty.

For `differences = [1,-3,4]`, the offsets are $0,1,-2,2$. Thus `mi = -2` and `mx = 2`, giving span four. The allowed interval from one through six has width five, so the number of shifts is $5-4+1=2$. Choosing $h=3$ gives `[3,4,1,5]`, and choosing $h=4$ gives `[4,5,2,6]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"differences": [1, -3, 4], "lower": 1, "upper": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store every prefix offset:** Building the representative sequence in a list and then taking its minimum and maximum is correct but uses $O(n)$ space instead of the exact constant-space scan.
- **Try every starting value:** There can be up to 200,001 candidates, and validating each would repeat the same prefix work. The interval derivation counts all candidates at once.
- **Check only total difference:** A path can leave the allowed range in the middle and later return. Minimum and maximum prefix offsets are both necessary.
- **Early impossibility check:** The editorial may return as soon as `mx - mi > upper - lower`. The exact source finishes the scan and clamps the final count to zero; both are correct.
- **All zero differences:** Every offset is zero, so each allowed starting integer gives a constant valid sequence. The count is `upper - lower + 1`.
- **Single allowed value:** When `lower == upper`, a valid sequence exists only if every prefix offset is identical, meaning every hidden element stays at that value.
- **Negative differences:** They lower `x` and may update `mi`; no special case is needed.
- **Positive differences:** They may update `mx` symmetrically.
- **Alternating differences:** Even when the final offset returns to zero, the intermediate span controls feasibility.
- **Exact fit:** If `mx - mi == upper - lower`, exactly one shift fits, and the formula returns one.
- **Span too wide:** The raw formula is nonpositive and `max(..., 0)` returns zero.
- **Inclusive endpoints:** The final `+ 1` is required because both the smallest and largest valid starting values count.
- **Initial offset zero:** Initializing `mi` and `mx` to zero includes `hidden[0]`. Starting them only from the first accumulated difference could miss the first element’s constraint.
- **Input preservation:** The solution only reads `differences` and never constructs or modifies a hidden sequence array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `differences`. The loop visits each entry once and performs constant-time addition and comparisons, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

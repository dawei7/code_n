# Guided Example: Container With Most Water

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}`
- **Required output:** `49`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $$i^{\text{th}}$$ line are `(i, 0)` and $(i, \text{height}[i])$.

The objective is to compute `49` from `{"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate two chosen lines into an area formula

For indices `l < r`, the container width is the horizontal distance

$$
r-l.
$$

Water must remain level, and the container may not be slanted. The shorter vertical line determines the highest water level before water spills over that side. Therefore the area is

$$
A(l,r) = (r-l)\min(\texttt{height[l]},\texttt{height[r]}).
$$

The taller line contributes no extra height above the shorter one. This “minimum height times distance” fact is what makes it possible to eliminate pairs without trying all of them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start with the greatest possible width

The method places



at the two outermost lines. No pair has a larger width. The widest pair is not necessarily optimal—a shorter inner width may be compensated by much taller lines—but it gives a useful comparison point and leaves every other pair inside the interval.

At each iteration, the code evaluates the current pair before moving a pointer:



Recording the current area first is essential because the elimination argument uses that already-measured pair as an upper bound for many unmeasured pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The method places



at the two outermost lines.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why moving the taller side cannot help while the shorter side stays

Assume `height[l] < height[r]`. The current area is

$$
(r-l)\texttt{height[l]}.
$$

Consider pairing the same left line with any inner right index `k`, where $l < k < r$. Its width is smaller:

$$
k-l < r-l.
$$

Its usable height is at most the fixed left height:

$$
\min(\texttt{height[l]},\texttt{height[k]}) \le \texttt{height[l]}.
$$

Combining the two inequalities gives

$$
A(l,k) \le (k-l)\texttt{height[l]} < (r-l)\texttt{height[l]} = A(l,r).
$$

Every remaining pair that keeps `l` is strictly worse than the current pair, which has already been considered. The left line can never participate in a better unseen answer, so discarding it with `l += 1` is safe.

Moving `r` instead would reduce the width while keeping `height[l]` as the limiting height. Even an infinitely tall new right line could not recover the lost width. The only possibility for improvement is to replace the shorter line and hope for a higher limiting height.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `49` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `49` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Brute-force all pairs:** Evaluate the exact ar:** - **Brute-force all pairs:** Evaluate the exact area for every $l < r$. This uses constant auxiliary space but $O(n^2)$ time, which is too slow for up to $10^5$ lines.
- **Sort lines by height:** Height alone is insufficient because width is equally important. Sorting also destroys direct positional relationships unless indices are carried and does not simplify the maximum-product tradeoff as cleanly as two pointers.
- **Move the taller pointer:** With the shorter height unchanged and width reduced, no immediate or future pair retaining the shorter endpoint can improve. This move lacks the safe-elimination proof.
- **Move both pointers on unequal heights:** This can skip a tall line that should pair with the retained taller endpoint. Only the known limiting side is safe to discard.
- **Equal endpoint heights:** Either pointer may move after recording the area; the implementation moves `r`.
- **Exactly two lines:** The loop evaluates the only possible pair once and returns its area.
- **Zero-height lines:** They create area zero. When one endpoint is zero, discarding that limiting endpoint is safe; if both are zero, the tie branch removes the right one.
- **All heights equal:** The widest outer pair is optimal. Later widths shrink with the same limiting height, so `ans` never changes.
- **Strictly increasing heights:** The left endpoint is repeatedly discarded until width/height tradeoffs have all been represented by evaluated pairs.
- **Strictly decreasing heights:** The right endpoint is symmetrically discarded.
- **No slanting:** The formula intentionally uses the shorter vertical height; averaging heights or using the taller height would describe a different, invalid geometry.
- **Input preservation:** Only indices move. The height array is never sorted or modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of lines.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

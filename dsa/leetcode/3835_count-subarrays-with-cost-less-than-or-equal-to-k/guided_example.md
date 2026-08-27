# Guided Example: Count Subarrays With Cost Less Than or Equal to K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2], "k": 4}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`, and an integer `k`.

The objective is to compute `5` from `{"nums": [1, 3, 2], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: For a fixed right endpoint, valid starts form one suffix

Fix `r` and compare windows `nums[l..r]` as `l` moves right.

Removing elements from the left cannot increase the maximum, cannot decrease the minimum, and shortens the length. Therefore both nonnegative factors in

$$
(\max-\min)(r-l+1)
$$

stay the same or decrease. The cost cannot increase when the window shrinks.

Consequently, for each right endpoint there is a smallest valid start `l`. Every start from `l` through `r` is valid, while every earlier start is invalid.

This suffix property is what allows a sliding window. Once the smallest valid `l` is known, the number of valid subarrays ending at `r` is simply

$$
r-l+1.
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The left boundary never needs to move backward

When a new rightmost value is appended, the window length grows and its range `max - min` cannot decrease. Therefore the cost for an unchanged left boundary cannot decrease.

If some start was too far left for the previous right endpoint, it cannot become valid after extending farther right. The minimum valid `l` is monotone nondecreasing across the scan.

This proves that one left pointer can serve all right endpoints without restarting.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When a new rightmost value is appended, the window length gr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the maximum with a decreasing deque

`q1` stores indices whose values decrease from front to back. Its front is the maximum value in the current window.

Before appending new index `r` with value `x`, the source removes indices from the back while

`nums[q1[-1]] <= x`.

Any such older value can never again be the maximum while `x` remains in the window: `x` is at least as large and lies later, so it also expires later as `l` advances. The older index is dominated and can be discarded.

After appending `r`, `nums[q1[0]]` is the window maximum.

Using `<=` rather than only `<` keeps the latest occurrence among equal maxima. That is safe and simplifies expiration because the latest equal value survives longer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every subarray:** Updating minimum a:** - **Enumerate every subarray:** Updating minimum and maximum incrementally still requires $O(N^2)$ pairs, which is too slow for $N=10^5$.
- **Balanced multiset window:** An ordered multiset can provide min and max in $O(\log N)$ per insertion/removal, yielding $O(N\log N)$ time. Monotonic deques exploit one-directional movement for linear time.
- **Two heaps with lazy deletion:** This also maintains extrema but is more complicated and logarithmic; stale-entry bookkeeping is unnecessary here.
- **k equals zero:** A valid window must have maximum equal to minimum, so the method counts exactly constant-valued subarrays.
- **All values equal:** Every range is zero, no shrinking occurs, and the answer is all $N(N+1)/2$ subarrays.
- **Single-element input:** Its cost is zero and the function returns 1.
- **Strict failure versus inclusive success:** The loop shrinks only when cost is `> k`, so a cost exactly equal to `k` is counted.
- **Duplicate maxima or minima:** Back removal keeps the newest equal occurrence, which remains available longer and preserves the correct extreme.
- **Large products:** The maximum range and length can create values above 32-bit limits, but Python multiplication is exact.
- **Earliest valid start:** Cost monotonicity under left-shrinking guarantees that all later starts are valid and justifies adding `r - l + 1` at once.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. Every index is appended once to each deque. It can be removed at most once from each deque, from either the back as dominated or the front as expired. The left pointer advances at most $N-1$ times.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Moving Average from Data Stream

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"size": 3, "stream": [1, 10, 3, 5]}`
- **Required output:** `[1.0, 5.5, 4.666666666666667, 6.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

The objective is to compute `[1.0, 5.5, 4.666666666666667, 6.0]` from `{"size": 3, "stream": [1, 10, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store only the fixed number of values that can still affect an answer.

After at least `size` calls, every new average depends only on the newest `size` stream values. Anything older can never reenter a future window, so retaining the entire stream would waste memory.

The exact source uses a fixed-length list as a circular buffer. It also keeps a running sum, allowing each new average to be calculated without summing the buffer again.

The three object fields are:

- `data`: an array of exactly `size` slots;
- `s`: the sum of the values currently in the live window;
- `cnt`: the total number of calls already completed.

The manifest summary mentions a deque, but the checked-in source uses modular indexing into an array. Both designs have similar asymptotic bounds, yet the overwrite behavior here is specifically circular-buffer behavior.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"size": 3, "stream": [1, 10, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize empty slots with zero.

The constructor creates `data = [0] * size`. Before the window fills, some buffer slots do not represent actual stream values. Zero is a convenient neutral placeholder because subtracting it does not alter the running sum.

The constructor also sets `s = 0` and `cnt = 0`, matching an empty stream. The contract guarantees `size >= 1`, so the buffer is never empty and modular indexing is always defined.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor creates `data = [0] * size`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the slot for the next value.

At the start of a `next(val)` call, the source computes

$$
i=\text{cnt}\bmod\text{size}.
$$

For the first `size` calls, this yields indices `0, 1, ..., size - 1`, filling unused slots from left to right. After that, the remainder wraps back to zero and repeats cyclically.

When the buffer is full, slot `i` contains exactly the value that arrived `size` calls earlier—the oldest value in the current window. That is the value that must expire when `val` enters.

For a buffer of length three, write indices follow

$$
0,1,2,0,1,2,\ldots.
$$

On the fourth call, index zero holds the first stream value, which is exactly the one no longer among the newest three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1.0, 5.5, 4.666666666666667, 6.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"size": 3, "stream": [1, 10, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1.0, 5.5, 4.666666666666667, 6.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deque plus running sum:** Append each new valu:** - **Deque plus running sum:** Append each new value, pop from the left when capacity is exceeded, and update the sum with both changes. It has the same $O(1)$ time per call and $O(w)$ space and matches the manifest wording, but needs a deque object rather than a fixed array.
- **- **Store the entire stream:** Append all values a:** - **Store the entire stream:** Append all values and sum the final window for every call. This can take $O(w)$ time per average and $O(m)$ storage, retaining values that will never matter again.
- **- **Recompute the circular-buffer sum:** Fixed sto:** - **Recompute the circular-buffer sum:** Fixed storage alone controls space, but calling `sum(data)` each time would cost $O(w)$ per call. The running sum is what produces constant-time updates.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(w)$. Let $w$ be the configured window size and $m$ the number of calls to `next`. Constructor allocation of the fixed array takes $O(w)$ time and $O(w)$ space.
- **Auxiliary Space Complexity:** $O(w)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

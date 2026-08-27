# Guided Example: Find the Highest Altitude

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"gain": [-5, 1, 5, 0, -7]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a biker going on a road trip. The road trip consists of $n + 1$ points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

The objective is to compute `1` from `{"gain": [-5, 1, 5, 0, -7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Altitude is a running sum of gains

The biker begins at altitude zero. After the first road segment, the altitude is `gain[0]`. After two segments, it is `gain[0] + gain[1]`. In general, the altitude at point $r$ is the prefix sum of the first $r$ gains.

Because $n$ gains connect $n+1$ points, the complete altitude sequence is

$$
0,\quad
\texttt{gain}[0],\quad
\texttt{gain}[0]+\texttt{gain}[1],\quad\ldots
$$

The requested answer is the maximum value in exactly this sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"gain": [-5, 1, 5, 0, -7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate prefix sums lazily

`accumulate(gain, initial=0)` produces an iterator. It first yields the supplied initial value zero, then successively adds each gain and yields the new running total.

Including `initial=0` is essential. The starting point is a real point on the journey and can be the highest altitude, especially when every later prefix sum is negative.

Without the initial value, `accumulate(gain)` would begin after the first movement and could incorrectly miss altitude zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `accumulate(gain, initial=0)` produces an iterator.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Let max consume the altitude stream

`max(...)` reads every yielded altitude and retains the greatest. The exact source composes the two operations:

`return max(accumulate(gain, initial=0))`.

No list of all altitudes is created. The prefix sums exist one at a time as the iterator advances.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"gain": [-5, 1, 5, 0, -7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit loop:** Track `current += gain[i]` an:** - **Explicit loop:** Track `current += gain[i]` and `best = max(best,current)`. It has identical $O(n)$ time and $O(1)$ space and may be easier to debug.
- **Build a prefix-sum list:** It makes every altitude inspectable but uses $O(n)$ extra space unnecessarily.
- **Take max of gain values:** This is incorrect because gains are changes, not absolute altitudes.
- **All negative gains:** The starting altitude zero remains the answer.
- **All positive gains:** The final prefix sum is the maximum.
- **Zero gains:** They repeat the current altitude and cause no special behavior.
- **Highest point occurs multiple times:** `max` returns its value once, as required.
- **Highest at start:** `initial=0` preserves it.
- **Highest at destination:** The final accumulated sum is included.
- **Single gain:** The answer is the larger of zero and that gain.
- **Input preservation:** Lazy accumulation reads `gain` without changing it.
- **Iterator behavior:** It is consumed once by `max`; no second traversal is needed.
- **Prefix meaning:** After consuming gain `i`, the accumulated value is the altitude at point `i + 1`, so the iterator covers every visited point exactly once.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(gain)`. `accumulate` processes every gain once, and `max` consumes each of the $n+1$ yielded altitudes once. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

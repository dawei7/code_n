# Guided Example: Find the Losers of the Circular Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "k": 2}`
- **Required output:** `[4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the $i^{\text{th}}$ friend brings you to the $(i+1)^th$ friend for $1 \le i < n$, and moving clockwise from the $n^{\text{th}}$ friend brings you to the $1^st$ friend.

The objective is to compute `[4, 5]` from `{"n": 5, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent friends with zero-based indices

The statement numbers friends from 1 through $n$, but Python arrays use indices zero through $n-1$.

The solution represents friend 1 by index zero. Array `vis` records whether each indexed friend has ever received the ball.

Only when building the returned list does the code convert an unvisited index `i` back to the problem's number `i + 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the current holder and turn multiplier

Variable `i` is the index of the friend currently holding the ball. It starts at zero because friend 1 receives the ball initially.

Variable `p` is the current turn number and starts at one. On turn `p`, the ball moves `p * k` clockwise steps.

After calculating the next holder, `p` increments so the following pass uses the next multiple of `k`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark receipt before making the pass

The loop condition is `while not vis[i]`. Entering the loop proves the current friend has not previously received the ball.

The code immediately sets `vis[i] = true`. This counts the initial possession by friend 1 and every later arrival.

It then calculates where that friend passes the ball. On the next condition check, the game stops if the destination was already marked.

This ordering matches the rule that the game finishes when someone receives the ball for the second time. That repeated recipient is not newly marked because it was already present.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash set of recipients:** Also supports $O(1)$ expected membership checks, but the dense Boolean array is simpler and helps enumerate losers.
- **Search prior positions after every move:** Avoids extra visited storage but can take $O(n^2)$ time.
- **Attempt a closed-form cycle analysis:** Possible number theory may characterize visits, but direct simulation is clearer within $n \le 50$.
- **One friend:** Friend 1 is marked, receives the ball again after wrapping, and there are no losers.
- **`k = n`:** The first pass returns to the current friend immediately.
- **Pass longer than one circle:** Modulo handles any multiple without repeated stepping.
- **Initial possession:** Friend 1 must be marked before the first pass.
- **Repeated recipient:** It was already marked from its first receipt and is not a loser.
- **Ascending output:** Scanning indices in order removes the need to sort.
- **One-based versus zero-based labels:** Convert only at output; modulo arithmetic stays zero-based.
- **Turn counter placement:** Increment after using `p` so the first pass is exactly `k` steps.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. At most $n$ friends can be marked before a repeat, so the simulation takes $O(n)$ time. Scanning `vis` to build the output takes another $O(n)$, leaving total time $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

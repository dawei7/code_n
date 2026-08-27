# Guided Example: Minimum Cost to Reach Every Position

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cost": [5, 3, 4, 1, 3, 2]}`
- **Required output:** `[5, 3, 3, 1, 1, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `cost` of size `n`. You are currently at position `n` (at the end of the line) in a line of $n + 1$ people (numbered from 0 to `n`).

The objective is to compute `[5, 3, 3, 1, 1, 1]` from `{"cost": [5, 3, 4, 1, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**One paid jump can unlock a suffix of target positions.** You begin behind everyone at position $n$. Swapping with person $j$ in front costs `cost[j]` and moves you to position $j$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cost": [5, 3, 4, 1, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

After that swap, every position with index greater than or equal to $j$ lies behind your new position in the line's movement model. People behind you can swap for free, so you can reach any target position $i\ge j$ without paying again.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After that swap, every position with index greater than or e... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Therefore, to reach target $i$, it is sufficient to choose one paid swap with any person $j$ satisfying $0\le j\le i$, then use free swaps to move back to $i$. The cost of that strategy is `cost[j]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 3, 3, 1, 1, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cost": [5, 3, 4, 1, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 3, 3, 1, 1, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate swaps for every target:** This repeat:** - **Simulate swaps for every target:** This repeats line-state work and can become quadratic, while reachability depends only on one cheapest prefix payment.
- **Dynamic programming over positions:** The transition collapses to a running minimum; a full table is unnecessary.
- **Use suffix minima:** A person after target $i$ does not directly unlock $i$ for free, so the relevant range is the prefix.
- **Add several swap costs:** One paid jump followed by free behind swaps is always sufficient; positive extra payments cannot help.
- **First position:** Only person zero is an eligible one-payment choice, so answer zero is `cost[0]`.
- **New cheaper cost:** Once encountered, it becomes the answer for that and every later position unless an even cheaper value appears.
- **Strictly increasing costs:** The first value remains every prefix minimum.
- **Strictly decreasing costs:** Each current position's own cost becomes its answer.
- **Duplicate minimum costs:** Any occurrence attaining the same prefix minimum yields an equally cheap route.
- **Single-element array:** The loop writes the only cost, which is the sole possible paid swap.
- **Positive-cost guarantee:** It supports the argument that extra paid swaps cannot reduce total cost.
- **Independent outputs:** The source does not mutate `cost` or share a performed swap sequence between targets.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop visits each of the $n$ prices once and performs a constant-time comparison and assignment. Time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Furthest Building You Can Reach

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [4, 2, 7, 6, 9, 14, 12], "bricks": 5, "ladders": 1}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

The objective is to compute `4` from `{"heights": [4, 2, 7, 6, 9, 14, 12], "bricks": 5, "ladders": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Spend ladders on the most expensive climbs

Only positive height differences consume resources. A descent or equal-height move is free. Among the positive climbs needed to reach a fixed prefix, ladders should cover the largest ones and bricks should cover the smaller ones.

The exchange argument is simple. Suppose an allocation uses a ladder on a climb of size $x$ but bricks on a larger climb of size $y>x$. Swapping the ladder to $y$ and paying $x$ bricks instead saves $y-x$ bricks without using another ladder. Therefore an optimal allocation can always place ladders on the largest climbs encountered.

The source maintains exactly that allocation online with a min-heap `h`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [4, 2, 7, 6, 9, 14, 12], "bricks": 5, "ladders": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Temporarily give every new climb a ladder

The loop examines each edge from building `i` to `i+1`. It computes `d = b - a`. When `d <= 0`, the move is free and no heap or resource value changes.

For a positive `d`, the source pushes it into `h`. Conceptually, every climb in the heap currently receives a ladder.

If the heap size is no greater than `ladders`, all heap climbs can indeed be covered by available ladders, so no bricks are spent.

If pushing creates more heap entries than ladders, one climb must switch to bricks. `heappop(h)` removes the smallest climb among those tentatively assigned ladders, and that amount is subtracted from `bricks`.

After this pop, the heap contains the largest at most `ladders` climbs seen so far. Every other positive climb in the processed prefix has been paid with bricks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop examines each edge from building `i` to `i+1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the heap may revise an earlier decision

Suppose one ladder was used on an earlier climb of 3 and the current climb is 8. Pushing 8 creates heap `[3,8]`. If only one ladder exists, popping 3 means retroactively paying 3 bricks and moving the ladder to 8.

If the current climb were 2 instead, pushing gives `[2,3]` and popping 2 means paying bricks for the current climb while leaving the ladder on 3.

The same code handles both cases. No explicit “is the current climb larger?” branch is needed because the min-heap chooses the cheapest climb to remove from ladder coverage.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [4, 2, 7, 6, 9, 14, 12], "bricks": 5, "ladders": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Max-heap of brick-paid climbs:** Initially pay:** - **Max-heap of brick-paid climbs:** Initially pay every climb with bricks. When bricks become negative, replace the largest brick payment with a ladder. This is the symmetric greedy solution with similar complexity.
- **Binary search the reachable building:** For a candidate prefix, select its largest ladder-covered climbs and test brick cost. Repeating prefix checks adds complexity and usually more total work.
- **Sort all climbs for every prefix:** It can identify optimal allocation but repeatedly sorting produces excessive time. The heap updates the allocation incrementally.
- **No ladders:** Every positive climb is immediately popped and paid with bricks; the heap remains empty after each iteration.
- **No bricks:** The journey succeeds through at most the climbs covered by ladders. The first required brick payment makes the count negative.
- **More ladders than positive climbs:** Every climb remains in the heap and no bricks are spent.
- **Descending or equal buildings:** Non-positive differences are free and never enter the heap.
- **Equal climb sizes:** Either equal climb can receive the ladder; only total brick cost matters.
- **Failure on edge `i`:** Building `i` is reachable but `i+1` is not, so returning `i` is the correct zero-based index.
- **Single building:** The sliced loop is empty and the only building, index 0, is returned.
- **Python slice storage:** `heights[:-1]` is an avoidable $O(n)$ copy that makes the exact space usage larger than the abstract heap algorithm.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log(\ell+1)$. Let $n$ be the number of buildings and $\ell$ the number of ladders. The loop considers $n-1$ edges. Each positive climb is pushed once. Whenever heap size exceeds $\ell$, one item is popped. The heap contains at most $\ell$ items after an iteration and at most $\ell+1$ momentarily, so each heap operation costs $O(\log(\ell+1))$.
- **Auxiliary Space Complexity:** $O(n+\ell)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

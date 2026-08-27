# Guided Example: K-th Nearest Obstacle Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queries": [[1, 2], [3, 4], [2, 3], [-3, 0]], "k": 2}`
- **Required output:** `[-1, 7, 5, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an infinite 2D plane.

The objective is to compute `[-1, 7, 5, 3]` from `{"queries": [[1, 2], [3, 4], [2, 3], [-3, 0]], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

After each insertion, only the $k$ smallest distances matter. Among those retained distances, the largest is exactly the $k$-th nearest. The source implements a size-$k$ max-heap using Python's min-heap by storing negative distances.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queries": [[1, 2], [3, 4], [2, 3], [-3, 0]], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For obstacle $(x,y)$, the required Manhattan distance is `abs(x) + abs(y)`. Pushing its negative means a larger real distance is a smaller negative number and rises to the min-heap root. Thus `-pq[0]` is the largest retained real distance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For obstacle $(x,y)$, the required Manhattan distance is `ab... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Every new distance is pushed. Once query index `i` is at least `k`, there are `k+1` inserted candidates in the heap before removal, so `heappop` discards the most negative entry: the largest real distance. The heap returns to size $k$ and contains the $k$ smallest distances seen so far.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, 7, 5, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queries": [[1, 2], [3, 4], [2, 3], [-3, 0]], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, 7, 5, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store all distances and sort after every query:** - **Store all distances and sort after every query:** This repeats sorting and can cost $O(n^2\log n)$.
- **Balanced ordered multiset:** It can maintain all distances and select the $k$-th, but uses $O(n)$ space rather than discarding irrelevant values.
- **Min-heap of all distances:** Its root gives the nearest, not the $k$-th nearest, unless elements are destructively removed.
- **Negated max-heap:** This is the exact source technique because Python's standard heap is a min-heap.
- **`k = 1`:** The heap retains only the smallest distance, and every output after the first is the nearest obstacle.
- **Fewer than `k` queries processed:** Minus one is required even though the heap has a root.
- **Equal distances:** Duplicates remain separate heap entries and count toward rank.
- **Negative coordinates:** Absolute values correctly compute Manhattan distance in every quadrant.
- **Obstacle at the origin:** Its distance is zero and it will always belong to the retained nearest set.
- **Very large coordinates:** The sum can reach $2\cdot10^9$, safely represented by Python integers.
- **Unique coordinates but duplicate distances:** Coordinate uniqueness does not imply distance uniqueness; the heap correctly ignores that distinction.
- **Heap size invariant:** Push occurs before pop, allowing the new candidate and current worst retained candidate to compete uniformly.
- **Why the root is the rank answer:** Exactly $k$ values remain, all no larger than every discarded value. Their largest element has exactly $k-1$ retained values no greater than it when multiplicity is considered, making it the $k$-th order statistic.
- **New distant obstacle:** It is pushed, immediately becomes the most negative heap entry, and is popped again. Existing nearest distances and the answer remain unchanged.
- **New close obstacle:** It remains in the heap and causes the previous largest retained distance to be removed, so the reported $k$-th distance can only stay equal or decrease over time.
- **Monotonic answers after availability:** Once at least $k$ obstacles exist, adding obstacles cannot increase the $k$-th nearest distance. The maintained heap exhibits this property directly.
- **Why indices are unnecessary:** Tie-breaking among obstacles at equal distance is irrelevant because the output is only the distance. Unlike an update problem, no obstacle later needs to be identified or modified.
- **`k` larger than total query count:** Every output is minus one. The heap may grow to all query distances but never exceeds `k`, which is still within the stated space bound.
- **Negating zero:** Distance zero remains zero, and `-pq[0]` returns zero correctly.
- **Streaming behavior:** Each answer is finalized using only previous obstacles and the current query. Future queries are never needed, making the method suitable for an online stream.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log k)$. Let $n$ be the number of queries. The heap never exceeds $k+1$ entries. Each push and possible pop costs $O(\log k)$, giving $O(n\log k)$ time.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

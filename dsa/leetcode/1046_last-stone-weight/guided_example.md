# Guided Example: Last Stone Weight

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stones": [2, 7, 4, 1, 8, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `stones` where $\text{stones}[i]$ is the weight of the $i^{\text{th}}$ stone.

The objective is to compute `1` from `{"stones": [2, 7, 4, 1, 8, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The operation always needs the two current maximums

After every smash, a new weight may be inserted. Repeatedly scanning the whole list for the two largest values would redo substantial work.

A priority queue is designed for this pattern: remove the extreme value, update it, and insert a result. Python's `heapq` implements a min-heap, while this problem needs a max-heap. The exact solution stores every weight with its sign negated.

For positive weights, a larger original weight becomes a smaller negative number. For example, weight eight becomes `-8` and weight seven becomes `-7`. The min-heap removes `-8` first, which corresponds to removing original maximum eight.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stones": [2, 7, 4, 1, 8, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the heap

`h = [-x for x in stones]` creates a separate list of negated weights. The original input order and values are not modified.

`heapify(h)` rearranges that list in place into heap order. Heap order does not fully sort the list; it guarantees that `h[0]` is the smallest negative value, representing the largest remaining stone.

Bottom-up heap construction takes linear time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Remove the two heaviest stones

While more than one heap entry remains, the code executes:

`y, x = -heappop(h), -heappop(h)`.

The first pop returns the smallest negative number, which becomes the largest positive weight `y` after negation. The second becomes the next-largest weight `x`. Therefore, `x <= y`, matching the source's notation.

The simultaneous assignment evaluates both right-hand expressions before assigning names, but the pops still occur left to right in Python.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stones": [2, 7, 4, 1, 8, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan for two maximums each turn:** It avoids a heap but costs `O(N)` per smash and `O(N^2)` total time.
- **Maintain a sorted list:** Maximum removal is constant time at the end, but inserting each difference can shift linearly many entries, retaining quadratic worst-case time.
- **Re-sort after every smash:** This is even more expensive, up to `O(N^2 \log N)`.
- **Bucket counts by weight:** With maximum weight `W`, frequency buckets can run in `O(N + W)` time and `O(W)` space. It is useful only because weights are bounded and is pseudo-polynomial in `W`.
- **Custom max-heap:** It removes the negation trick but requires more implementation code. Python's standard min-heap plus negative values is simpler.
- **Single stone:** The loop never runs, and negating `h[0]` returns its original weight.
- **Two equal stones:** Both are popped, nothing is pushed, and the result is zero.
- **Two unequal stones:** Their difference is pushed as one negative entry and returned as the final positive weight.
- **Many equal maximums:** Each pair is destroyed correctly; heap ordering among equal entries is irrelevant.
- **New difference becomes the maximum:** `heappush` places it appropriately, and it can be selected on the next iteration.
- **Sign discipline:** Heap entries are always negative. `x - y` is the correct stored representation because `y >= x`.
- **Input preservation:** The comprehension builds `h` rather than negating `stones` in place, so callers retain their original list.
- **Positive-weight contract:** Every original stone is positive, and unequal smashes produce a strictly positive difference.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = len(stones)`. Negating values takes `O(N)` time, and `heapify` takes `O(N)` time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Remove Stones to Minimize the Total

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"piles": [5, 4, 9], "k": 2}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `piles`, where $\text{piles}[i]$ represents the number of stones in the $i^{\text{th}}$ pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

The objective is to compute `12` from `{"piles": [5, 4, 9], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maximize the stones removed at every operation

Applying the operation to a pile of size $x$ removes $\lfloor x/2\rfloor$ stones and leaves

$$
x-\left\lfloor\frac x2\right\rfloor
=\left\lceil\frac x2\right\rceil.
$$

The number removed is nondecreasing with pile size. Therefore, at each step, choosing a currently largest pile gives the greatest immediate reduction in the total.

This greedy choice remains optimal across repeated operations. If a schedule applies an operation to smaller pile $a$ while a larger pile $b$ is available, exchanging that operation to $b$ cannot remove fewer stones. The updated $b$ can then participate in later choices. Repeated exchanges transform an optimal schedule into one that always takes a current maximum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"piles": [5, 4, 9], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Simulate a max-heap with negative values

Python's standard heap is a min-heap. The solution stores `-x` for every pile size. The smallest negative number represents the largest original pile, so `pq[0]` is the current target.

`heapify(pq)` constructs the heap in linear time.

The update is compact:

`heapreplace(pq, pq[0] // 2)`.

`heapreplace` removes the smallest heap entry and inserts the supplied replacement in one operation while preserving heap order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why floor division on a negative value gives the right remainder

Suppose the largest pile is $x$, so the root is $-x$. Python floor division satisfies

$$
(-x)//2=-\left\lceil\frac x2\right\rceil.
$$

That is exactly the negative encoding of the remaining pile size. For $x=9$, `-9 // 2` is `-5`, representing five stones after removing four. For $x=4$, `-4 // 2` is `-2`.

Using truncation-toward-zero intuition would be dangerous here; Python's floor behavior is what makes the one-line update correct.

The expression `pq[0] // 2` is evaluated from the old root before `heapreplace` mutates the heap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"piles": [5, 4, 9], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort after every operation:** Repeated sorting finds the maximum but costs roughly $O(KN\log N)$.
- **Scan for the maximum:** It uses constant extra space if mutating input, but costs $O(KN)$ time.
- **Frequency buckets:** Since pile sizes are bounded, counts by size can support operations efficiently, though repeated halving and maximum tracking add implementation complexity.
- **Same pile repeatedly:** The heap naturally selects it again whenever it remains largest, as the rules allow.
- **Odd pile:** Size $2q+1$ removes $q$ and leaves $q+1$; negative floor division encodes this ceiling.
- **Even pile:** Size $2q$ leaves exactly $q$.
- **Pile size one:** The operation removes zero and leaves one. Exact $k$ operations may eventually repeat such piles without changing the total.
- **Tied largest piles:** Choosing either removes the same number; heap ordering among equal values does not affect optimal total.
- **Diminishing removals:** Repeated gains from one pile never increase, which supports taking the currently best gain first.
- **Heap size:** Each operation replaces one entry rather than deleting a pile, so exactly $N$ entries remain.
- **One pile:** Every operation repeatedly replaces it by its ceiling half.
- **Exact operation count:** The loop always runs $k$ times, even when all piles reach one.
- **Input preservation:** A separate negative list is built, so `piles` itself is not mutated.
- **Final sign:** Heap entries stay nonpositive, so negating their sum recovers the total of represented positive pile sizes.
- **Imported heap helpers:** The exact source assumes `heapify` and `heapreplace` are available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of piles and $K$ the required operation count.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

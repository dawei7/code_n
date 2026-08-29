# Guided Example: Maximum Score After Binary Swaps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 5, 2, 3], "s": "01010"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and a binary string `s` of the same length.

The objective is to compute `7` from `{"nums": [2, 1, 5, 2, 3], "s": "01010"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Describe reachable one positions as deadlines

Legal swaps change `"01"` to `"10"`, so a one may move left across zeros but never right across a zero. Ones also cannot pass one another.

List the original one positions in increasing order as

$$
p_1<p_2<\cdots<p_m.
$$

If their final positions are $q_1<q_2<\cdots<q_m$, reachability requires

$$
q_k\le p_k
$$

for every $k$. The $k$th one must be assigned a distinct score position no later than its original position. Conversely, any increasing positions satisfying these inequalities can be reached by moving the ones from left to right into those earlier-or-equal places.

Thus each original one position is a deadline: when scan index `p_k` is reached, one unused position from prefix `0..p_k` must be selected.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 5, 2, 3], "s": "01010"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store all currently available score values

The source scans `nums` and `s` together from left to right. At every index, it pushes `-x` into `pq`.

Python provides a min-heap. Negating scores makes the most valuable available score the smallest stored negative number. Popping it and subtracting it from `ans` adds the original positive value.

The heap contains score positions already encountered but not yet assigned to a one. A position may be selected at most once because popping removes it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Satisfy a deadline whenever an original one appears

When current character `c` is `"1"`, another original one deadline has arrived. The source immediately pops the largest score among all unassigned positions in the current prefix.

After processing any prefix ending at index `i`:

- the number of selected positions equals the number of original ones in `s[0..i]`;
- every selected position lies inside that prefix;
- `pq` contains all other prefix positions.

The heap can never be empty at a one: the current position was pushed before the conditional pop, and previous pops cannot outnumber previous ones.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 5, 2, 3], "s": "01010"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate adjacent swaps:** Exploring or performing swaps directly can be quadratic and hides the assignment structure.
- **Choose the globally largest values:** A large value to the right of an early one's deadline may be unreachable for that one.
- **Min-cost matching:** The nested prefix constraints form a special deadline problem that the heap solves greedily.
- **Process from right to left:** A dual formulation is possible, but the source treats original ones as left-to-right deadlines.
- **Push after handling a one:** That would incorrectly exclude the one's current position from its legal choices; the source pushes first.
- **All zeros:** No score position is selected and the answer is zero.
- **All ones:** No one can change its relative occupancy; all values are selected.
- **One at index zero:** Its only available position is zero, so that value is popped immediately.
- **Late one:** It may choose any still-unused position in its entire prefix.
- **Duplicate score values:** Heap occurrences remain separate and can be selected for different ones.
- **Positive scores:** The algorithm still respects reachability; positivity means using all fixed ones is naturally required.
- **Ones never cross:** Sorted deadline-to-position matching preserves their order.
- **Input preservation:** The heap stores negated values without changing `nums` or `s`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Each of the $N$ positions is pushed once. Each original one causes one pop, for at most $N$ pops. Heap operations cost $O(\log N)$, yielding $O(N\log N)$ total time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

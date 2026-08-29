# Guided Example: Count the Number of Good Partitions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` consisting of **positive** integers.

The objective is to compute `8` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A value ties all of its occurrences together

A partition cuts the array into contiguous groups, and each distinct value must appear in exactly one group. Therefore, if a value first appears at one position and last appears later, no cut may occur anywhere between those two positions. Otherwise occurrences of that value would be placed into different groups.

Each distinct value can consequently be viewed as imposing a closed interval from its first occurrence to its last occurrence. Overlapping intervals also become inseparable: if one value forces positions 1 through 4 together and another forces positions 3 through 7 together, then positions 1 through 7 must belong to one component. The problem reduces to finding how many maximal merged occurrence intervals cover the array.

The implementation does not explicitly store both endpoints or sort intervals. It first builds `last = {x: i for i, x in enumerate(nums)}`. Because later assignments overwrite earlier ones, `last[x]` becomes the final index where value `x` occurs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan and maintain the farthest forced boundary

Variable `j` is the farthest last occurrence of any value seen in the current component. It begins at `-1`. At index `i` with value `x`, the update `j = max(j, last[x])` extends the component’s required boundary if `x` occurs farther to the right.

When `i == j`, every value encountered since this component began has its final occurrence at or before `i`. No value in that component appears later. A cut after `i` is therefore safe, and `k`, the number of completed components, is incremented.

If `i < j`, at least one seen value appears later, so cutting after `i` would split that value across groups. The scan must remain inside the same component. It is impossible for `i > j` during an active component because visiting an index causes `j` to be at least that value’s last occurrence, which is at least `i`.

Consider `nums = [1, 2, 1, 3, 4, 3]`. The last positions are 2 for value 1, 1 for value 2, 5 for value 3, and 4 for value 4. At index zero, `j` becomes two. Index one does not extend it, and index two closes the first component. Index three makes `j = 5`; index four remains inside; index five closes the second component. Thus $k=2$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: From forced components to partition choices

Inside a component, no cut is legal because some occurrence interval crosses every internal candidate boundary. Between two consecutive completed components, however, no value crosses the boundary, so a cut is optional.

If there are $k$ components, there are $k-1$ boundaries between them. Each boundary independently has two choices: cut there, or merge the neighboring components into the same group. Hence the number of good partitions is

$$
2^{k-1}.
$$

For the example with two components, the choices are either keep them as two groups or merge them into one, yielding two good partitions. If every position belongs to one merged component, $k=1$ and the only valid partition is the whole array.

The implementation calculates this value with `pow(2, k - 1, 1_000_000_007)`. The three-argument power performs fast modular exponentiation, so it never constructs the potentially enormous exact power.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every cut combination:** There are $2^{N-1}$ raw ways to place boundaries, so validating all of them is infeasible.
- **Explicit interval sorting and merging:** Building first/last intervals and sorting them works, but array scan order already presents first encounters in order, allowing an $O(N)$ merge without sorting.
- **Frequency countdown:** One can track counts remaining and the number of active values. This is valid but needs more changing state than the farthest-last-index invariant.
- **All values distinct:** Every occurrence interval has length zero, so every index closes a component. With $k=N$, all $2^{N-1}$ boundary selections are valid.
- **All values equal:** The first occurrence extends `j` to the final index, producing one component and exactly one partition.
- **Nested intervals:** A shorter interval entirely inside a longer one does not create a boundary; `max` preserves the longer forced endpoint.
- **Chained overlaps:** Even if the first and last intervals do not directly overlap, intermediate intervals can extend `j` repeatedly and correctly merge the entire chain.
- **Modulo arithmetic:** Only the final count modulo $10^9+7$ is requested. Modular `pow` preserves the correct residue without forming $2^{k-1}$ explicitly.
- **Input order:** Sorting would destroy contiguity and the original occurrence intervals, so the solution scans the array as given.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length and $U$ its number of distinct values. Building `last` visits all $N$ positions and uses expected $O(1)$ hash-map updates. The second scan also visits each position once with an expected constant-time lookup. The total expected running time is $O(N)$.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

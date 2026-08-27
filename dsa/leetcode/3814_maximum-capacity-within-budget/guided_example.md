# Guided Example: Maximum Capacity Within Budget

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"costs": [4, 8, 5, 3], "capacity": [1, 5, 2, 7], "budget": 8}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `costs` and `capacity`, both of length `n`, where $\text{costs}[i]$ represents the purchase cost of the $$i^{\text{th}}$$ machine and $\text{capacity}[i]$ represents its performance capacity.

The objective is to compute `8` from `{"costs": [4, 8, 5, 3], "capacity": [1, 5, 2, 7], "budget": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Discard machines that can never participate

Every cost and capacity is positive. If one machine has `cost >= budget`, selecting it alone already violates the strict requirement, and adding a second positive-cost machine cannot help. The source therefore builds `arr` using only pairs `(cost, capacity)` whose cost is strictly below `budget`.

This filter is safe for both one-machine and two-machine choices. It also handles the zero-machine option implicitly: if `arr` is empty, no individual machine is affordable, so the best achievable capacity is 0.

The remaining tuples are sorted. Python sorts a pair first by cost and then by capacity, so costs are nondecreasing:

$$
a_0\le a_1\le\cdots\le a_{m-1},
$$

where $m$ is the number of individually affordable machines. The secondary capacity ordering among equal costs is not required for correctness, but it does not hurt.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"costs": [4, 8, 5, 3], "capacity": [1, 5, 2, 7], "budget": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep the best capacity inside the currently feasible partner range

For a fixed first machine at sorted index `i`, only later indices need to be considered as its partner. Any pair has one smaller sorted index, and the algorithm evaluates that pair when this smaller index becomes `i`. This prevents pairing a machine with itself and avoids reconsidering the same unordered pair from both directions.

Because costs are sorted, feasible later partners form a prefix of the later indices. If index `j` satisfies

$$
a_i+a_j<\texttt{budget},
$$

then every index $k$ with $i<k\le j$ is also feasible because $a_k\le a_j$. Conversely, once the largest remaining cost is too expensive, that index cannot partner with `i`.

The source maintains this changing set of candidates in `remain`, a `SortedList` of pairs `(capacity, sorted_index)`. Ordering by capacity first means `remain[-1][0]` is the maximum capacity among all currently stored candidates. The sorted index is included to make every entry unique even when two distinct machines have equal capacities.

Initially, `remain` contains every machine in `arr`. The right pointer `j` begins at the last sorted index. Before evaluating a fixed `i`, the source discards `(arr[i][1], i)` so that the machine cannot be selected twice.

It then checks the most expensive surviving endpoint. While `arr[i][0] + arr[j][0] >= budget`, index `j` is illegal because equality is forbidden as well as greater cost. That entry is discarded from `remain` and `j` moves left. When the loop stops with `i < j`, every remaining index from `i + 1` through `j` has a legal total cost with `i`.

At this point, `remain[-1]` does not identify the cheapest legal partner. It identifies the legal partner with greatest capacity, which is exactly what should be combined with `arr[i][1]`. Cost determines eligibility; among eligible machines, only capacity affects the objective.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a fixed first machine at sorted index `i`, only later in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why removed right endpoints never need to return

As `i` moves right, `arr[i][0]` never decreases. Suppose a high-cost endpoint `j` is too expensive for the current `i`:

$$
a_i+a_j\ge\texttt{budget}.
$$

For any later first index $i'>i$, $a_{i'}\ge a_i$, so

$$
a_{i'}+a_j\ge a_i+a_j\ge\texttt{budget}.
$$

That endpoint is also illegal for every future iteration. It can be removed permanently, which is why `j` only moves left. This monotonicity prevents an $O(N^2)$ restart of the partner search.

After an iteration, `i` increases. At the beginning of the next iteration, its own entry is discarded. Inductively, `remain` contains exactly the later indices that have not been permanently rejected for excessive cost. Once the inner loop finishes, those are precisely the valid partners for the current first index.

Every legal pair is considered in the following sense: when its smaller sorted index is `i`, its larger index lies in the feasible range, and `remain` contains it. The algorithm need not calculate that particular pair if another feasible partner has higher capacity; using the maximum capacity can only produce an equal or better total for the same first machine.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"costs": [4, 8, 5, 3], "capacity": [1, 5, 2, 7], "budget": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix maximum plus binary search:** Sort by c:** - **Prefix maximum plus binary search:** Sort by cost, build the best capacity over every prefix, and for each machine binary-search the largest partner cost strictly below `budget - cost` while excluding the same index. This matches the manifest summary and also achieves $O(N\log N)$ time, but it is not the exact source's data flow.
- **Quadratic pair enumeration:** Testing every pair is straightforward and handles the strict inequality directly, but it costs $O(N^2)$ and is too slow for $N=10^5$.
- **Cost-indexed maximum table:** Since `budget <= 2 * 10^5`, capacities can be aggregated by cost and prefix maxima built over the numeric cost domain. Distinct-machine handling for two equal-cost selections still requires retaining the best two capacities at a cost.
- **No individually affordable machine:** Filtering produces an empty array and the function correctly returns 0.
- **Exactly equal to the budget:** A single cost equal to `budget` is filtered out, and a pair sum equal to `budget` is removed by the `>=` condition. Both reflect the exclusive bound.
- **Only one affordable machine:** `ans` is initialized from that machine, the `i < j` loop never runs, and its capacity is returned.
- **Equal costs:** Sorting may order them by capacity, but their distinct sorted indices keep them separate. Two equal-cost machines may be paired when twice the cost is strictly below the budget.
- **Equal capacities:** Including the sorted index in each `SortedList` tuple prevents two machines from collapsing into one multiset entry.
- **Best pair need not use the cheapest machine:** Every sorted index eventually serves as the smaller endpoint while a later partner exists, so a higher-cost, higher-capacity pair is still evaluated.
- **Positive capacities:** The largest affordable individual machine is always at least as good as selecting zero machines. If capacities could be negative, the zero-machine option would need explicit comparison, but the contract excludes that case.
- **External ordered-container dependency:** `SortedList` must be provided by the harness or imported from its supporting library. Replacing it with an ordinary list would make middle removals linear and could degrade the algorithm to quadratic time.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log M)$. Let $M\le N$ be the number of machines whose individual cost is below `budget`. Filtering costs $O(N)$ time. Sorting `arr` costs $O(M\log M)$. Inserting the $M$ entries into `SortedList` one at a time costs $O(M\log M)$ in the standard ordered-multiset complexity model.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

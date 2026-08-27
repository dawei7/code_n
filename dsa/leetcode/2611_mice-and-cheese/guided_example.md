# Guided Example: Mice and Cheese

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"reward1": [1, 1, 3, 4], "reward2": [4, 4, 1, 1], "k": 2}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are two mice and `n` different types of cheese, each type of cheese should be eaten by exactly one mouse.

The objective is to compute `15` from `{"reward1": [1, 1, 3, 4], "reward2": [4, 4, 1, 1], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the unavoidable choice from the incremental benefit

Every cheese must be assigned to exactly one mouse, and the first mouse must receive exactly $k$ cheeses. For cheese $i$, switching its owner from the second mouse to the first changes the score by

$$
\Delta_i=\texttt{reward1[i]}-\texttt{reward2[i]}.
$$

This difference may be positive, zero, or negative even though both reward arrays contain positive values. A positive difference favors the first mouse; a negative difference means the second mouse would score more on that cheese.

One way to view the total is to give every cheese to the second mouse first:

$$
B=\sum_{i=0}^{n-1}\texttt{reward2[i]}.
$$

Then select exactly $k$ indices to transfer to the first mouse. Transferring index $i$ adds $\Delta_i$, so a selected set $S$ has total

$$
B+\sum_{i\in S}\Delta_i,
\qquad |S|=k.
$$

The baseline $B$ is the same for every valid assignment. Maximizing the score is therefore exactly the problem of selecting the $k$ largest differences.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"reward1": [1, 1, 3, 4], "reward2": [4, 4, 1, 1], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort indices rather than rewards

The code creates `range(n)` and sorts those indices using

`reward1[i] - reward2[i]`

as the key, in descending order. The resulting list `idx` puts the most favorable transfers first.

Sorting indices preserves the connection between the two rewards for one cheese. Sorting `reward1` and `reward2` independently would destroy that pairing and could combine rewards that belong to different cheese types.

After sorting:

- indices in `idx[:k]` go to the first mouse;
- indices in `idx[k:]` go to the second mouse.

The return expression sums `reward1` for the first group and `reward2` for the second group. The slices partition all indices, so every cheese is used exactly once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code creates `range(n)` and sorts those indices using

`... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the largest differences are optimal

Consider any valid assignment that does not choose the $k$ largest differences. Then some selected index $a$ has a smaller difference than an unselected index $b$:

$$
\Delta_a<\Delta_b.
$$

Swap their owners: give $b$ to the first mouse and $a$ to the second. The first mouse still has exactly $k$ cheeses, but the total changes by

$$
\Delta_b-\Delta_a>0.
$$

So the original assignment could not have been optimal. Repeating such exchanges removes every inversion until the selected set consists of $k$ largest differences.

If differences tie, swapping tied indices changes the score by zero. Any ordering among them is valid, which is why the algorithm does not need a special tie rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"reward1": [1, 1, 3, 4], "reward2": [4, 4, 1, 1], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Min-heap of size $k$:** Scan all differences a:** - **Min-heap of size $k$:** Scan all differences and retain the $k$ largest in $O(n\log k)$ time and $O(k)$ space, then add them to the second-mouse baseline.
- **Quickselect:** Partition around the $k$th largest difference for expected $O(n)$ time, though implementation and worst-case guarantees are more involved.
- **Dynamic programming:** A state by prefix and number assigned to mouse one works in $O(nk)$ time, but ignores the independent additive structure.
- **Sort rewards independently:** This is invalid because rewards at the same index describe the same cheese and must remain paired.
- **`k = 0`:** The first slice is empty, so every cheese goes to the second mouse.
- **`k = n`:** The second slice is empty, so every cheese goes to the first mouse.
- **All differences negative:** Exactly $k$ transfers are still required; choose the least negative ones.
- **Tied differences:** Any tied ownership choice gives the same total.
- **Large raw reward versus difference:** Selection must use comparative gain, not `reward1[i]` alone.
- **Input preservation:** Sorting a separate index list leaves both reward arrays in their original order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the number of cheese types. Building the index range and sorting it by differences takes $O(n\log n)$ time. Each key evaluation is $O(1)$, and Python's key-based sort computes the key once per element.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

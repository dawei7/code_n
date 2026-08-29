# Guided Example: Boats to Save People

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"people": [1, 2], "limit": 3}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `people` where $\text{people}[i]$ is the weight of the $i^{\text{th}}$ person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

The objective is to compute `1` from `{"people": [1, 2], "limit": 3}` while avoiding redundant calculations and unnecessary overhead.

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

Each boat carries at most two people, so the heaviest remaining person must take a boat on the current step. The only useful decision is whether that person can share with someone. Sorting makes the lightest and heaviest remaining weights available through two pointers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"people": [1, 2], "limit": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

- `i` points to the lightest person not yet assigned.
- `j` points to the heaviest person not yet assigned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Each loop iteration assigns the person at `j` to one boat and increments `ans`. If the lightest and heaviest fit together, `people[i] + people[j] <= limit`, the lightest person shares that boat and `i` advances. Whether or not a partner fits, `j` decreases because the heaviest person has been rescued.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"people": [1, 2], "limit": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every pairing:** Searching all pair combinations or matchings is far more expensive and unnecessary because sorted extremes determine a safe greedy choice.
- **Pair the two heaviest:** This often exceeds the limit and can waste opportunities to place light passengers with heavy ones.
- **Fill boats starting from the lightest:** Pairing two light people may leave two heavy people needing separate boats, whereas each light person could potentially share with a heavy one.
- **Counting sort:** Weight and limit are bounded by $3\cdot10^4$, so frequency counts can avoid comparison sorting and approach $O(n+\texttt{limit})$ time, at the cost of an additional weight-frequency array.
- **One person:** Exactly one boat is counted, regardless of whether twice that weight would fit.
- **All people exceed half the limit:** No two can share, so the loop uses one boat per person.
- **Every extreme pair fits:** Each boat takes two people, except possibly one final unpaired person.
- **Pair sum exactly equals limit:** The `<=` comparison allows the pair, as required.
- **Every individual is feasible:** The constraint `people[i] <= limit` guarantees no person is impossible to rescue alone.
- **Duplicate weights:** Sorting and pointer movement treat each occurrence as a distinct person.
- **Input mutation:** `people.sort()` changes the caller's order. Use `sorted(people)` if preservation is required.
- **At most two people:** Even when three or more light people have a combined weight under the limit, a boat cannot carry more than two; the algorithm never assigns a third passenger.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of people. Sorting dominates the scan.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

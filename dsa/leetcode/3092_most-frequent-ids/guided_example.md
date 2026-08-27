# Guided Example: Most Frequent IDs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 2, 1], "freq": [3, 2, -3, 1]}`
- **Required output:** `[3, 3, 2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The problem involves tracking the frequency of IDs in a collection that changes over time. You have two integer arrays, `nums` and `freq`, of equal length `n`. Each element in `nums` represents an ID, and the corresponding element in `freq` indicates how many times that ID should be added to or removed from the collection at each step.

The objective is to compute `[3, 3, 2, 2]` from `{"nums": [2, 3, 2, 1], "freq": [3, 2, -3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**The challenge is maintaining a changing maximum.** A hash map can update the frequency of one ID in expected constant time, but it cannot by itself answer “what is the largest current frequency?” without scanning every ID after every update. Such repeated scans could take quadratic time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 2, 1], "freq": [3, 2, -3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source combines three structures:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact source combines three structures:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `cnt[x]` stores the current frequency of ID `x`;
- `pq` is a min-heap of negated frequency values, which acts as a max-heap;
- `lazy[v]` records how many heap entries with frequency value `v` have become stale.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 3, 2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 2, 1], "freq": [3, 2, -3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 3, 2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Balanced ordered map of frequency multipliciti:** - **Balanced ordered map of frequency multiplicities:** Update old and new frequencies and read the largest key. This also gives $O(\log n)$ per step but Python has no built-in ordered multiset.
- **Heap with an ID in every entry:** Push each updated `(count, ID)` pair and pop while the pair's count differs from `cnt[id]`. This is often simpler conceptually and has the same asymptotic bounds.
- **Scan all IDs after each update:** The map update is easy, but repeated maximum scans can cost $O(n^2)$ overall.
- **Frequency becomes zero:** Zero may remain in both counters and the heap; the reported maximum is still zero when no positive occurrence exists.
- **Collection becomes empty:** Cleanup may empty `pq`, and the explicit conditional appends zero.
- **Repeated updates to one ID:** Each old count is marked stale and each new count is pushed; amortized cleanup still applies.
- **Several IDs share the maximum:** The answer is only the count, so one valid heap occurrence is enough.
- **Negative update:** It decreases `cnt[x]`, and the input guarantee ensures the result never drops below zero.
- **Positive update:** It may create a new maximum immediately because its negated value rises toward the heap top.
- **Stale value below the top:** Leaving it in place is safe until all larger candidates disappear.
- **Many stale entries at one value:** `lazy[value]` is a multiplicity, so cleanup removes the correct number one by one.
- **Implicit zero debt:** Marking an unseen ID's old zero is harmless for this nonnegative-maximum problem, as described above.
- **Why not delete zero keys:** Deleting them is optional bookkeeping and would not improve the asymptotic bound.
- **Large counts:** Frequencies can accumulate beyond one update's magnitude, but Python integers do not overflow.
- **Output ownership:** The heap identifies only the maximum frequency, exactly what the result requests; it deliberately cannot identify a winning ID.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of updates. Each update performs one heap push, costing $O(\log n)$. It may perform several pops, but every heap entry is pushed once and can be popped at most once. Across the whole run there are only $O(n)$ pops, each costing $O(\log n)$. The total time is therefore $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

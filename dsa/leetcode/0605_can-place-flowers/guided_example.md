# Guided Example: Can Place Flowers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"flowerbed": [1, 0, 0, 0, 1], "n": 1}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

The objective is to compute `true` from `{"flowerbed": [1, 0, 0, 0, 1], "n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Padding removes boundary special cases

The first line creates:



The artificial zeros represent empty space just outside the original bed. Every original plot now has both a left and right array neighbor, including the original endpoints. Planting at the first original plot is legal exactly when that plot and its real right neighbor are zero; the artificial left zero contributes no restriction. The last plot is symmetric.

The loop runs from index one through the next-to-last index, so it visits exactly original plots and never plants in a sentinel.

This expression constructs a new list and rebinds the local variable. The caller’s original list is not mutated, even though the padded working list is updated.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"flowerbed": [1, 0, 0, 0, 1], "n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Testing a three-plot neighborhood

For current index `i`:



The slice contains left neighbor, current plot, and right neighbor. Values are only zero or one, so their sum is zero if and only if all three are empty.

If legal, the algorithm writes one at the current position and decrements the remaining requirement `n`. Mutating the working list is essential: when the scan reaches `i + 1`, it sees the newly planted flower on its left and cannot plant adjacently.

The slice has fixed length three, so allocation and summation are constant work per iteration, though direct comparisons would avoid the temporary slice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why planting immediately is optimal

Consider the leftmost index at which the greedy scan plants. Its left neighbor is empty and already finalized; its right neighbor is empty. Any feasible plan for the remaining bed has two possibilities:

- it also plants at this index;
- it does not.

If it does not, the earliest new flower it could place in this local area is at least one position to the right. If a feasible optimal plan plants at the immediate right position, move that flower left to the greedy index. The left side is safe by the greedy test, and moving left cannot conflict with any later flower that did not already conflict with the original right-position flower. If the plan plants even later, adding or choosing the greedy position similarly consumes no more suffix capacity than waiting.

Thus, there exists an optimal placement agreeing with the greedy decision. Repeating the exchange argument at each planted position proves that the scan finds a maximum-cardinality set of new nonadjacent flowers.

Another view uses runs of zeros. For each empty run bounded by existing flowers or bed edges, placing at the leftmost legal position and then every other position achieves the run’s maximum. The scan performs exactly that pattern across all runs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"flowerbed": [1, 0, 0, 0, 1], "n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **In-place boundary checks:** Test current zero plus `i == 0 or left zero` and `i == m-1 or right zero`. Achieves $O(1)$ auxiliary space but mutates the caller’s array.
- **Previous/next state without mutation:** Track whether the previous plot is occupied and inspect the next input value. Can preserve input with constant extra state if carefully advanced.
- **Count zero runs mathematically:** Derive capacity for interior and edge runs. Avoids mutation but requires separate formulas for boundary runs.
- **Early return:** As soon as remaining `n <= 0`, return true. Improves best-case time but not the $O(m)$ worst case.
- **Request zero:** Always feasible. The exact source still scans and may plant in its private copy, then returns true.
- **Single empty plot:** Padding makes both virtual neighbors zero, so one flower can be planted.
- **Single occupied plot:** No placement is possible.
- **All-zero bed:** Greedy plants indices 0, 2, 4, ... in original coordinates, which is maximum.
- **Endpoint planting:** Sentinel zeros correctly allow it when the one real neighbor is empty.
- **New adjacency:** Mutating the working list blocks the next plot immediately.
- **Existing valid-bed guarantee:** No two original ones are adjacent; behavior on invalid input is outside the contract.
- **Input preservation:** Because of list concatenation, the original `flowerbed` object remains unchanged.
- **Fixed-size slice:** It is constant time per position but still allocates a tiny temporary; direct comparisons are leaner.
- **Space fidelity:** Padding is an $O(m)$ copy. The manifest’s $O(1)$ space describes a different implementation of the same greedy rule.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m$ be the original flowerbed length. Constructing the padded list takes $O(m)$ time. The loop visits $m$ original positions and performs fixed-size slice/sum work, so total time is $O(m)$.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

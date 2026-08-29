# Guided Example: Sort Array by Moving Items to Empty Space

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 0, 3, 1]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of size `n` containing **each** element from `0` to $n - 1$ (**inclusive**). Each of the elements from `1` to $n - 1$ represents an item, and the element `0` represents an empty space.

The objective is to compute `3` from `{"nums": [4, 2, 0, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A move is a swap with the empty position

Moving any item into the empty space places zero where that item used to be. Operationally, every move swaps value 0 with one other value. The array is a permutation, so cycle decomposition describes how many such swaps are needed to reach a chosen target layout.

There are two valid targets. The helper `f` measures the cost to reach an identity permutation, with parameter `k` identifying the target position of the empty value in the representation being evaluated.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 0, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cycle decomposition against the identity

Treat `nums[i]` as a mapping from position `i` to the value that belongs at position `nums[i]` in the identity target. A fixed position `i == nums[i]` needs no move. Every other position belongs to a nontrivial permutation cycle.

The visited loop discovers each nontrivial cycle once. Before walking a new cycle it adds one to `cnt`, and inside the walk it adds one for every cycle position. A cycle of length $L$ therefore initially contributes $L+1$.

This $L+1$ is the correct cost for a cycle that does not contain the empty position:

1. Swap the empty space into the cycle, costing one move.
2. Use the empty position to place cycle items into their targets.
3. The sequence requires $L$ further swaps before the empty space exits and the cycle is fixed.

Equivalently, an ordinary item-only cycle needs one entry/exit overhead beyond its $L$ elements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The cycle containing empty is cheaper

If the target position `k` already holds the empty label, `nums[k] == k`, zero is fixed and belongs to no nontrivial cycle. Every discovered nontrivial cycle needs the $L+1$ treatment.

If `nums[k] != k`, position `k` lies in one nontrivial cycle containing the empty label. That cycle needs only $L-1$ swaps: the empty space is already inside it, and each swap can place one item correctly until the cycle closes.

The generic count assigned that cycle $L+1$, two too many. Therefore

`cnt - 2 * (nums[k] != k)`

subtracts exactly two when the empty cycle is nontrivial.

For multiple nontrivial cycles, only one can contain zero. All other cycles still require using zero to enter and leave them, so their $L+1$ costs remain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 0, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate greedy swaps for each target:** Maintain value positions and repeatedly put the needed item into the empty slot. This can achieve linear time but cycle decomposition gives a cleaner move-count proof.
- **General minimum-swap count:** Ordinary arbitrary swaps need $L-1$ per cycle, but restricting every swap to involve zero creates the extra $L+1$ cost for cycles without zero.
- **Already sorted in either layout:** The corresponding identity representation has no nontrivial cycle and returns zero.
- **Empty fixed for one target:** No subtraction occurs because zero is outside all nontrivial cycles.
- **Empty inside a nontrivial cycle:** Exactly one cycle receives the two-move discount.
- **Several item-only cycles:** Each requires its own empty-space entry and exit overhead.
- **Two valid targets:** Evaluating only empty-at-beginning could miss a cheaper or already sorted empty-at-end arrangement.
- **Shift transformation:** Adding `n` before modulo keeps original zero mapped correctly to `n-1`.
- **Permutation guarantee:** Every mapping decomposes into closed cycles; duplicates or missing values would invalidate this reasoning.
- **One nontrivial two-cycle with empty:** It costs one move, and the formula `L+1-2` gives one.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For one call to `f`, every index is marked visited at most once, so cycle discovery takes $O(n)$ time and the visited list uses $O(n)$ space. The helper is called twice. Constructing the shifted permutation also takes $O(n)$ time and space. Total time is $O(n)$ and peak auxiliary space is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

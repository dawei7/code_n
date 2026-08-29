# Guided Example: Minimum Number Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 4, 2, 3]}`
- **Required output:** `[3, 2, 5, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of **even** length and there is also an empty array `arr`. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

The objective is to compute `[3, 2, 5, 4]` from `{"nums": [5, 4, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each round consumes the two smallest remaining values

Alice removes the minimum remaining value first, then Bob removes the new minimum. Bob appends his removed value before Alice appends hers. If the two removed values are $a \le b$, the round contributes `[b, a]` to the result.

The implementation models the changing minimum with a min-heap. `heapify(nums)` rearranges the input list in place so that `nums[0]` is the smallest value and the heap property supports efficient repeated removal.

During each loop iteration, `a = heappop(nums)` removes Alice’s minimum. The next `heappop` removes Bob’s minimum `b` from what remains. The code appends `b` and then `a`, exactly reversing their removal order as the game requires. Because the input length is even, two pops are always available until the heap becomes empty.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 4, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why heap extraction reproduces the rules exactly

A Python min-heap guarantees that `heappop` returns a smallest element currently stored. Before the first pop of a round, the heap contains precisely all values not removed in earlier rounds, so `a` is Alice’s required choice. After that pop, the heap contains precisely the values Bob is allowed to choose from, so `b` is Bob’s required minimum.

Appending Bob’s value first and Alice’s second matches the distinct append rule; it is not enough merely to return values in sorted order. Repeating the same exact simulation until the heap is empty produces the unique result array.

For `nums = [5, 4, 2, 3]`, heap extraction yields two and then three, so the first output pair is `[3, 2]`. The remaining values are four and five; extraction yields them in that order and appending reverses them to `[5, 4]`. The complete answer is `[3, 2, 5, 4]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Relationship to sorting

If all values were sorted as

`x0 <= x1 <= x2 <= x3 <= ...`,

the removal sequence would be exactly that sorted sequence. The game’s append sequence swaps every adjacent pair, producing

`[x1, x0, x3, x2, ...]`.

The manifest summary describes that sort-and-swap perspective, but the exact protected solution does not call `sort`. It uses `heapify` followed by repeated `heappop` operations. Both approaches produce the same result, but their data flow and some implementation-space details differ.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 2, 5, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 4, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 2, 5, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort and swap adjacent pairs:** Sorting once and emitting `nums[1], nums[0], nums[3], nums[2], ...` is equally correct and also takes $O(N\log N)$ time. It matches the manifest summary more literally than this heap source.
- **Repeated linear minimum search:** Removing the minimum twice per round from an ordinary list can take $O(N^2)$ time.
- **Counting frequencies:** Since values have a small stated range, a counting array can generate minima in $O(N+V)$ time, but it relies on that bound and needs extra range storage.
- **Duplicate minima:** Equal values can be popped in any internal order because only values, not identities, appear in the answer.
- **Two elements:** The heap pops the smaller for Alice and the larger for Bob, then returns them as `[larger, smaller]`.
- **Even-length guarantee:** It ensures the second pop of every round exists. Without it, the rules would leave an unmatched value.
- **Input mutation:** The exact implementation empties `nums`. Copying before `heapify` would preserve the caller’s list but require $O(N)$ additional space.
- **No adversarial strategy:** Names of players do not imply choices; both minimum removals are mandatory.
- **Pair order:** Appending `a` before `b` would return the removal order, not the required Bob-before-Alice append order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the original number of elements. `heapify` takes $O(N)$ time. There are $N$ heap pops, each costing $O(\log N)$ in the worst case as the heap shrinks. Appends are amortized $O(1)$. The total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

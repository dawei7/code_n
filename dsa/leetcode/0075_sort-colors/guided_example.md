# Guided Example: Sort Colors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 0, 2, 1, 1, 0]}`
- **Required output:** `[0, 0, 1, 1, 2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` with `n` objects colored red, white, or blue, sort them **<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

The objective is to compute `[0, 0, 1, 1, 2, 2]` from `{"nums": [2, 0, 2, 1, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain four consecutive regions

The array contains only `0`, `1`, and `2`, and their required sorted order is exactly their numeric order. The implementation uses three indices to maintain these regions:

- Positions `0` through `i` contain confirmed zeroes.
- Positions `i + 1` through `k - 1` contain confirmed ones.
- Positions `k` through `j - 1` have not yet been classified.
- Positions `j` through the end contain confirmed twos.

Here `i` is the last index of the zero region, `j` is the first index of the two region, and `k` is the first unclassified index. The initialization `i = -1`, `j = len(nums)`, and `k = 0` makes all three classified regions empty and makes the entire array the unknown region. Using `-1` and `len(nums)` as outside sentinels avoids special cases for the first zero and first two.

The loop continues while `k < j`. This condition says that at least one unclassified position remains. Each branch classifies at least one position, so the unknown interval steadily disappears.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 0, 2, 1, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Place a zero at the next left position

When `nums[k] == 0`, the zero belongs immediately after the existing zero region. The source first increments `i`, making it the destination for the next zero, and swaps `nums[i]` with `nums[k]`.

If `i == k`, the swap is with itself and simply confirms that position as zero. If `i < k`, the old value at the new `i` came from the confirmed-one region, because positions between the old zero boundary and `k` are all ones. The swap moves the zero left and moves that one to position `k`. Incrementing `k` then includes the moved one in the confirmed-one region. Both swapped values are therefore fully classified, which is why advancing `k` is safe in this branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `nums[k] == 0`, the zero belongs immediately after the ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Place a two at the next right position

When `nums[k] == 2`, the source decrements `j` and swaps the current two with `nums[j]`. The two is now at the first position of the confirmed-two suffix, so that suffix grows leftward by one.

Crucially, `k` does not advance. The value moved from `j` came from the unknown region unless `j` has just met `k`. It might be zero, one, or two and must be inspected. Advancing immediately would skip that value and could leave the array unsorted. Rechecking the same `k` is the defining asymmetry of the algorithm.

If decrementing `j` makes `j == k`, the swap is effectively at the boundary and the loop ends. No unknown position remains.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 0, 1, 1, 2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 0, 2, 1, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 0, 1, 1, 2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Counting two passes:** Count how many zeroes, :** - **Counting two passes:** Count how many zeroes, ones, and twos occur, then overwrite the array in blocks. It is $O(n)$ time and $O(1)$ space but does not satisfy the one-pass follow-up.
- **Library sort:** It would obscure the three-value structure, typically costs $O(n\log n)$, and is explicitly forbidden.
- **Stable partition:** Preserving relative identity within each color is unnecessary because equal integer color codes are indistinguishable; stable in-place partitioning would add complexity.
- **All zeroes:** Every iteration grows the zero prefix, often through self-swaps.
- **All ones:** `k` simply scans to `j` without any swaps.
- **All twos:** `j` repeatedly moves left while `k` stays until the unknown interval vanishes.
- **Single element:** One branch classifies it and the loop ends.
- **Zero swapped from the right:** The unchanged `k` after a two swap ensures it is processed next.
- **Two swapped from the right:** It is processed again and moved into the still-growing suffix.
- **Already sorted input:** The pointers scan once; zero self-swaps are harmless and the result remains sorted.
- **Reverse-grouped input:** Swaps progressively exchange left twos with right zeroes without extra storage.
- **Input-domain reliance:** The `else` branch means “one” only because no other integer is allowed.
- **Mutation contract:** Callers must inspect the changed list, not a return value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. In every iteration either `k` increases or `j` decreases. Neither moves in the opposite direction, so there are at most about $2n$ pointer movements and $O(n)$ total time. This matches the manifest and fulfills the one-pass follow-up even though a value swapped from the right may be inspected on the next iteration.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

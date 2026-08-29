# Guided Example: Dinner Plate Stacks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"capacity": 1, "operations": [["pop", []], ["popAtStack", [0]]]}`
- **Required output:** `[-1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have an infinite number of stacks arranged in a row and numbered (left to right) from `0`, each of the stacks has the same maximum capacity.

The objective is to compute `[-1, -1]` from `{"capacity": 1, "operations": [["pop", []], ["popAtStack", [0]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two different choices must stay efficient

`push` must find the leftmost stack with free capacity. `pop` must find the rightmost nonempty stack. `popAtStack` can create a hole in the middle that a later push should fill before using stacks farther right.

A plain list of stacks gives direct indexed access, but scanning from the left for every push can be slow when many early stacks are full. The solution combines:

- `stacks`, a list of the actual stack lists;
- `not_full`, a sorted set of indices whose existing stacks have room.

The sorted set's first element is always the smallest available index, exactly what `push` needs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"capacity": 1, "operations": [["pop", []], ["popAtStack", [0]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain no useless empty stacks at the right edge

Internal empty stacks must remain addressable because their indices cannot shift. However, empty stacks at the end of `stacks` can be removed safely: no later stack exists whose index would change.

The implementation maintains the invariant that `stacks` has no trailing empty stack after a successful pop. Consequently, the last list entry, when any exists, is the rightmost nonempty stack. This makes `pop` a call to `popAtStack(len(stacks) - 1)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Push into the leftmost available stack

If `not_full` is nonempty, `not_full[0]` gives its minimum index. The value is appended there.

If that stack reaches `capacity`, its index is discarded from `not_full` because it can accept no more values. If it remains below capacity, it stays in the set for another push.

If `not_full` is empty, every existing stack is full. The leftmost nonfull position is therefore the next new index, so the code appends `[val]` to `stacks`. When capacity is greater than one, the new stack still has room and its index is added to the set. For capacity one, the new stack is already full and is not added.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"capacity": 1, "operations": [["pop", []], ["popAtStack", [0]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan from index zero on every push:** This can take `O(s)` per push when many early stacks are full.
- **Use a min-heap of nonfull indices:** A heap can find the leftmost hole, but duplicate and stale entries require lazy cleanup. `SortedSet` maintains unique live indices directly.
- **Use a max-heap for nonempty indices as well:** That can support rightmost pop, but the no-trailing-empty invariant makes a second ordered structure unnecessary.
- **Capacity one:** Every push creates a full stack, and `not_full` remains empty until internal pops create holes.
- **Pop from an internal stack:** Its index is added to `not_full` so the next appropriate push can fill the hole.
- **Pop from an empty or missing index:** Return `-1` and leave all invariants unchanged.
- **Several trailing empty holes:** Empty internal stacks can become trailing after a later stack is removed; the cleanup loop removes all of them.
- **All stacks empty:** Cleanup makes `stacks` empty, and ordinary pop delegates with index negative and returns `-1`.
- **Duplicate values:** Stack selection depends on positions and capacity, not value uniqueness.
- **Amortized cleanup:** A single pop can trim many slots, but every trimmed slot was created earlier and is removed only once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m log s)$. Let `s` be the number of existing stack slots, `v` the number of stored values, and `m` the number of operations.
- **Auxiliary Space Complexity:** $O(v + s)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

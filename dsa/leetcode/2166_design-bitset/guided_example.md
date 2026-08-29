# Guided Example: Design Bitset

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"], "arguments": [[5], [3], [1], [], [], [0], [], [], [0], [], []]}`
- **Required output:** `[null, null, null, null, false, null, null, true, null, 2, "01010"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **Bitset** is a data structure that compactly stores bits.

The objective is to compute `[null, null, null, null, false, null, null, true, null, 2, "01010"]` from `{"operations": ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"], "arguments": [[5], [3], [1], [], [], [0], [], [], [0], [], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Establish the core invariant

At every index, exactly one of `a[idx]` and `b[idx]` is `'1'`. Initially, `a` contains all zeros and `b` all ones, so the invariant holds.

`cnt` stores the number of ones in the currently visible array `a`. It begins at zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"], "arguments": [[5], [3], [1], [], [], [0], [], [], [0], [], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fix one bit

If `a[idx] == '0'`, `fix` changes it to one and increments `cnt`. If it was already one, neither action occurs, preserving idempotence.

The assignment `b[idx] = '0'` is performed in either case. After the method, the visible bit is one and its complement is zero, so the two-array invariant holds.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Unfix one bit

`unfix` is symmetric. If the visible bit is one, it becomes zero and `cnt` decreases. If already zero, the count remains unchanged. Setting `b[idx] = '1'` restores the complementary value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, null, false, null, null, true, null, 2, "01010"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"], "arguments": [[5], [3], [1], [], [], [0], [], [], [0], [], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, null, false, null, null, true, null, 2, "01010"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One array plus inversion flag:** Interpret each stored bit through a global flipped boolean. This uses one array rather than two but makes fix and unfix compare physical and logical values carefully.
- **Flip by scanning:** Rewriting all bits makes one flip $O(n)$ and can be too slow across $10^5$ calls.
- **Recount on every query:** Maintaining `cnt` avoids repeated $O(n)$ scans.
- **Fix an existing one:** The count must not increase twice; the conditional prevents it.
- **Unfix an existing zero:** The count likewise remains unchanged.
- **Repeated flips:** Two swaps restore the original arrays and two count complements restore the original count.
- **Size one:** All operations and aggregate predicates follow the same invariants.
- **All bits fixed:** `cnt == size` makes `all` true; flipping makes the count zero.
- **No bits fixed:** `one` is false until a fix or suitable flip creates a one.
- **String output:** Joining `a` uses current logical order and does not expose `b`.
- **Character storage:** Bits are strings because `toString` can join them directly.
- **Index validity:** The contract guarantees every `idx` is inside the allocated lists.
- **Output allocation:** Even with constant-time updates, returning an $n$-character string necessarily costs $O(n)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Construction allocates and fills two length-$n$ lists, taking $O(n)$ time and space. `fix`, `unfix`, `flip`, `all`, `one`, and `count` each use $O(1)$ time. `toString` takes $O(n)$ time and creates an $O(n)$ output string.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

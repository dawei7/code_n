# Guided Example: Min Stack

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["MinStack", "push", "getMin", "top"], "arguments": [[], [1], [], []]}`
- **Required output:** `[null, null, 1, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

The objective is to compute `[null, null, 1, 1]` from `{"operations": ["MinStack", "push", "getMin", "top"], "arguments": [[], [1], [], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why an ordinary stack is not enough

A normal stack can return or remove its top in constant time because the top is
stored at a known end of the underlying list. Its minimum is different: without
extra information, `getMin()` would have to inspect every active value. That
would take linear time and violate the requirement that every operation be
$O(1)$.

The key observation is that stack history is nested. While a value remains in
the stack, nothing below it changes. Therefore, for every depth, the minimum of
the prefix ending at that depth can be computed once during `push` and kept
until the matching `pop`.

The selected class represents this history with two synchronized lists:

- `stk1[i]` is the actual value pushed at depth `i`;
- `stk2[i + 1]` is the minimum of all actual values from depth zero through
  depth `i`.

`stk2` has one extra entry at its bottom: positive infinity. That sentinel is
the minimum of an empty conceptual prefix and lets the first `push` use exactly
the same formula as every later push.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["MinStack", "push", "getMin", "top"], "arguments": [[], [1], [], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Push a value and its prefix minimum together

For `push(val)`, the source first appends `val` to `stk1`. It then computes
`min(val, stk2[-1])` and appends that result to `stk2`.

Suppose the old stack minimum was $m$. After pushing $v$, every earlier value
is unchanged, so the new minimum can only be one of two values: the old minimum
$m$, or the newly introduced value $v$. Hence the new minimum is
$\min(v,m)$. No scan is necessary.

For the first push, the old tracker top is infinity. Every allowed integer is
smaller than infinity, so the appended tracker value is the first actual value.
The sentinel removes the need for a special empty-stack branch.

Equal minima are deliberately repeated. If the current minimum is `-2` and
another `-2` is pushed, the tracker receives another `-2`. This is useful:
each actual stack entry has exactly one matching tracker entry, so a pop can
remove one item from each list without counting duplicates or comparing values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For `push(val)`, the source first appends `val` to `stk1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep both lists synchronized on removal

`pop()` calls `pop()` once on `stk1` and once on `stk2`. Before the operation,
an actual stack of size $k$ has a tracker of size $k+1$, including the
sentinel. After removing one entry from each, their size difference remains
one.

The tracker value exposed afterward was created when the new top was pushed.
It is therefore exactly the minimum of all entries that still remain. This
holds whether the removed value was larger than the minimum, was the only
occurrence of the minimum, or was one of several equal minima.

The problem guarantees that `pop()` is called only on a nonempty stack. As a
result, the actual list never underflows, and the sentinel is never removed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, 1, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["MinStack", "push", "getMin", "top"], "arguments": [[], [1], [], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, 1, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One stack of pairs:** Store `(value, minimum_s:** - **One stack of pairs:** Store `(value, minimum_so_far)` at every depth. It expresses the same invariant with one container and the same $O(n)$ storage.
- **Two stacks with change points:** Keep all values in one stack and push onto a minimum stack only when a value is at most the current minimum. Equal minima must also be tracked, or counted, so popping one duplicate does not lose the remaining minimum.
- **Difference encoding:** Store differences relative to the current minimum and restore the previous minimum algebraically when a negative marker is popped. It uses one list but requires more careful arithmetic.
- **Scan during `getMin`:** Uses no minimum history, but a query becomes $O(n)$ and violates the contract.
- **Heap or balanced tree:** Maintaining deletions consistently costs at least logarithmic time and is unnecessary for stack-ordered removal.
- **Repeated minimum:** The tracker intentionally stores repeated prefix minima, so removing one occurrence leaves the next correct tracker entry.
- **First push:** The infinity sentinel makes the ordinary minimum formula valid, provided `inf` is defined.
- **Pop to empty:** The actual list becomes empty while the tracker returns to `[inf]`; the contract prevents `top()` or `getMin()` at that moment.
- **Full integer range:** Comparing an allowed integer with mathematical infinity is safe in Python.
- **Undefined sentinel name:** Standalone use must define `inf`; otherwise even construction fails before any stack operation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of values currently in the logical stack, and let $q$ be
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

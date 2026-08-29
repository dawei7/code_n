# Guided Example: Zigzag Iterator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"v1": [1, 2], "v2": [3, 4, 5, 6]}`
- **Required output:** `[1, 3, 2, 4, 5, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two vectors of integers `v1` and `v2`, implement an iterator to return their elements alternately.

The objective is to compute `[1, 3, 2, 4, 5, 6]` from `{"v1": [1, 2], "v2": [3, 4, 5, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent iteration with one cursor per vector

The exact source stores references to the two input vectors in `vectors` and stores their next unread indices in `indexes`. Initially both indices are zero. It also keeps `cur`, the vector that should be considered next, and `size = 2`.

The iterator does not merge or copy the vector contents. Its complete logical position is described by three small pieces of state:

- `indexes[0]`: the next unread position in `v1`;
- `indexes[1]`: the next unread position in `v2`; and
- `cur`: which vector currently has the turn.

This differs from the manifest's deque-of-active-vectors summary. The protected implementation uses cyclic indices and lets `hasNext()` skip exhausted vectors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"v1": [1, 2], "v2": [3, 4, 5, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Let `next()` consume exactly one current element

When called in the intended protocol, `next()` assumes `cur` points to a vector with an unread element. It retrieves that vector and its saved index, reads the element, increments only that vector's index, and advances `cur` cyclically:

$$
\texttt{cur}=(\texttt{cur}+1)\bmod 2.
$$

Advancing after every returned element creates alternation while both vectors still contain values. Consuming from `v1` gives `v2` the next turn; consuming from `v2` wraps back to `v1`.

The saved indices advance independently. Returning an element from one vector does not change the unread position of the other, so every original vector preserves its internal order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Make `hasNext()` both a query and a positioning step

After one vector is exhausted, blindly alternating to it would make `next()` index past its end. The exact design handles this in `hasNext()`.

Starting from the current turn, `hasNext()` checks whether `indexes[cur] == len(vectors[cur])`. Equality means every element of that vector has been returned. If so, it rotates `cur` to the next vector and checks again.

When it encounters a vector whose saved index is smaller than its length, the loop ends and `hasNext()` returns true. At that moment it has also positioned `cur` so the following `next()` call is safe and returns the correct next available vector's element.

This state-changing behavior is intentional. `hasNext()` is not a purely observational method in this implementation; it normalizes `cur` past exhausted vectors.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 2, 4, 5, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"v1": [1, 2], "v2": [3, 4, 5, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 2, 4, 5, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deque of active positions:** Enqueue each nonempty vector's `(vector index, element index)`, pop one for `next()`, and re-enqueue its advanced position only if elements remain. This avoids repeatedly scanning exhausted vectors and extends cleanly to $K$ vectors, but it is not the exact source.
- **Precompute the merged result:** Building the complete zigzag list makes later calls simple but costs $O(N)$ additional storage and performs work even if the caller stops early.
- **One vector empty initially:** `hasNext()` rotates to the nonempty vector before `next()`, so all of its values are returned in order.
- **One vector exhausts early:** The exhausted vector is skipped on later turns, and the longer vector supplies its remaining suffix without loss.
- **Equal-length vectors:** Turns alternate until both become exhausted together, after which the full-cycle check returns false.
- **Both empty outside the total-length constraint:** The constructor still works; the first `hasNext()` completes a cycle and returns false.
- **Repeated `hasNext()` calls:** They do not advance past an available vector and therefore do not consume data.
- **Calling `next()` without a successful check:** The exact implementation offers no guard and may index an empty vector. Clients must follow the documented iterator loop.
- **Values and duplicates:** Element magnitude, sign, and equality do not affect scheduling. The iterator preserves all values and each vector's internal order.
- **Generalized cyclic order:** With $K$ vectors, advancing modulo $K$ yields round-robin order, while exhausted vectors must be skipped. The same structure works functionally, though a deque improves worst-case per-call efficiency.
- **Input mutation by callers:** The iterator keeps references rather than snapshots. Changing vector lengths or contents during iteration can invalidate saved indices or alter returned values; such concurrent mutation is outside the intended contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. For exactly two vectors, `next()` performs a constant number of reads, writes, and arithmetic operations, so it takes $O(1)$ time. `hasNext()` examines at most two vectors before either finding an element or completing a cycle, so it also takes $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

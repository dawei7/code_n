# Guided Example: Flatten 2D Vector

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"vec": [[1, 2], [3], [4]]}`
- **Required output:** `[1, 2, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design an iterator to flatten a 2D vector. It should support the `next` and `hasNext` operations.

The objective is to compute `[1, 2, 3, 4]` from `{"vec": [[1, 2], [3], [4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The normalized cursor state

After `forward()` finishes, exactly one of two conditions holds:

1. `i < len(vec)` and `j < len(vec[i])`, so `(i, j)` identifies the next integer to return; or
2. `i == len(vec)`, so every row has been exhausted and no next integer exists.

The helper loops while `i` is a valid row and `j >= len(vec[i])`. An empty row has length zero, so `j = 0` already satisfies the exhaustion condition. A consumed nonempty row also satisfies it after `next()` increments `j` past the last valid position. In either case, the helper advances to the following row and resets `j = 0`.

The condition uses `>=` rather than equality. Under normal valid operations, `j` reaches exactly the row length, but `>=` expresses the broader truth that any position at or beyond the end is invalid and makes the helper robust to that state.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"vec": [[1, 2], [3], [4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How `next()` consumes one value

`next()` first calls `forward()`. This ensures that any empty or exhausted rows have been skipped before indexing. It then reads `vec[i][j]`, increments `j`, and returns the saved value.

Incrementing `j` after reading is important: the current coordinate always means “the next value not yet returned,” not “the value returned most recently.” After the final value in a row, `j` becomes equal to that row's length. The method does not immediately seek the next row; the next operation performs that work lazily through `forward()`.

The contract guarantees every call to `next()` is valid. Therefore, after normalization inside `next()`, the exhausted state cannot occur. If a caller violated that precondition, indexing `vec[len(vec)]` would raise an error; the class is not required to manufacture a sentinel result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `next()` first calls `forward()`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How `hasNext()` inspects without consuming

`hasNext()` also begins with `forward()`, then returns whether `i < len(vec)`. If a valid row remains, normalization guarantees a valid element exists there. If `i` has reached the number of rows, no remaining row or element exists.

Calling `hasNext()` may move across empty or exhausted rows, but it never advances past a real integer. Once `(i, j)` points to a value, repeated calls to `hasNext()` cause the loop condition to fail immediately and leave the cursor unchanged. This idempotence is crucial for iterator behavior: clients often call `hasNext()` several times before calling `next()`, and those checks must not skip data.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"vec": [[1, 2], [3], [4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Flatten in the constructor:** Copy every integ:** - **Flatten in the constructor:** Copy every integer into one list and iterate with one index. Then each public operation is strict $O(1)$, but construction costs $O(N+V)$ time and storage costs $O(N)$, defeating the lazy iterator design.
- **Store row iterators:** Keep an iterator over rows and a current inner iterator, advancing until one has data. This matches the follow-up style in iterator-oriented languages and retains lazy $O(1)$ auxiliary state when the underlying iterators are references.
- **Leading empty rows:** The first operation skips them; the constructor remains $O(1)$.
- **Empty rows between values:** `forward()` may cross any number of them and stops at the next actual integer.
- **Trailing empty rows:** After the last value, normalization consumes all remaining empty rows and sets `i` to `len(vec)`.
- **Completely empty outer vector:** `i` starts equal to `len(vec)`, so `hasNext()` returns `false` immediately.
- **Only empty inner vectors:** One `hasNext()` may scan all rows and returns `false`; subsequent calls are constant time because the exhausted cursor is stable.
- **Repeated `hasNext()` calls:** Once normalized at a valid element or at exhaustion, further checks do not advance anything and return the same answer until `next()` consumes a value.
- **`next()` without a preceding `hasNext()`:** It is supported because `next()` performs its own normalization.
- **Invalid `next()` after exhaustion:** The contract guarantees this does not happen. The source would raise an indexing error rather than return a sentinel.
- **Rows with negative values or duplicates:** Values are returned unchanged. Cursor logic depends only on structure and lengths, not on integer contents.
- **External mutation:** Because `vec` is stored by reference, changing it during iteration can alter the observed sequence. Standard iterator use assumes the backing collection is not structurally modified unless explicitly supported.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $V$ be the number of inner rows, $N$ the total number of integers, and $C$ the number of public method calls. The constructor performs three assignments and takes $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Peeking Iterator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"iterator_data": [1, 2, 3], "operations": ["next", "peek", "next", "next", "hasNext"]}`
- **Required output:** `[1, 2, 2, 3, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design an iterator that supports the `peek` operation on an existing iterator in addition to the `hasNext` and the `next` operations.

The objective is to compute `[1, 2, 2, 3, false]` from `{"iterator_data": [1, 2, 3], "operations": ["next", "peek", "next", "next", "hasNext"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why peeking requires one saved value

The underlying iterator exposes only `next()` and `hasNext()`. Calling its `next()` is destructive from the caller's perspective: it returns the current element and advances the underlying position. There is no method for moving that iterator backward.

To implement `peek()`, the wrapper must learn the next value without advancing its own logical position. The only available way to learn that value is to call the underlying `next()`, so the wrapper must save the returned element and give it back later when its own `next()` is called.

Only one value of lookahead is required. `peek()` asks about the immediate next element, not an arbitrary future offset. The exact source stores that one possible value in `peeked_element` and records whether the cache is occupied in `has_peeked`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"iterator_data": [1, 2, 3], "operations": ["next", "peek", "next", "next", "hasNext"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a flag instead of treating `None` as the state

The constructor initializes



The Boolean is the authoritative state. `peeked_element` is meaningful only when `has_peeked` is true. This separation is stronger than checking whether the cached value is `null`: in a generic iterator, `null` might itself be a legitimate element. A separate occupancy flag distinguishes “a cached value whose value happens to be `null`” from “there is no cached value.”

Although the current problem uses positive integers, the exact design already contains the key mechanism needed by the generic follow-up.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor initializes



The Boolean is the authoritat... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Two logical states describe the wrapper

When `has_peeked` is false, no element is buffered. The wrapper's next logical value is still the underlying iterator's next value.

When `has_peeked` is true, `peeked_element` is the wrapper's next logical value. The underlying iterator has already advanced one position beyond it, but that advancement is hidden from users until the wrapper's `next()` consumes the cache.

This distinction between physical underlying position and logical wrapper position is the heart of the design. A peek may advance the wrapped object internally, yet the public sequence does not advance because the fetched value remains pending in the cache.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 2, 3, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"iterator_data": [1, 2, 3], "operations": ["next", "peek", "next", "next", "hasNext"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 2, 3, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefetch in the constructor:** Always store th:** - **Prefetch in the constructor:** Always store the next element immediately and refill after every `next()`. This can simplify method branches, but construction must handle an empty iterator and performs work even if no method is called. The exact source fetches lazily.
- **Copy all remaining values:** Materializing the iterator into a list makes peeking easy but uses $O(n)$ space, fails for infinite streams, and defeats the iterator abstraction.
- **Use `null` as the only sentinel:** This works only if `null` can never be a real element. The explicit `has_peeked` flag is safer and supports generic value types.
- **Repeated peeks:** Only the first fills the cache. Every later peek returns the same pending value without advancing anything further.
- **Peek at the final element:** The underlying iterator becomes physically exhausted, but `hasNext()` remains true because the cached final element is still logically available.
- **Next after peek:** It must return the cache and must not call the underlying iterator again, or the peeked value would be skipped.
- **Next without peek:** Direct delegation is correct because no buffered value stands between the wrapper and the underlying sequence.
- **Valid-call guarantee:** The source assumes `peek()` and `next()` are never requested when no logical element remains. It does not define a custom exception path for invalid calls.
- **Empty iterator outside current constraints:** Construction remains safe because it does not prefetch. `hasNext()` delegates and returns false; invalid `peek()` or `next()` would rely on the underlying iterator's behavior.
- **Generic values:** Replacing integer-specific annotations with a type parameter is sufficient for storage and returns. The existing Boolean occupancy flag already permits falsey values such as `0`, `false`, empty strings, and even `null`.
- **External use of the wrapped iterator:** The wrapper assumes exclusive control of the supplied iterator after construction. Advancing it separately would desynchronize the cached logical view and is outside the intended design.
- **Thread safety:** Concurrent method calls could race on the cache fields. The interview design is single-threaded; a shared concurrent wrapper would need synchronization.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Each wrapper method performs a constant number of flag checks, assignments, and at most one underlying iterator call. Assuming the supplied iterator's `next()` and `hasNext()` are $O(1)$, constructor, `peek()`, `next()`, and `hasNext()` each take $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

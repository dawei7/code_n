# Guided Example: Peeking Iterator

We trace the step-by-step single-element lookahead buffer management, idempotent `peek()` caching, cache-consuming `next()` dispatch, and virtualized `hasNext()` queries on representative iterator sequences:

- **Input:** Underlying iterator over $[1, 2, 3]$; operations: `["next", "peek", "next", "next", "hasNext"]`
- **Required output:** `[1, 2, 2, 3, false]`
- **Consecutive Peeks:** Calling `peek()` multiple times in succession returns the same cached element without advancing the underlying iterator
- **Peek at Final Element:** After peeking the last element ($3$), the underlying iterator becomes exhausted, but `hasNext()` continues to return `true` because the cached element remains pending
- **Generic Support:** Uses an explicit boolean flag `has_peeked` rather than sentinel checking (`None`), supporting arbitrary generic types including `null` and boolean values

This instance demonstrates wrapper adapter design patterns, explains the separation between the physical position of the wrapped iterator and the logical position presented to the caller, details lookahead cache transitions, and ensures all operations (`peek`, `next`, `hasNext`) run in strictly $O(1)$ constant time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an underlying sequential iterator over array $[1, 2, 3]$ supporting only:
- `next() -> int`: advances to and returns the next element.
- `hasNext() -> bool`: checks if more elements exist.

Design `PeekingIterator` to support a non-advancing `peek()` operation:
```text
Step 1: next()    -> returns 1 (underlying iterator advances to 2)
Step 2: peek()    -> inspects 2 without logical advance (caches 2)
Step 3: next()    -> returns 2 (consumes cached 2)
Step 4: next()    -> returns 3 (underlying iterator advances to end)
Step 5: hasNext() -> returns False (stream is exhausted)
Output: [1, 2, 2, 3, false]
```

### The Inherent Destructiveness of `next()`
The underlying iterator has no backward seek or rewind functionality.
To inspect the next element without advancing the client's logical cursor:
1. We must physically call `iterator.next()` to fetch the upcoming value.
2. We store that value in a 1-element cache (`peeked_element`).
3. When the user later calls `next()`, we return the cached value rather than advancing the underlying iterator again.
4. When the user calls `hasNext()`, we report `true` if either the cache is occupied OR the underlying iterator has more elements.

---

## 2. Conceptual Foundation & Invariants

### Internal State Representation
- `self.iterator`: The wrapped underlying iterator.
- `self.has_peeked: bool = False`: A boolean flag indicating whether the 1-element lookahead buffer is currently holding an unconsumed value.
- `self.peeked_element`: The cached value (valid only when `has_peeked` is True).

*(Crucial Architecture: We do not check `peeked_element is not None` because in generic collections, `None` or `0` can be a valid data element. An explicit boolean flag guarantees generic correctness)*.

### Operation Protocols

#### 1. `peek()`
- If `not self.has_peeked`:
  Fetch from underlying iterator:
  $$
  \text{self.peeked\_element} \leftarrow \text{self.iterator.next()}
  $$
  $$
  \text{self.has\_peeked} \leftarrow \text{True}
  $$
- Return `self.peeked_element`.

#### 2. `next()`
- If `not self.has_peeked`:
  Delegate directly to the underlying iterator:
  $$
  \text{return self.iterator.next()}
  $$
- If `self.has_peeked`:
  Consume the cached element and clear the buffer:
  $$
  \text{res} = \text{self.peeked\_element}
  $$
  $$
  \text{self.has\_peeked} \leftarrow \text{False}, \quad \text{self.peeked\_element} \leftarrow \text{None}
  $$
  $$
  \text{return res}
  $$

#### 3. `hasNext()`
A next element exists if either a peeked element is waiting in the buffer OR the underlying iterator has unread elements:
$$
\text{return self.has\_peeked or self.iterator.hasNext()}
$$

> **Invariant.** The logical next element visible to the caller is `self.peeked_element` if `has_peeked` is True, or `self.iterator.next()` otherwise. The underlying iterator is never ahead of the caller's logical view by more than 1 position.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence on array $[1, 2, 3]$:
Initial state: `has_peeked = False, peeked_element = None`.
Underlying iterator points to index 0 (element $1$).

---

### Step 1: Operation `next()`
- Cache check: `has_peeked == False`.
- Action: Fetch directly from underlying iterator.
  $$
  \text{res} = \text{iterator.next()} = \mathbf{1}
  $$
- Underlying iterator moves to index 1 (element $2$).
- State: `has_peeked = False, peeked_element = None`.
- Emitted: $1$.

---

### Step 2: Operation `peek()`
- Cache check: `has_peeked == False`.
- Action: Prefetch upcoming element from underlying iterator.
  $$
  \text{peeked\_element} \leftarrow \text{iterator.next()} = \mathbf{2}
  $$
  $$
  \text{has\_peeked} \leftarrow \text{True}
  $$
- Underlying iterator physically moves to index 2 (element $3$).
- State: `has_peeked = True, peeked_element = 2`.
- Emitted: $2$.
*(Logical cursor remains at element 2!)*.

---

### Step 3: Operation `next()`
- Cache check: `has_peeked == True`.
- Action: Consume cached value without touching underlying iterator.
  $$
  \text{res} = \text{peeked\_element} = \mathbf{2}
  $$
  $$
  \text{has\_peeked} \leftarrow \text{False}, \quad \text{peeked\_element} \leftarrow \text{None}
  $$
- Underlying iterator remains at index 2 (element $3$).
- State: `has_peeked = False, peeked_element = None`.
- Emitted: $2$.

---

### Step 4: Operation `next()`
- Cache check: `has_peeked == False`.
- Action: Fetch directly from underlying iterator.
  $$
  \text{res} = \text{iterator.next()} = \mathbf{3}
  $$
- Underlying iterator advances past the end of the array.
- State: `has_peeked = False, peeked_element = None`.
- Emitted: $3$.

---

### Step 5: Operation `hasNext()`
- Evaluation:
  $$
  \text{self.has\_peeked} \lor \text{self.iterator.hasNext()} = \text{False} \lor \text{False} = \mathbf{\text{False}}
  $$
- Emitted: `false`.

---

## 4. Complete Execution Trace

```text
Underlying: [1, 2, 3]

1. next():    has_peeked=F -> iterator.next() -> 1
2. peek():    has_peeked=F -> peeked_element=iterator.next()=2, has_peeked=T -> return 2
3. next():    has_peeked=T -> return 2, has_peeked=F, peeked=None
4. next():    has_peeked=F -> iterator.next() -> 3
5. hasNext(): has_peeked=F and iterator.hasNext()=F -> return False

Results: [1, 2, 2, 3, false]
```

| Step | Method Called | Cache Status Before Call | Action Taken | Returned Value | Cache Status After Call | Underlying Iterator State |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 1 | `next()` | Empty (`False`) | Read directly from iterator | **1** | Empty (`False`) | Points to 2 |
| **2** | `peek()` | Empty (`False`) | **Prefetch into cache** | **2** | **Full (`True`, val $= 2$)** | Points to 3 |
| **3** | `next()` | **Full (`True`, val $= 2$)** | **Consume from cache** | **2** | **Empty (`False`)** | Points to 3 |
| 4 | `next()` | Empty (`False`) | Read directly from iterator | **3** | Empty (`False`) | Exhausted |
| **5** | `hasNext()` | Empty (`False`) | Evaluate `has_peeked or hasNext()` | **`false`** | Empty (`False`) | Exhausted |

---

## 5. Algorithmic Correctness

**Soundness.** `peek()` returns the immediate upcoming element without advancing the user's visible sequence. When `next()` follows `peek()`, it yields the identical value that was displayed by `peek()`, fulfilling the contract of lookahead idempotency.

**Completeness.** `hasNext()` returns `True` whenever either `has_peeked` is True (a value is buffered in memory ready to be served) or `iterator.hasNext()` is True (more values remain in the source). No element is skipped or duplicated.

---

## 6. Traps This Instance Exposes

- **Calling Underlying `next()` on Every `peek()`:** If `peek()` is called three times in a row, naively calling `iterator.next()` on each invocation would advance the underlying iterator 3 times, skipping elements! Guarding with `if not self.has_peeked` ensures prefetching happens at most once until consumed.
- **Using `None` as an Empty-Cache Sentinel:** In generic languages (e.g. Java, Python), a list can contain `None` or `null` as valid elements. Checking `if self.peeked_element is not None` fails when `None` is the stored value. An independent boolean flag `has_peeked` prevents this bug.
- **Underlying Iterator Exhaustion After `peek()`:** When peeking at the final element, the underlying iterator's `hasNext()` becomes False. If `hasNext()` only checked the underlying iterator, it would incorrectly report that no elements remain! Checking `self.has_peeked or self.iterator.hasNext()` properly preserves the availability of the cached element.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time for all operations (`peek`, `next`, `hasNext`). Each operation executes at most a constant number of attribute checks, assignments, and at most one underlying iterator call.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary space. Only a single lookahead variable (`peeked_element`) and a boolean flag (`has_peeked`) are stored.

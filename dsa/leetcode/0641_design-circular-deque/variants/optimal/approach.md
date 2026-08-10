## General

**Represent a logical deque inside a fixed array**

The deque has a fixed capacity `k`. A normal array already provides exactly `k` storage slots, but repeatedly shifting values to insert or delete at the front would be too expensive. The circular design avoids all shifting by allowing the logical sequence to wrap from the last physical array index back to index zero.

The implementation stores three pieces of state:

- `q` is the fixed array of length `capacity`;
- `front` is the physical index of the logical front element when the deque is nonempty;
- `size` is the number of logical elements currently stored.

The capacity never changes. Empty and full states are determined by `size`, which avoids the ambiguity that occurs if front and rear indices alone are equal in both situations.

**The mapping that makes every operation understandable**

For every logical offset `t` from zero through `size - 1`, the element at that position in the deque is stored at:

`(front + t) % capacity`.

Offset zero is the front. Offset `size - 1` is the rear. The modulo operation wraps an index back into the valid range `0` through `capacity - 1`.

For example, suppose the capacity is five, `front` is four, and `size` is three. The logical elements occupy physical indices four, zero, and one. Their physical order looks split, but the formula reads them as one continuous logical deque.

This mapping is the central invariant. Each method either preserves it without moving values or changes `front` and `size` so that it remains true.

**Insert at the front**

Insertion must first reject a full deque. If `size == capacity`, every array slot already belongs to a logical element, so overwriting any slot would destroy data and the method returns `False`.

For a nonempty deque, the new front must occupy the slot immediately before the old front:

`(front - 1 + capacity) % capacity`.

Adding `capacity` before modulo keeps the intermediate value nonnegative and makes the intention portable to languages whose remainder behavior for negative values differs from Python's.

The value is written at the new `front`, then `size` increases by one. Every old element's physical index stays unchanged, but its logical offset increases by one, so the mapping still holds.

For an empty deque, the implementation does not move `front`. There is no old front that must be preceded; it simply writes the first value at the current index. This is correct even if prior deletions left `front` at any wrapped position. That position becomes both the logical front and rear.

**Insert at the rear**

The rear insertion position is one logical offset after all existing elements. Since the current offsets are zero through `size - 1`, the free rear slot is:

`(front + size) % capacity`.

After writing there, incrementing `size` makes that slot the new offset `size - 1`. No existing value moves. The same formula works when the deque is empty because `size` is zero, so the first value is written at `front`.

**Delete from the front**

An empty deque has no value to remove, so deletion returns `False` without changing state.

Otherwise, the element currently at offset one must become the new offset zero. Its physical index is `(front + 1) % capacity`, so the method advances `front` to that index and decreases `size`.

The old array cell is not cleared. Clearing is unnecessary because membership is defined by `front` and `size`, not by the numeric contents of `q`. Once `front` advances, that stale value lies outside the logical deque and may later be overwritten.

If the deletion removes the last element, `size` becomes zero and `front` still advances. That is harmless: an empty deque has no meaningful stored element, and the next insertion can use whatever valid index `front` currently contains.

**Delete from the rear**

The rear is determined from `front` and `size` rather than stored separately. Removing it therefore needs only to decrease `size` by one. Under the mapping, the old rear was at offset `size - 1`. After the decrement, that offset is outside the logical range, so the value has been logically removed even though its stale bits remain in the array.

No pointer movement or clearing is necessary. This is one of the benefits of representing the rear implicitly.

**Read the front and rear**

Both accessors return `-1` when the deque is empty, as required by the interface.

For a nonempty deque, the front value is directly `q[front]`. The rear is the element at logical offset `size - 1`, so its physical index is:

`(front + size - 1) % capacity`.

This formula works across wraparound. If `front` is zero and `size` is one, it returns zero. If `front` is four in a capacity-five array and `size` is three, it returns physical index one, matching the wrapped example.

**Why the representation remains correct**

Initially, `size` is zero, so the mapping has no required elements and the representation is valid. Each successful front insertion creates a new offset zero and shifts only the logical offsets of existing values. Each successful rear insertion writes exactly the next logical offset. A front deletion advances the base index so old offset one becomes new offset zero. A rear deletion shortens the valid offset range by one. Accessors do not mutate anything.

Full and empty checks prevent insertions or deletions that would violate the range `0 <= size <= capacity`. By considering every mutating operation, the logical-to-physical mapping and the size bounds are preserved after every call. The access formulas derived from that mapping therefore always return the correct values.

## Complexity detail

Let `Q` be the number of method calls after construction and `k` be the requested capacity.

Construction allocates and initializes an array of `k` entries, so it takes `O(k)` time and `O(k)` space. Each later operation performs only a fixed number of comparisons, arithmetic operations, array accesses, and assignments. No method loops over the contents, so every individual operation is `O(1)` and a sequence of `Q` operations takes `O(Q)` time.

The backing array is the only storage that grows with capacity, giving `O(k)` space. The indices, size, and capacity use `O(1)` additional scalar storage. Stale values do not consume extra space; they remain in already allocated slots.

Modulo is constant-time under the usual bounded-integer model. The constraints ensure positive capacity, so no operation attempts a modulo by zero.

## Alternatives and edge cases

- **Doubly linked list:** Front and rear insertion and deletion are constant-time with head and tail pointers, but every element needs node allocation and two links. The fixed-capacity array is more compact, cache-friendly, and naturally enforces the maximum size.

- **Python's built-in deque:** It already provides efficient end operations, but using it would sidestep the purpose of designing the circular structure. It would also need an explicit capacity policy for failed insertions.

- **Shifting an ordinary array:** Keeping the front permanently at index zero requires moving all elements for front insertions and deletions, making those operations `O(k)`. Circular indexing is what removes those shifts.

- **Two indices without a size:** If front and rear positions are equal, the structure needs another convention to distinguish empty from full, often sacrificing one slot. Tracking `size` permits all `k` slots to be used and makes the predicates direct.

- **Capacity one:** Empty insertion writes at `front` and makes the deque full. Both front and rear access the same slot. Either deletion returns it to empty. The modulo formulas remain valid.

- **Insertion into an empty deque:** `insertFront` deliberately does not move `front`, while `insertLast` calculates the same current index. In both cases the only element is simultaneously front and rear.

- **Deletion of the last element:** Front deletion advances `front` and rear deletion does not, so they may leave different empty-state indices. Both are valid because the next insertion reestablishes the one-element mapping from whichever index remains.

- **Wraparound:** Inserting at the front when `front` is zero moves it to `capacity - 1`. Inserting at the rear beyond the last index wraps to zero. Physical order is irrelevant as long as the modulo mapping is preserved.

- **Stale array values:** Deletions do not erase slots. Methods must never use a sentinel value to infer membership; only `front` and `size` define which cells are live.

- **Stored value equal to `-1`:** The allowed inserted values are positive under the reference constraints, so `-1` is unambiguous as an empty-access result. Even with arbitrary values, emptiness would still be determined by `size`; callers would simply have an interface ambiguity.

- **Failed operation:** An insertion on a full deque or deletion on an empty one must return `False` and leave every state field unchanged. Checking the condition before any index or size mutation guarantees that behavior.

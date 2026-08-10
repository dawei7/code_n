## General

**Represent one logical queue with two deques**

The full sequence is always

`q1 followed by q2`.

`q1` stores the left portion and `q2` stores the right portion. The rebalancing method maintains this size invariant:

$$
\lvert q1\rvert \le \lvert q2\rvert \le \lvert q1\rvert+1.
$$

Thus the halves have equal size when the total length is even, and `q2` has the one extra element when it is odd. Both are `deque` objects, so inserting or removing at either end takes constant time.

This invariant places the middle at a boundary:

- for an even total length, the frontmost of the two middle positions is the last element of `q1`;
- for an odd total length, the unique middle is the first element of `q2`.

That is why middle operations never need to walk through the queue.

**How rebalancing restores the invariant**

Every public operation changes the length by at most one before calling `rebalance`, so the halves can be only slightly out of balance.

If `len(q1) > len(q2)`, the left half has one extra element. `q1.pop()` removes its boundary element and `q2.appendleft(...)` places that same value at the front of the right half. The concatenated logical order is unchanged.

If `len(q2) > len(q1) + 1`, the right half has too many elements. `q2.popleft()` removes its first boundary element and `q1.append(...)` places it at the end of the left half, again preserving full order.

The conditions are separate `if` statements, but after one ordinary public operation at most one transfer is needed. The result always satisfies the invariant.

**Push operations**

`pushFront` inserts with `q1.appendleft(val)` because the front of `q1` is the front of the entire sequence. Rebalancing may move the last left-half value across the middle, but it never moves the newly inserted front out of first position.

`pushBack` uses `q2.append(val)` because the back of `q2` is the logical back. If `q2` becomes two larger than `q1`, its first value moves to `q1`; the newly appended value remains at the back.

`pushMiddle` first appends `val` to the end of `q1`. If the old length was odd, `q2` previously had one extra element; the append makes sizes equal, and the new value sits immediately before the old right half at the correct insertion index. If the old length was even, the append makes `q1` one larger; rebalancing moves its last element—the inserted value—to the front of `q2`, again placing it at the middle boundary. Both parity cases implement the required middle insertion.

**Pop operations**

`popFront` first handles emptiness. Normally the front is `q1.popleft()`. A valid nonempty state can have empty `q1` only when the queue has exactly one element in `q2`, so the fallback `q2.popleft()` handles that case. Rebalancing restores sizes afterward.

For `popMiddle`, equal half sizes mean an even total length. The required frontmost middle is the last item in `q1`, so the code uses `q1.pop()`. If sizes differ, `q2` has one extra element and its first item is the unique middle, so the code uses `q2.popleft()`.

`popBack` removes `q2.pop()`. Under the invariant, if `q2` is empty then `q1` must also be empty, so checking only `not self.q2` is a sufficient emptiness test. After any successful removal, rebalancing preserves the representation.

**Why all operations are correct**

Assume before an operation that concatenating `q1` and `q2` gives the logical queue and the size invariant holds. Each push or pop changes exactly the intended physical end or the precisely characterized middle boundary. Rebalancing transfers only a boundary value between deques and therefore does not change their concatenation. It restores the size invariant.

The constructor begins with two empty deques, which satisfy both claims. By induction, every method returns or inserts the correct element and leaves a valid representation for the next call. Empty pops return `-1` without changing state, as required.

## Complexity detail

Each public operation performs a constant number of `deque` end operations, comparisons, and at most one boundary transfer. Python deque append, append-left, pop, and pop-left operations are $O(1)$ amortized, so every push and pop is $O(1)$ amortized time.

For `Q` total method calls, total time is $O(Q)$, matching the manifest. If the queue contains `S` current elements, the two deques store exactly those `S` values and use $O(S)$ space, at most $O(Q)$ over the operation history.

No operation copies the full queue or scans to its middle. The object keeps only two deque references in addition to the stored values.

## Alternatives and edge cases

- **Python list:** Front or middle insertion and removal shifts many elements, costing $O(S)$ per operation in the worst case.
- **One deque with rotation:** Rotating to reach the middle can be linear per middle operation. Two balanced deques keep the middle exposed permanently.
- **Doubly linked list plus middle pointer:** This can also support constant-time operations, but updating the middle across all parity changes requires more custom pointer logic.
- **Empty pop:** `popFront` and `popMiddle` test both halves; `popBack` tests only `q2` because the invariant makes an empty right half imply an empty queue.
- **One element:** It resides in `q2`. All three pop methods remove and return that same sole value.
- **Even-length middle pop:** There are two central positions, and `q1.pop()` selects the frontmost one exactly as required.
- **Odd-length middle pop:** The unique center is `q2[0]`, removed with `popleft`.
- **Middle push after even length:** Rebalancing moves the new boundary value into the front of `q2`, producing the prescribed insertion position.
- **Middle push after odd length:** No transfer is needed after appending to `q1`; the inserted value is directly before the old center.
- **Repeated front or back operations:** Rebalancing moves only one boundary item each time, so the invariant never drifts.
- **Value `-1`:** Inserted values are at least one, so `-1` is an unambiguous empty-pop sentinel.

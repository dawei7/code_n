## General
**Attach deferred work to stack depths.** Store the pushed values normally and keep a parallel `increments` array. Entry `i` represents an addition that applies to every value from the bottom through depth `i`.

For `increment(k, val)`, find the deepest affected index, `min(k, size) - 1`, and add `val` only to that increment marker. No stored value needs to be changed immediately.

When popping depth `i`, add its marker to the stored value. If a lower element remains, propagate the same marker to depth `i - 1`, because every deferred increment covering the popped element also covered all elements below it. This transfers each marker downward exactly when needed and ensures a later pop receives every increment that included its depth.

A push appends a zero marker, so increments issued before that push never affect the new value. A full-stack push is ignored, and an empty pop returns `-1`, preserving the bounded-stack contract.

## Complexity detail
Each `push`, `pop`, and `increment` performs constant work, so every operation takes $O(1)$ time. The values and deferred markers contain at most `maxSize` entries, using $O(\texttt{maxSize})$ space.

## Alternatives and edge cases
- **Update values eagerly:** Add `val` directly to the bottom `k` entries. It is simple and correct but takes $O(k)$ time per increment.
- **Difference array without pop propagation:** Range markers can encode increments, but they must be accumulated in the correct direction when values are removed.
- **Push at capacity:** Ignore the value without changing either internal array.
- **Pop when empty:** Return `-1` and leave deferred state empty.
- **Increment beyond current size:** Affect every stored element, not nonexistent capacity slots.
- **Increment an empty stack:** Do nothing; no marker should be retained for future pushes.
- **Overlapping increments:** Markers add together and propagate, so each popped value receives precisely the operations whose bottom ranges covered it.

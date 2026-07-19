## General
**Replace the unavailable predecessor operation**

Ordinary deletion changes the predecessor's `next`, but that predecessor is unavailable. The guaranteed successor provides an equivalent representation trick.

**Make the given object represent its successor**

Copy the successor's value into the given node, then point the given node directly to the successor's next node. The externally visible value sequence loses exactly the requested value.

Nodes before the given object remain untouched. After copying, the given object represents its former successor; bypassing that successor restores the remainder of the original suffix.

Before mutation the suffix is `[target, next, rest...]`. After copying and bypassing it is `[next, rest...]`, exactly the sequence obtained by deleting the target position. No other list position changes.

The object identity of the supplied node remains in the list, but the contract observes the list's value sequence rather than requiring that exact object to be detached. This distinction is what makes constant-time deletion possible without the predecessor.

## Complexity detail
One value assignment and one pointer assignment take $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Shift every later value left:** is correct but takes $O(n)$ time.
- **Search from the head:** is impossible because the head is not supplied.
- The method requires a successor, which is why the target is guaranteed not to be the tail.

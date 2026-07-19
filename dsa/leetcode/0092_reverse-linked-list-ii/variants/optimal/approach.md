## General
**Preserve the prefix-to-segment boundary before reversal**

Advance `current` to one-based position `left`, retaining `before`, the node immediately preceding it when one exists. Save this first segment node as `segment_tail`; after reversal, it will be the last node of the segment and must reconnect to the suffix.

**Bound standard pointer reversal by segment length**

Repeat standard pointer reversal exactly `right - left + 1` times. Save `current.next` before overwriting it, point `current.next` to `previous`, and advance both pointers. At completion, `previous` is the segment's new head and `current` is the first untouched suffix node.

Using the known node count prevents reversal from leaking into the suffix and avoids needing value-based or null-based stopping conditions.

**Repair the two links that cross segment boundaries**

First connect `segment_tail.next = current`, repairing the segment-to-suffix boundary. Then connect `before.next = previous`, repairing the prefix-to-segment boundary. If `before` is null because `left = 1`, `previous` itself becomes the overall head.

**Outside nodes remain untouched while internal links flip**

During reversal, `previous` heads exactly the already-reversed portion of the requested segment, while `current` heads its unprocessed portion followed by the original suffix. The prefix is temporarily disconnected but otherwise unchanged, and saved boundary pointers keep every part reachable for final reconnection.

**Trace a reversal that changes the head**

For `[1,2,3]` with `left = 1` and `right = 3`, `before` is null and node `1` is saved as `segment_tail`. Three reversal steps produce head `3` and null suffix. Connecting the tail to the suffix keeps `1.next = null`, and returning `previous` yields `[3,2,1]`.

**Two saved boundary edges make the reversal local**

The loop reverses each link whose source lies inside the selected segment and stops after exactly `right - left + 1` nodes. Saving the prefix predecessor, original segment head, and suffix prevents either external connection from being lost.

After reversal, the prefix predecessor points to the segment's old last node, while the old first node—now the segment tail—points to the untouched suffix. No outside link changes, so exactly the requested positions reverse and every node remains in the chain.

## Complexity detail
At most one traversal locates and reverses the segment, so time is $O(n)$. A constant number of pointers use $O(1)$ space.

## Alternatives and edge cases
- **Copy values to an array and rewrite them backward:** uses $O(right-left)$ space and changes values rather than links.
- **Recursive reversal:** can express the operation but uses linear call-stack space.
- **Repeated adjacent swaps:** can take quadratic time for long segments.
- When `left = right`, one reversal iteration restores the same node between unchanged boundaries.
- The contract guarantees valid positions. A defensive API for out-of-range boundaries would require separate behavior.

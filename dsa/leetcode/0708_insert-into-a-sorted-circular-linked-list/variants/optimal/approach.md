## General
**Recognize the two legal kinds of gap**

For neighboring nodes `current` and `following`, a normal gap accepts the value when `current.val <= insertVal <= following.val`. At the unique wrap from the maximum region to the minimum region, identified by `current.val > following.val`, the value belongs there when it is at least the current maximum or at most the following minimum.

**Walk at most one complete cycle**

Start at `head`, test each adjacent pair, and advance. Stop when a legal gap is found or when advancing returns to `head`.

**Handle indistinguishable placements**

If a full cycle has no selected gap, all values are equal or every gap is equivalent for this insertion. Inserting after the current head is valid.

**Splice one node without breaking the cycle**

Create the node, point it to `current.next`, and then point `current.next` to it. For an empty input, make the new node point to itself. Nonempty insertion returns the original head.

**Why the resulting cycle remains sorted**

In a normal gap, both adjacent inequalities remain valid after splitting the gap. At the wrap, the new value extends either the maximum or minimum end without creating a second descending transition. The fallback cycle is uniform, so any placement is valid. All untouched links retain their previous order.

## Complexity detail
At most `n` adjacent pairs are inspected before insertion, taking $O(n)$ time. Only the current, following, and new node references are stored, so the extra space is $O(1)$.

## Alternatives and edge cases
- **Collect and sort values:** append the new value, sort, and rebuild a cycle; it takes $O(n \log n)$ time and $O(n)$ auxiliary space while unnecessarily replacing links.
- **Restart for every candidate gap:** repeatedly walk from the head to reach each next pair; it preserves the structure but takes $O(n^2)$ time.
- An empty list becomes a one-node self-cycle.
- A one-node or all-equal cycle permits insertion at any link.
- A new minimum or maximum is inserted across the maximum-to-minimum wrap.
- Duplicate values may be inserted into any equal-valued gap.
- The supplied head need not point to the minimum value.

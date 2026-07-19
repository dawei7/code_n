## General
**Preserve stack order with a doubly linked list**

Store each pushed value in a node between permanent head and tail sentinels. The node immediately before the tail is always the stack top. A node can also be unlinked from the middle in constant time, which is essential when `popMax` selects a value below the top.

**Give every occurrence a sequence number**

Assign increasing identifiers to pushes and place `(-value, -identifier)` in a min-heap. Negating the value makes the heap root a maximum. For equal values, the larger identifier was pushed later and is closer to the top, so its more-negative identifier wins the heap tie exactly as required.

**Connect the two views by identifier**

Map each active identifier to its linked-list node. `popMax` cleans obsolete heap roots, removes the current root, finds its node through the map, and unlinks that node. Ordinary `pop` unlinks the tail node and deletes its identifier from the map; its heap entry can remain until it reaches the root.

**Why lazy heap deletion is safe**

An identifier is active precisely while its linked-list node remains in the stack. Heap cleanup discards only identifiers absent from the active map, so it cannot remove a live occurrence. After cleanup, the root has the greatest live value and, among equal values, the greatest live identifier. Thus `peekMax` reports the correct maximum and `popMax` removes its topmost occurrence, while the linked list continues to answer `top` and `pop` in stack order.

## Complexity detail
`top` and ordinary `pop` take $O(1)$ time. A push performs one heap insertion, while `peekMax` and `popMax` perform amortized $O(\log q)$ heap work. Every stale entry is inserted and discarded at most once, so `q` operations take $O(q \log q)$ total time. The linked nodes, active map, and heap use $O(q)$ space.

## Alternatives and edge cases
- **Balanced ordered map plus linked nodes:** map each value to its nodes in stack order; it supports worst-case logarithmic maximum updates, but Python has no built-in balanced ordered map.
- **Two stacks with temporary removal:** maintain a parallel maximum stack and move elements aside during `popMax`; the operation is correct but may take $O(n)$ time.
- **Plain list with a maximum scan:** ordinary stack calls are simple, but every `peekMax` or `popMax` can scan all stored values and make a long sequence quadratic.
- Equal maximum values must be distinguished by push order so `popMax` removes the one closest to the top.
- Negative values require ordinary numeric ordering; the least-negative value is the maximum.
- Heap entries left by ordinary pops are harmless only when every maximum read cleans stale roots first.
- Removing the only element must reconnect the two sentinels and leave both views logically empty.

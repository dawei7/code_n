## General
**First isolate each level in ordinary breadth-first order**

Use a queue and snapshot its size at the start of each depth. Removing exactly that many nodes creates one left-to-right level; children enqueued during the pass wait for the following iteration. Left-before-right child insertion preserves horizontal order.

**Prepend whole levels, never individual node values**

Append each completed level to the left side of a result deque. This reverses depth order while preserving the already-correct left-to-right order inside the level. Prepending individual values would incorrectly reverse horizontal order too.

A deque avoids shifting every previously stored level, which repeated insertion at list index zero could require.

**Traversal proceeds top-down while accumulated output is bottom-up**

Before each queue pass, the queue contains exactly the next depth in left-to-right order. The result deque contains every completed shallower level in reverse depth order.

**Trace level prepending**

The tree `[3, 9, 20, null, null, 15, 7]` produces ordinary levels `[3]`, `[9, 20]`, and `[15, 7]`. Prepending each one leaves `[[15, 7], [9, 20], [3]]`.

**Prepending reverses depth order without reversing levels**

Frozen breadth-first boundaries collect each depth exactly once and retain its left-to-right node order. When a completed level is prepended, it moves ahead of every previously collected shallower level while its internal order remains unchanged.

Each newly discovered depth is deeper than all earlier ones, so repeated prepending produces strictly bottom-to-top level order after the final depth.

## Complexity detail
Every node is enqueued and dequeued once, giving $O(n)$ time. The traversal queue holds at most $O(w)$ nodes; the level deque is part of the required output.

## Alternatives and edge cases
- **Collect top-down then reverse once:** is also $O(n)$ and equally valid.
- **Insert each level at list index zero:** can add quadratic shifting across many levels.
- **Reverse values inside levels:** would change horizontal order and solve a different traversal.
- Empty input returns an empty result. One level is unchanged by bottom-up ordering.
- Collecting all ordinary levels and reversing the outer list once is equally linear and may be simpler when a deque is unavailable.

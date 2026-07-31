## General

**Only the last query for each window determines its final priority.** Every queried window ends ahead of every never-queried window. Among queried windows, the one whose last occurrence is latest finishes first, the next-latest finishes second, and so on. An earlier occurrence becomes irrelevant when the same window is moved to the front again.

Scan `queries` from right to left. The first time a window is seen in this reverse scan is its last occurrence in forward time, so append it to the result and record it in a set. This produces all queried windows directly in their final front-to-back order.

The unqueried windows were never moved relative to one another. Scan the original `windows` order and append every identifier absent from the set. The two parts contain every window exactly once and reproduce the final state without performing any intermediate list mutation.

## Complexity detail

Let $n=\lvert\texttt{windows}\rvert$ and $q=\lvert\texttt{queries}\rvert$. The reverse query scan and final window scan take $O(n+q)$ expected time with hash-set membership. The result and seen set use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Literal remove and insert:** Finding and moving each queried window in an array is correct but can take $O(nq)$ time.
- **Linked list alone:** Moving a known node is constant time, but locating nodes and restoring output order still require additional indexing and traversal state.
- Repeating one query does not duplicate that window in the result.
- Querying the current top window leaves the order unchanged.
- If every window is queried, reverse last-occurrence order is the entire answer.
- If only some windows are queried, all others retain their original relative order.
- A single-window permutation remains unchanged under every valid query.
- The input `windows` is a permutation, so each unqueried identifier is appended exactly once.

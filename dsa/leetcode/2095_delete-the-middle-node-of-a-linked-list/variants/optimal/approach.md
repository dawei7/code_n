## General
**Positioning a pointer before the node to remove**

Use a slow pointer that advances one node per iteration and a fast pointer that advances two. Start the slow pointer at the head and the fast pointer two nodes ahead. When the fast pointer reaches the end, the slow pointer is immediately before index $\lfloor n/2 \rfloor$.

The one-node list is handled separately because its middle is the head itself and no predecessor exists. For all longer lists, bypass the middle with `slow.next = slow.next.next`.

**Why the even case chooses the second center**

For length $2q$, the fast pointer can make $q-1$ two-node advances from index `2` before stopping, leaving slow at index $q-1$ and deleting index $q$. For length $2q+1$, it leaves slow at the same predecessor index and deletes index $q$. These are exactly the required floors.

**Why the remaining links are preserved**

No pointer before `slow` is changed, and the only update connects the middle's predecessor directly to its successor. Thus every other node remains in original order, while exactly the designated node becomes unreachable from the returned head.

## Complexity detail
The fast pointer traverses at most $n$ links and the slow pointer at most half as many, so the time is $O(n)$. Only two pointers are stored and the list is modified in place, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Two linear passes:** First count the nodes, then walk to the middle predecessor; this is also $O(n)$ time and $O(1)$ space but traverses more links.
- **Store nodes in an array:** Random access makes the middle easy to locate but requires $O(n)$ auxiliary space.
- **Repeated traversal by index:** Starting from the head for every successive position eventually locates the middle but takes $O(n^2)$ time.
- A one-node list becomes empty.
- For two nodes, index `1` is deleted and the head remains.
- Node values may repeat; the node is selected only by position.

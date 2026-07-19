## General
**Let one pointer measure twice the progress of the other**

Initialize `slow` and `fast` at `head`. While `fast` has both a current node and a following node, advance `slow` by one link and `fast` by two links. No node values or list modifications are needed.

After $t$ iterations, `slow` is $t$ links from the head and `fast` is $2t$ links from it. When the loop ends, `fast` has reached the end for an even-length list or the final node for an odd-length list. Exactly $\lfloor n/2\rfloor$ iterations have occurred, placing `slow` at the required zero-based position. For even $n$, that position is deliberately the second middle.

## Complexity detail
The fast pointer crosses the list once and the slow pointer crosses at most half of it, so the total time is $O(n)$. Only two node references are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count, then walk halfway:** A full length pass followed by $\lfloor n/2\rfloor$ steps is also $O(n)$ time and $O(1)$ space, but it requires two traversals.
- **Store every node in an array:** Direct indexing makes the middle easy to select but uses $O(n)$ auxiliary space.
- **Repeatedly measure prefixes and suffixes:** Testing every node by rescanning both sides is correct but takes $O(n^2)$ time.
- **Single node:** The loop never executes and `head` is returned.
- **Two nodes:** One iteration moves `slow` to the second node, enforcing the second-middle rule.
- **Repeated values:** Selection depends on node position, not value, so equal values require no special handling.
